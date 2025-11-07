"""Visualization browser screen."""

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button, DataTable, LoadingIndicator
from textual.binding import Binding
from textual import events

from ..api.client import DatamonkeyClient
from ..utils.vega_editor import generate_vega_editor_url, open_in_vega_editor
import logging

logger = logging.getLogger(__name__)


class VisualizationScreen(Screen):
    """Visualization browser screen with Vega Editor integration."""
    
    BINDINGS = [
        Binding("escape", "pop_screen", "Back"),
        Binding("r", "refresh", "Refresh"),
        Binding("f", "filter", "Filter"),
        Binding("e", "export", "Export"),
        Binding("c", "copy_url", "Copy URL"),
        Binding("v", "open_vega", "Open in Vega Editor"),
        Binding("space", "view_details", "View Details"),
    ]
    
    CSS = """
    VisualizationScreen {
        layout: vertical;
        height: 100%;
    }

    .header {
        padding: 0 1;
    }

    .toolbar {
        margin: 0 1;
        padding: 1 0;
        layout: horizontal;
    }

    .toolbar Button {
        min-width: 14;
        margin-right: 1;
    }

    .table-container {
        margin: 0 1 1 1;
        border: solid $primary;
        padding: 1;
        expand: greedy;
        layout: vertical;
    }

    DataTable.viz-table {
        width: 100%;
        border: solid $primary;
        expand: greedy;
    }

    .info-panel {
        border: solid $secondary;
        padding: 1;
        layout: vertical;
    }

    .info-title {
        text-style: bold;
        color: $primary;
    }

    .info-content {
        height: auto;
    }

    .loading {
        height: 3;
        align: center middle;
    }
    """
    
    def __init__(self, api_client: DatamonkeyClient):
        """Initialize the visualization screen.
        
        Args:
            api_client: The Datamonkey API client
        """
        super().__init__()
        self.api_client = api_client
        self.visualizations = []
        self.current_viz = None
        self._viz_lookup = {}
    
    def compose(self) -> ComposeResult:
        """Create the visualization screen layout."""
        yield Header(classes="header")

        with Horizontal(classes="toolbar"):
            yield Button("🔄 Refresh", id="refresh-btn")
            yield Button("🔍 Filter", id="filter-btn")
            yield Button("🗑️ Delete", id="delete-btn", disabled=True)
            yield Button("📤 Export", id="export-btn", disabled=True)
            yield Button("📋 Copy URL", id="copy-btn", disabled=True)
            yield Button("🌐 Open Vega", id="vega-btn", disabled=True)

        with Vertical(classes="table-container"):
            yield DataTable(id="viz-table", classes="viz-table")
            with Vertical(classes="info-panel"):
                yield Static("Selected Visualization", classes="info-title")
                yield Static("None selected", id="viz-info", classes="info-content")

        yield Footer()
    
    def key_esc(self) -> None:
        """Handle ESC key to go back to main screen."""
        self.app.pop_screen()
    
    async def on_mount(self) -> None:
        """Initialize the screen when mounted."""
        await self.setup_table()
        await self.load_visualizations()

    
    async def setup_table(self) -> None:
        """Set up the data table columns."""
        table = self.query_one("#viz-table", DataTable)
        
        table.add_column("ID", key="id", width=20)
        table.add_column("Title", key="title", width=25)
        table.add_column("Job ID", key="job_id", width=12)
        table.add_column("Dataset", key="dataset", width=12)
        table.add_column("Created", key="created", width=15)
        
        table.cursor_type = "row"
    
    async def load_visualizations(self, job_id: str = None, dataset_id: str = None) -> None:
        """Load the list of visualizations."""
        try:
            # Show loading indicator
            loading = LoadingIndicator()
            self.mount(loading)
            
            response = await self.api_client.list_visualizations(job_id, dataset_id)
            table = self.query_one("#viz-table", DataTable)
            
            # Clear existing rows only (preserve columns)
            table.clear(columns=False)
            
            info_widget = self.query_one("#viz-info", Static)
            info_widget.update("None selected")
            self.current_viz = None
            self._viz_lookup.clear()

            if response.visualizations:
                self.visualizations = response.visualizations
                self.notify(f"Loading {len(response.visualizations)} visualizations...")

                for idx, viz in enumerate(response.visualizations):
                    viz_id = getattr(viz, "viz_id", None)
                    job_id = getattr(viz, "job_id", None)
                    dataset_id = getattr(viz, "dataset_id", None)
                    title = getattr(viz, "title", None)
                    created_value = getattr(viz, "created_at", None)

                    viz_id_display = (viz_id[:20] + "...") if viz_id and len(viz_id) > 20 else (viz_id or "Unknown")
                    job_display = (job_id[:12] + "...") if job_id and len(job_id) > 12 else (job_id or "")
                    dataset_display = (dataset_id[:12] + "...") if dataset_id and len(dataset_id) > 12 else (dataset_id or "")
                    created_str = self.format_date(created_value)

                    try:
                        row_key = viz_id or str(idx)
                        table.add_row(
                            viz_id_display,
                            title or "Untitled",
                            job_display,
                            dataset_display,
                            created_str,
                            key=row_key,
                        )
                        self._viz_lookup[row_key] = viz
                        self.notify(f"Added viz row {idx+1}: {title or 'Untitled'}")
                    except Exception as row_err:
                        self.notify(f"Failed to add viz row {idx+1}: {row_err}")
                
                # Force table refresh
                table.refresh()
                self.notify(f"✅ Loaded {len(response.visualizations)} visualizations. Table has {table.row_count} rows.")
            else:
                table.add_row("No visualizations", "", "", "", "", key="empty")
                table.refresh()
                self.notify("No visualizations found")
                
            loading.remove()
            
        except ValueError as e:
            # Handle authentication requirement
            loading.remove()
            if "Authentication required" in str(e):
                self.notify("🔐 Please create a job or visualization first to get authenticated")
                table = self.query_one("#viz-table", DataTable)
                table.clear(columns=False)
                table.add_row("Create your first job to get started", "", "", "", "")
            else:
                self.notify(f"Failed to load visualizations: {e}")
        except Exception as e:
            loading.remove()
            self.notify(f"Failed to load visualizations: {e}")
    
    def format_date(self, date_str: str) -> str:
        """Format date string."""
        try:
            return date_str[:10] if date_str else "N/A"
        except:
            return "N/A"
    
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "refresh-btn":
            await self.action_refresh()
        elif event.button.id == "filter-btn":
            await self.action_filter()
        elif event.button.id == "delete-btn":
            await self.action_delete()
        elif event.button.id == "export-btn":
            await self.action_export()
        elif event.button.id == "copy-btn":
            await self.action_copy_url()
        elif event.button.id == "vega-btn":
            await self.action_open_vega()
    
    async def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle visualization row selection."""
        if event.row_key and event.row_key.value:
            key = str(event.row_key.value)
            if key in self._viz_lookup:
                await self.view_visualization(self._viz_lookup[key])

    async def view_visualization(self, visualization) -> None:
        """Display visualization details."""
        self.current_viz = visualization
        info_widget = self.query_one("#viz-info", Static)

        spec = getattr(visualization, 'spec', None)
        logger.info("Raw visualization spec", extra={
            "type": type(spec).__name__,
            "preview": str(spec)[:200],
        })
        dataset_id = getattr(visualization, "dataset_id", None) or "N/A"
        job_id = getattr(visualization, "job_id", None) or "N/A"
        created = getattr(visualization, "created_at", None)
        created_str = self.format_date(created)

        details = [
            f"ID: {getattr(visualization, 'viz_id', 'N/A')}",
            f"Title: {getattr(visualization, 'title', 'Untitled')}",
            f"Job: {job_id}",
            f"Dataset: {dataset_id}",
            f"Created: {created_str}",
        ]

        if spec and isinstance(spec, dict):
            preview_keys = ", ".join(list(spec.keys())[:5]) or "(empty spec)"
            details.append(f"Spec keys: {preview_keys}")
        info_widget.update("\n".join(details))

        self.notify(f"Viewing: {getattr(visualization, 'title', 'Unknown')} visualization")
        self._set_action_buttons_state(enabled=True)

    async def action_refresh(self) -> None:
        """Refresh the visualization list."""
        await self.load_visualizations()
    
    async def action_filter(self) -> None:
        """Filter visualizations."""
        # TODO: Implement filter dialog
        self.notify("Filter feature coming soon")
    
    async def action_export(self) -> None:
        """Export visualization spec."""
        if not self.current_viz:
            self.notify("Please select a visualization first")
            return

        spec = getattr(self.current_viz, 'spec', None)
        if spec:
            # TODO: Implement file save dialog
            self.notify("Export feature coming soon")
        else:
            self.notify("No specification to export")

    
    async def action_copy_url(self) -> None:
        """Copy Vega Editor URL to clipboard."""
        if not self.current_viz:
            self.notify("Please select a visualization first")
            return
        
        spec = getattr(self.current_viz, 'spec', None)
        if spec:
            try:
                import pyperclip
                url = generate_vega_editor_url(spec)
                pyperclip.copy(url)
                self.notify("Vega Editor URL copied to clipboard!")
            except ImportError:
                self.notify("Install pyperclip for clipboard support: pip install pyperclip")
            except Exception as e:
                self.notify(f"Failed to copy URL: {e}")
        else:
            self.notify("No specification to generate URL")
    
    async def action_open_vega(self) -> None:
        """Open visualization in Vega Editor."""
        if not self.current_viz:
            self.notify("Please select a visualization first")
            return
        
        spec = getattr(self.current_viz, 'spec', None)
        if spec:
            try:
                url = open_in_vega_editor(spec)
                self.notify(f"Opened in browser: {url[:50]}...")
            except Exception as e:
                self.notify(f"Failed to open Vega Editor: {e}")
        else:
            self.notify("No specification to open")
    
    async def action_view_details(self) -> None:
        """View details of selected visualization."""
        table = self.query_one("#viz-table", DataTable)
        
        if table.cursor_row is None:
            self.notify("Please select a visualization first")
            return
        
        row_key = str(table.cursor_key.value)
        if row_key in self._viz_lookup:
            await self.view_visualization(self._viz_lookup[row_key])

    async def action_delete(self) -> None:
        """Delete selected visualization."""
        if not self.current_viz:
            self.notify("Please select a visualization first")
            return

        viz_id = getattr(self.current_viz, "viz_id", None)
        if not viz_id:
            self.notify("Cannot delete visualization without ID")
            return

        try:
            await self.api_client.delete_visualization(viz_id)
            self.notify(f"🗑️ Deleted visualization {viz_id}")
            await self.load_visualizations()
        except Exception as err:
            self.notify(f"Failed to delete visualization: {err}")
        finally:
            self._set_action_buttons_state(enabled=False)

    def _set_action_buttons_state(self, *, enabled: bool) -> None:
        """Enable or disable actions that require a selection."""
        for button_id in ("delete-btn", "export-btn", "copy-btn", "vega-btn"):
            button = self.query_one(f"#{button_id}", Button)
            button.disabled = not enabled
