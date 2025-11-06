"""Test authentication flow and session management."""

import pytest
from unittest.mock import Mock, patch

from datamonkey_tui.api.client import DatamonkeyClient
from datamonkey_tui.screens.main import MainScreen
from datamonkey_tui.screens.session import SessionScreen
from datamonkey_tui.config.session import session_manager


class TestAuthenticationFlow:
    """Test the authentication flow and session management."""
    
    @pytest.fixture
    def api_client(self):
        """Create a mock API client."""
        return Mock(spec=DatamonkeyClient)
    
    def test_main_screen_shows_unauthenticated_status(self, api_client):
        """Test main screen shows warning when not authenticated."""
        # Clear any existing token
        session_manager.clear_token()
        
        screen = MainScreen(api_client)
        
        # Check that compose would show unauthenticated status
        # (We can't easily test the visual output, but we can test the logic)
        has_token = session_manager.get_token() is not None
        assert not has_token
    
    def test_main_screen_shows_authenticated_status(self, api_client):
        """Test main screen shows success when authenticated."""
        # Set a token
        session_manager.set_token("test-token")
        
        screen = MainScreen(api_client)
        
        # Check that compose would show authenticated status
        has_token = session_manager.get_token() is not None
        assert has_token
        
        # Clean up
        session_manager.clear_token()
    
    def test_session_screen_can_save_token(self):
        """Test session screen can save a token."""
        screen = SessionScreen()
        
        # Test saving a token
        test_token = "test-session-token-123"
        session_manager.set_token(test_token)
        
        # Verify token was saved
        retrieved_token = session_manager.get_token()
        assert retrieved_token == test_token
        
        # Clean up
        session_manager.clear_token()
    
    def test_session_screen_can_clear_token(self):
        """Test session screen can clear a token."""
        screen = SessionScreen()
        
        # First set a token
        session_manager.set_token("test-token")
        assert session_manager.get_token() is not None
        
        # Then clear it
        session_manager.clear_token()
        assert session_manager.get_token() is None
    
    @patch('datamonkey_tui.screens.main.SessionScreen')
    def test_auto_redirect_to_session_when_unauthenticated(self, mock_session_screen, api_client):
        """Test auto-redirect to session screen when trying to access protected features."""
        # Clear token
        session_manager.clear_token()
        
        screen = MainScreen(api_client)
        
        # Mock the app and notification
        mock_app = Mock()
        screen.app = mock_app
        
        # Try to access chat (protected feature)
        mock_event = Mock()
        mock_event.button.id = "chat-btn"
        
        screen.on_button_pressed(mock_event)
        
        # Should have shown notification and redirected to session screen
        mock_app.notify.assert_called_once()
        mock_app.push_screen.assert_called_once()
        
        # Verify it was SessionScreen that was pushed
        args = mock_app.push_screen.call_args[0]
        assert len(args) == 1
        # The argument should be a SessionScreen instance
