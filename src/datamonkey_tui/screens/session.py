"""Session management screen for setting API token."""

import logging
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Input, Button, Label
from textual.binding import Binding

from ..config.session import session_manager
from ..config.settings import settings

logger = logging.getLogger("datamonkey_tui.session")


class SessionScreen(Screen):
    """Screen for managing user session and API token."""
    
    BINDINGS = [
        Binding("escape", "pop_screen", "Back"),
        Binding("enter", "save_token", "Save Token"),
        Binding("c", "clear_token", "Clear Token"),
    ]
    
    CSS = """
    SessionScreen {
        align: center middle;
    }
    
    .session-container {
        width: 80;
        height: auto;
        padding: 2;
        border: solid $primary;
        background: $surface;
    }
    
    .title {
        text-style: bold;
        color: $primary;
        text-align: center;
        margin: 0 0 1 0;
    }
    
    .info {
        color: $text-muted;
        margin: 0 0 2 0;
        text-align: center;
    }
    
    .step {
        color: $text;
        margin: 0 0 0 2;
        text-align: left;
    }
    
    .token-input {
        width: 100%;
        margin: 1 0;
        border: solid $primary;
    }
    
    .button-container {
        width: 100%;
        margin: 2 0;
    }
    
    .action-button {
        width: 1fr;
        margin: 0 1;
        background: $primary;
    }
    
    .status {
        text-align: center;
        color: $accent;
        margin: 1 0;
    }
    
    .url-display {
        background: $surface;
        border: solid $panel;
        padding: 1;
        margin: 1 0;
        text-align: center;
        color: $text-muted;
    }
    """
    
    def compose(self) -> ComposeResult:
        """Create the session screen layout."""
        with Vertical(classes="session-container"):
            yield Static("🔐 Session Management", classes="title")
            yield Static("Manage your Datamonkey authentication token", classes="info")
            
            yield Static("API URL:", classes="info")
            yield Static(settings.api_url, classes="url-display")
            
            # Updated instructions for the new flow
            yield Static("How authentication works:", classes="info")
            yield Static("📤 Upload a dataset OR 💬 Create a conversation", classes="step")
            yield Static("🔑 Token is automatically generated and saved", classes="step")
            yield Static("✅ Use all features with your authenticated session", classes="step")
            yield Static("", classes="info")
            yield Static("Or manually set a token if you already have one:", classes="info")
            
            yield Label("API Token:")
            yield Input(
                placeholder="Paste existing API token here...",
                password=True,
                id="token-input",
                classes="token-input"
            )
            
            with Horizontal(classes="button-container"):
                yield Button("💾 Save Token", id="save-btn", classes="action-button")
                yield Button("🗑️ Clear Token", id="clear-btn", classes="action-button")
                yield Button("❌ Cancel", id="cancel-btn", classes="action-button")
            
            yield Static("", id="status-message", classes="status")
        
        yield Footer()
    
    def key_esc(self) -> None:
        """Handle ESC key to go back to main screen."""
        self.app.pop_screen()
    
    def on_mount(self) -> None:
        """Initialize the screen when mounted."""
        # Check if token is already set
        token = session_manager.get_token()
        if token:
            token_input = self.query_one("#token-input", Input)
            token_input.value = token
            self.update_status("Token already loaded - you can update or clear it", "info")
        else:
            self.update_status("No token set - create a conversation or upload dataset to get one automatically", "info")
    
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "save-btn":
            await self.action_save_token()
        elif event.button.id == "clear-btn":
            await self.action_clear_token()
        elif event.button.id == "cancel-btn":
            self.app.pop_screen()
    
    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission."""
        if event.input.id == "token-input":
            await self.action_save_token()
    
    async def action_save_token(self) -> None:
        """Save the API token."""
        token_input = self.query_one("#token-input", Input)
        token = token_input.value.strip()
        
        if not token:
            self.update_status("Please enter a token", "error")
            return
        
        try:
            session_manager.set_token(token)
            logger.info("Session token saved successfully")
            self.update_status("Token saved successfully! You can now access all features.", "success")
            
            # Wait a moment then return to main screen
            self.set_timer(2.0, self.return_to_main)
            
        except Exception as e:
            logger.error(f"Failed to save token: {e}")
            self.update_status(f"Failed to save token: {e}", "error")
    
    def return_to_main(self) -> None:
        """Return to main screen and refresh it."""
        # Pop back to main screen
        self.app.pop_screen()
        
        # Refresh main screen to show updated authentication status
        if hasattr(self.app.screen_stack[-1], 'refresh_session_status'):
            self.app.screen_stack[-1].refresh_session_status()
    
    async def action_clear_token(self) -> None:
        """Clear the API token."""
        try:
            session_manager.clear_token()
            logger.info("Session token cleared")
            token_input = self.query_one("#token-input", Input)
            token_input.value = ""
            self.update_status("Token cleared - you'll need to create a conversation or upload dataset to get a new one", "info")
            
            # Refresh main screen if it exists
            if len(self.app.screen_stack) > 1 and hasattr(self.app.screen_stack[-2], 'refresh_session_status'):
                self.app.screen_stack[-2].refresh_session_status()
            
        except Exception as e:
            logger.error(f"Failed to clear token: {e}")
            self.update_status(f"Failed to clear token: {e}", "error")
    
    def update_status(self, message: str, status_type: str = "info") -> None:
        """Update the status message."""
        status_widget = self.query_one("#status-message", Static)
        
        # Add color based on status type
        if status_type == "success":
            message = f"[green]{message}[/]"
        elif status_type == "error":
            message = f"[red]{message}[/]"
        else:
            message = f"[dim]{message}[/]"
        
        status_widget.update(message)
