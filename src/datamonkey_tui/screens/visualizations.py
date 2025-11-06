"""Visualization browser screen."""

import json
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button, DataTable, LoadingIndicator, TextArea
from textual.binding import Binding
from textual import events

from ..api.client import DatamonkeyClient
from ..config.session import session_manager
from ..utils.vega_editor import generate_vega_editor_url, open_in_vega_editor


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
        layout: grid;
        grid-size: 1 2;
        grid-columns: 1fr 1fr;
        grid-rows: auto 1fr auto;
    }
    
    .header {
        column-span: 2;
    }
    
    .list-container {
        border: solid $primary;
        margin: 1;
        padding: 1;
    }
    
    .detail-container {
        border: solid $secondary;
        margin: 1;
        padding: 1;
    }
    
    .title {
        text-style: bold;
        color: $primary;
        margin: 0 0 1 0;
    }
    
    .actions {
        margin: 1 0;
    }
    
    .action-button {
        margin: 0 1;
        background: $primary;
    }
    
    .spec-display {
        height: 100%;
        background: $surface;
        border: solid $panel;
        padding: 1;
    }
    
    .status {
        text-align: center;
        color: $text-muted;
        margin: 1 0;
        column-span: 2;
    }
    
    DataTable {
        height: 20;
    }
    
    .loading {
        height: 3;
        align: center middle;
    }
    
    .url-display {
        background: $surface;
        border: solid $primary;
        padding: 1;
        margin: 1 0;
        height: 3;
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
    
    def compose(self) -> ComposeResult:
        """Create the visualization screen layout."""
        yield Header(classes="header")
        
        # Visualization list
        with Vertical(classes="list-container"):
            yield Static("📊 Visualizations", classes="title")
            
            with Horizontal(classes="actions"):
                yield Button("🔄 Refresh", id="refresh-btn", classes="action-button")
                yield Button("🔍 Filter", id="filter-btn", classes="action-button")
            
            yield DataTable(id="viz-table")
        
        # Visualization details
        with Vertical(classes="detail-container"):
            yield Static("Visualization Details", classes="title")
            
            with Horizontal(classes="actions"):
                yield Button("📤 Export", id="export-btn", classes="action-button")
                yield Button("📋 Copy URL", id="copy-btn", classes="action-button")
                yield Button("🌐 Open Vega", id="vega-btn", classes="action-button")
            
            with ScrollableContainer(classes="spec-display"):
                yield TextArea(id="spec-display", language="json")
            
            yield Static("Vega Editor URL:", classes="url-display", id="url-display")
        
        yield Static("Select a visualization to view details", classes="status")
        yield Footer()
    
    def key_esc(self) -> None:
        """Handle ESC key to go back to main screen."""
        self.app.pop_screen()
    
    async def on_mount(self) -> None:
        """Initialize the screen when mounted."""
        # Make spec display readonly
        spec_widget = self.query_one("#spec-display", TextArea)
        spec_widget.readonly = True
        
        await self.setup_table()
        await self.load_visualizations()
    
    async def setup_table(self) -> None:
        """Set up the data table columns."""
        table = self.query_one("#viz-table", DataTable)
        
        table.add_column("ID", key="id", width=15)
        table.add_column("Type", key="type", width=15)
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
            
            # Clear existing data
            table.clear()
            
            if response.visualizations:
                self.visualizations = response.visualizations
                
                for viz in response.visualizations:
                    # Format date
                    created_str = self.format_date(viz.created_at) if hasattr(viz, 'created_at') else "N/A"
                    
                    table.add_row(
                        viz.id[:12] + "...",
                        viz.type or "Unknown",
                        (viz.job_id or "")[:8] + "...",
                        (viz.dataset_id or "")[:8] + "...",
                        created_str
                    )
            else:
                table.add_row("No visualizations", "", "", "", "")
                
            loading.remove()
            
        except ValueError as e:
            # Handle authentication requirement
            loading.remove()
            if "Authentication required" in str(e):
                self.notify("🔐 Please create a job or visualization first to get authenticated")
                table = self.query_one("#viz-table", DataTable)
                table.clear()
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
        elif event.button.id == "export-btn":
            await self.action_export()
        elif event.button.id == "copy-btn":
            await self.action_copy_url()
        elif event.button.id == "vega-btn":
            await self.action_open_vega()
    
    async def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle visualization row selection."""
        if event.row_key and event.row_key.value:
            viz_index = event.row_key.value - 1  # Row keys are 1-based
            if 0 <= viz_index < len(self.visualizations):
                await self.view_visualization(self.visualizations[viz_index])
    
    async def view_visualization(self, visualization) -> None:
        """Display visualization details."""
        self.current_viz = visualization
        
        # Update spec display
        spec_widget = self.query_one("#spec-display", TextArea)
        spec_widget.clear()
        
        if hasattr(visualization, 'spec') and visualization.spec:
            # Format JSON nicely
            spec_json = json.dumps(visualization.spec, indent=2)
            spec_widget.insert(spec_json)
        else:
            spec_widget.insert("No specification available")
        
        # Generate and display Vega Editor URL
        if hasattr(visualization, 'spec') and visualization.spec:
            url = generate_vega_editor_url(visualization.spec)
            url_widget = self.query_one("#url-display", Static)
            url_widget.update(f"Vega Editor URL: {url[:80]}...")
        
        self.notify(f"Viewing: {visualization.type or 'Unknown'} visualization")
    
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
        
        if hasattr(self.current_viz, 'spec') and self.current_viz.spec:
            # TODO: Implement file save dialog
            self.notify("Export feature coming soon")
        else:
            self.notify("No specification to export")
    
    async def action_copy_url(self) -> None:
        """Copy Vega Editor URL to clipboard."""
        if not self.current_viz:
            self.notify("Please select a visualization first")
            return
        
        if hasattr(self.current_viz, 'spec') and self.current_viz.spec:
            try:
                import pyperclip
                url = generate_vega_editor_url(self.current_viz.spec)
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
        
        if hasattr(self.current_viz, 'spec') and self.current_viz.spec:
            try:
                url = open_in_vega_editor(self.current_viz.spec)
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
        
        viz_index = table.cursor_row - 1
        if 0 <= viz_index < len(self.visualizations):
            await self.view_visualization(self.visualizations[viz_index])
