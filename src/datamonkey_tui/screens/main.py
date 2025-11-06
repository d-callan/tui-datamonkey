"""Main application screen with navigation."""

import logging
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button

from ..api.client import DatamonkeyClient
from ..config.session import session_manager
from .chat import ChatScreen
from .datasets import DatasetScreen
from .visualizations import VisualizationScreen
from .session import SessionScreen

logger = logging.getLogger("datamonkey_tui.main")


class MainScreen(Screen):
    """Main navigation screen for the TUI."""
    
    BINDINGS = [
        ("c", "push_screen('chat')", "Chat"),
        ("d", "push_screen('datasets')", "Datasets"),
        ("v", "push_screen('visualizations')", "Visualizations"),
        ("s", "push_screen('session')", "Session"),
        ("q", "quit", "Quit"),
        ("escape", "quit", "Quit"),
    ]
    
    CSS = """
    MainScreen {
        align: center middle;
    }
    
    .welcome-container {
        width: 80;
        height: auto;
        padding: 2;
        border: solid green;
        background: $surface;
    }
    
    .title {
        text-align: center;
        color: green;
        text-style: bold;
    }
    
    .subtitle {
        text-align: center;
        color: $text;
        margin: 1 0;
    }
    
    .button-grid {
        width: 100%;
        height: auto;
        margin: 2 0;
    }
    
    .nav-button {
        width: 1fr;
        margin: 0 1;
        background: $primary;
        color: $text;
        text-align: center;
    }
    
    .nav-button:hover {
        background: $primary-lighten-1;
    }
    
    .status {
        text-align: center;
        color: $text-muted;
        margin: 1 0;
    }
    
    .status-success {
        text-align: center;
        color: green;
        text-style: bold;
        margin: 1 0;
    }
    
    .status-warning {
        text-align: center;
        color: yellow;
        text-style: bold;
        margin: 1 0;
    }
    
    .status-info {
        text-align: center;
        color: cyan;
        margin: 0 0 1 0;
    }
    
    .needs-auth {
        background: $error;
        color: $text;
    }
    
    .authenticated {
        background: $success;
        color: $text;
    }
    """
    
    def __init__(self, api_client: DatamonkeyClient):
        """Initialize the main screen.
        
        Args:
            api_client: The Datamonkey API client
        """
        super().__init__()
        self.api_client = api_client
        logger.debug("Main screen initialized")
    
    def refresh_session_status(self) -> None:
        """Refresh the screen to update session status display."""
        logger.info("Refreshing main screen session status")
        self.recompose()
    
    def compose(self) -> ComposeResult:
        """Create the main screen layout."""
        yield Header()
        
        with Vertical(classes="welcome-container"):
            yield Static("🌳 Datamonkey TUI", classes="title")
            yield Static("Terminal Interface for Phylogenetic Analysis", classes="subtitle")
            
            # Session status based on the correct flow
            has_token = session_manager.get_token() is not None
            if has_token:
                yield Static("✅ Authenticated - Ready to use all features!", classes="status-success")
            else:
                yield Static("💡 Start by uploading a dataset or creating a chat to get authenticated", classes="status-info")
                yield Static("📤 Upload dataset or 💬 Create chat → Get token → Use all features", classes="status-info")
            
            with Horizontal(classes="button-grid"):
                yield Button("💬 Chat", id="chat-btn", classes="nav-button")
                yield Button("📁 Datasets", id="datasets-btn", classes="nav-button")
                yield Button("📊 Visualizations", id="visualizations-btn", classes="nav-button")
                yield Button("🔐 Session", id="session-btn", classes="nav-button")
            
            yield Static("Press C, D, V, S or click buttons to navigate", classes="status")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        button_id = event.button.id
        
        if button_id == "chat-btn":
            self.app.push_screen(ChatScreen(self.api_client))
        elif button_id == "datasets-btn":
            self.app.push_screen(DatasetScreen(self.api_client))
        elif button_id == "visualizations-btn":
            self.app.push_screen(VisualizationScreen(self.api_client))
        elif button_id == "session-btn":
            self.app.push_screen(SessionScreen())
    
    def action_push_screen(self, screen_name: str) -> None:
        """Action to push a screen by name."""
        if screen_name == "chat":
            self.app.push_screen(ChatScreen(self.api_client))
        elif screen_name == "datasets":
            self.app.push_screen(DatasetScreen(self.api_client))
        elif screen_name == "visualizations":
            self.app.push_screen(VisualizationScreen(self.api_client))
        elif screen_name == "session":
            self.app.push_screen(SessionScreen())
