"""Main Datamonkey TUI application."""

import logging
from textual.app import App

from .api.client import DatamonkeyClient
from .config.settings import settings

logger = logging.getLogger("datamonkey_tui")


class DatamonkeyApp(App):
    """A Textual app for interacting with Datamonkey API."""

    TITLE = "Datamonkey TUI"
    CSS = """
    Screen {
        align: center middle;
    }
    """
    
    def __init__(self):
        """Initialize the app with API client."""
        super().__init__()
        logger.info("Starting Datamonkey TUI application")
        
        # Create API client with token extraction callback
        self.api_client = DatamonkeyClient(on_token_extracted=self.on_token_extracted)
    
    def on_token_extracted(self) -> None:
        """Called when a new token is automatically extracted."""
        logger.info("New token extracted automatically - refreshing UI")
        self.notify("🔐 Auto-authenticated successfully!")
        
        # Refresh main screen if it's the current screen
        if hasattr(self.screen, 'refresh_session_status'):
            self.screen.refresh_session_status()
    
    def on_mount(self) -> None:
        """Set up the initial screen."""
        logger.info("Application mounted, showing main screen")
        from .screens.main import MainScreen
        self.push_screen(MainScreen(self.api_client))
    
    def on_exit(self) -> None:
        """Handle application exit."""
        logger.info("Datamonkey TUI application exiting")
    
    def key_q(self) -> None:
        """Handle Q key to quit the application."""
        self.exit()
    
    def key_escape(self) -> None:
        """Handle ESC key globally to go back."""
        if len(self.screen_stack) > 1:
            self.pop_screen()
        else:
            # If we're on the main screen, quit
            self.exit()
