"""Dataset management screen."""

import inspect
import os

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Static, Button, DataTable, LoadingIndicator, Input

from textual.markup import escape

from ..api.client import DatamonkeyClient


class UploadDatasetScreen(Screen):
    """Modal-like screen for uploading datasets."""

    BINDINGS = [
        ("escape", "cancel", "Cancel"),
        ("ctrl+v", "paste_path", "Paste Path"),
    ]

    CSS = """
    UploadDatasetScreen {
        align: center middle;
    }

    .upload-container {
        width: 60;
        padding: 2;
        border: solid $primary;
        background: $surface;
    }

    .field-label {
        margin: 1 0 0 0;
        text-style: bold;
    }

    .actions {
        margin-top: 2;
        width: 100%;
    }

    .actions Button {
        margin-right: 1;
    }
    """

    def __init__(self, api_client: DatamonkeyClient, on_complete) -> None:
        super().__init__()
        self.api_client = api_client
        self.on_complete = on_complete
        self._loading_indicator: LoadingIndicator | None = None

    def compose(self) -> ComposeResult:
        with Vertical(classes="upload-container"):
            yield Static("📤 Upload Dataset", classes="field-label")

            yield Static("File path", classes="field-label")
            yield Input(placeholder="/path/to/file.fasta", id="file-path")

            yield Static("Optional name", classes="field-label")
            yield Input(placeholder="Custom dataset name", id="dataset-name")

            yield Static("Optional description", classes="field-label")
            yield Input(placeholder="What is this dataset?", id="dataset-description")

            yield Static("Dataset type (default: fasta)", classes="field-label")
            yield Input(placeholder="fasta", id="dataset-type")

            yield Static("Tip: Use Ctrl+Shift+V or Paste Path to insert clipboard text", classes="field-label")

            with Horizontal(classes="actions"):
                yield Button("Paste Path", id="paste", variant="default")
                yield Button("Upload", id="submit", variant="primary")
                yield Button("Cancel", id="cancel")

    async def handle_submit(self) -> None:
        path_input = self.query_one("#file-path", Input)
        name_input = self.query_one("#dataset-name", Input)
        desc_input = self.query_one("#dataset-description", Input)
        type_input = self.query_one("#dataset-type", Input)

        file_path = path_input.value.strip()
        if not file_path:
            self.notify(escape("Please provide a dataset file path"))
            return

        display_name = name_input.value.strip() or None
        description = desc_input.value.strip() or None
        dataset_type = type_input.value.strip() or None

        self._set_loading(True)

        try:
            if not display_name:
                display_name = os.path.splitext(os.path.basename(file_path))[0]
                name_input.value = display_name

            await self.api_client.upload_dataset(
                file_path,
                name=display_name,
                description=description,
                dataset_type=dataset_type or "fasta",
            )

            self.notify("✅ Dataset uploaded successfully")

            if self.on_complete:
                result = self.on_complete()
                if inspect.isawaitable(result):
                    await result

            self.app.pop_screen()
        except FileNotFoundError as e:
            self.notify(escape(str(e)))
        except Exception as e:
            self.notify(escape(f"Failed to upload dataset: {e}"))
        finally:
            self._set_loading(False)

    def _set_loading(self, is_loading: bool) -> None:
        if is_loading:
            if not self._loading_indicator:
                self._loading_indicator = LoadingIndicator()
                self.mount(self._loading_indicator)
        else:
            if self._loading_indicator:
                self._loading_indicator.remove()
                self._loading_indicator = None

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            await self.handle_submit()
        elif event.button.id == "paste":
            await self.action_paste_path()
        elif event.button.id == "cancel":
            self.app.pop_screen()

    async def action_cancel(self) -> None:
        self.app.pop_screen()

    async def action_paste_path(self) -> None:
        path_input = self.query_one("#file-path", Input)
        try:
            import pyperclip  # type: ignore[import-not-found]
        except ImportError:
            self.notify("Install pyperclip for clipboard support: pip install pyperclip")
            return

        try:
            pasted = pyperclip.paste()
        except Exception as exc:
            self.notify(escape(f"Failed to read clipboard: {exc}"))
            return

        if pasted:
            path_input.value = pasted.strip()
            path_input.focus()
            self.notify("📋 Pasted path from clipboard")
        else:
            self.notify("Clipboard is empty")


class DatasetScreen(Screen):
    """Dataset management screen."""
    
    BINDINGS = [
        ("escape", "pop_screen", "Back"),
        ("r", "refresh", "Refresh"),
        ("u", "upload", "Upload"),
        ("d", "delete", "Delete"),
    ]
    
    CSS = """
    DatasetScreen {
        layout: vertical;
        height: 100%;
    }

    .header-container {
        padding: 1;
        border-bottom: solid $panel;
    }

    .title {
        text-style: bold;
        color: $primary;
    }
    
    .actions {
        margin: 1 0;
    }
    
    .action-button {
        margin: 0 1;
        background: $primary;
    }

    .table-container {
        margin: 0 1 1 1;
        padding: 1;
        border: solid $primary;
        overflow: auto;
        expand: greedy;
    }

    DataTable.dataset-table {
        width: 100%;
        border: solid $primary;
        expand: greedy;
    }

    .loading {
        height: 3;
        align: center middle;
    }

    """
    
    def __init__(self, api_client: DatamonkeyClient):
        """Initialize the dataset screen.
        
        Args:
            api_client: The Datamonkey API client
        """
        super().__init__()
        self.api_client = api_client
        self.datasets = []
    
    def compose(self) -> ComposeResult:
        """Create the dataset screen layout."""
        with Vertical(classes="header-container"):
            yield Static("📁 Datasets", classes="title")
            
            with Horizontal(classes="actions"):
                yield Button("🔄 Refresh", id="refresh-btn", classes="action-button")
                yield Button("📤 Upload", id="upload-btn", classes="action-button")
                yield Button("🗑️ Delete", id="delete-btn", classes="action-button")
        
        with Vertical(classes="table-container"):
            yield DataTable(id="dataset-table", classes="dataset-table")
        
        yield Footer()
    
    def key_esc(self) -> None:
        """Handle ESC key to go back to main screen."""
        self.app.pop_screen()
    
    async def on_mount(self) -> None:
        """Initialize the screen when mounted."""
        await self.setup_table()
        await self.load_datasets()
    
    async def setup_table(self) -> None:
        """Set up the data table columns."""
        table = self.query_one("#dataset-table", DataTable)
        
        table.add_column("ID", key="id", width=20)
        table.add_column("Name", key="name", width=30)
        table.add_column("Type", key="type", width=10)
        table.add_column("Size", key="size", width=10)
        table.add_column("Created", key="created", width=20)
        table.add_column("Status", key="status", width=15)
        
        table.cursor_type = "row"
    
    async def load_datasets(self) -> None:
        """Load the list of datasets."""
        try:
            # Show loading indicator
            loading = LoadingIndicator()
            self.mount(loading)
            
            response = await self.api_client.list_datasets()
            table = self.query_one("#dataset-table", DataTable)
            
            # Clear existing rows only (preserve columns)
            table.clear(columns=False)
            
            if response.datasets:
                self.datasets = response.datasets

                for idx, dataset in enumerate(response.datasets):
                    dataset_id = (dataset.id[:16] + "...") if getattr(dataset, "id", None) else "Unknown"
                    name = getattr(dataset, "name", None) or "Unnamed"
                    dataset_type = getattr(dataset, "type", None) or "Unknown"
                    created_value = getattr(dataset, "created", None)
                    size_str = "N/A"
                    status_str = "N/A"

                    created_str = self.format_date(created_value)

                    try:
                        table.add_row(
                            dataset_id,
                            name,
                            dataset_type,
                            size_str,
                            created_str,
                            status_str,
                        )
                    except Exception as row_err:
                        self.notify(f"Failed to add row {idx+1}: {row_err}")
                
                # Force table refresh
                table.refresh()
                self.notify(f"✅ Loaded {len(response.datasets)} datasets. Table has {table.row_count} rows.")
            else:
                table.add_row("No datasets", "", "", "", "", "")
                table.refresh()
                self.notify("No datasets found")
                
            loading.remove()
            
        except ValueError as e:
            # Handle authentication requirement
            loading.remove()
            if "Authentication required" in str(e):
                self.notify("🔐 Please upload a dataset first to get authenticated")
                table = self.query_one("#dataset-table", DataTable)
                table.clear(columns=False)
                table.add_row("Upload your first dataset to get started", "", "", "", "", "")
            else:
                self.notify(escape(f"Failed to load datasets: {e}"))
        except Exception as e:
            loading.remove()
            self.notify(escape(f"Failed to load datasets: {e}"))
    
    def format_date(self, value) -> str:
        """Format date value from API."""
        if value is None:
            return "N/A"

        try:
            from datetime import datetime

            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            value_str = str(value)
            if len(value_str) >= 10:
                return value_str[:10]
            return value_str
        except Exception:
            return "N/A"
    
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "refresh-btn":
            await self.action_refresh()
        elif event.button.id == "upload-btn":
            await self.action_upload()
        elif event.button.id == "delete-btn":
            await self.action_delete()
    
    async def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle dataset row selection."""
        if event.row_key and event.row_key.value:
            dataset_index = event.row_key.value - 1  # Row keys are 1-based
            if 0 <= dataset_index < len(self.datasets):
                dataset = self.datasets[dataset_index]
                self.notify(escape(f"Selected: {dataset.name or dataset.id}"))
                # TODO: Show dataset details in a modal
    
    async def action_refresh(self) -> None:
        """Refresh the dataset list."""
        await self.load_datasets()
    
    async def action_upload(self) -> None:
        """Upload a new dataset."""
        def _refresh():
            return self.load_datasets()

        self.app.push_screen(UploadDatasetScreen(self.api_client, _refresh))

    async def action_delete(self) -> None:
        """Delete selected dataset."""
        table = self.query_one("#dataset-table", DataTable)
        
        if table.cursor_row is None:
            self.notify("Please select a dataset to delete")
            return
        
        dataset_index = table.cursor_row - 1
        if 0 <= dataset_index < len(self.datasets):
            dataset = self.datasets[dataset_index]
            await self._delete_dataset(dataset.id, dataset.name or dataset.id)

    async def _delete_dataset(self, dataset_id: str, display_name: str) -> None:
        try:
            await self.api_client.delete_dataset(dataset_id)
            self.notify(escape(f"Deleted dataset: {display_name}"))
            await self.load_datasets()
        except Exception as e:
            self.notify(escape(f"Failed to delete dataset: {e}"))
