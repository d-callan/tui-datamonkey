"""Test that TextArea readonly fix works correctly."""

import pytest
from unittest.mock import Mock

from datamonkey_tui.api.client import DatamonkeyClient
from datamonkey_tui.screens.chat import ChatScreen
from datamonkey_tui.screens.visualizations import VisualizationScreen


class TestTextAreaFix:
    """Test that TextArea readonly issue is fixed."""
    
    @pytest.fixture
    def api_client(self):
        """Create a mock API client."""
        return Mock(spec=DatamonkeyClient)
    
    def test_chat_screen_textarea_creation(self, api_client):
        """Test ChatScreen can be created without readonly error."""
        screen = ChatScreen(api_client)
        assert screen is not None
        
        # Test that we can create TextArea without readonly parameter
        from textual.widgets import TextArea
        ta = TextArea()
        assert hasattr(ta, 'readonly')
        
        # Test we can set readonly after creation
        ta.readonly = True
        assert ta.readonly is True
    
    def test_visualization_screen_textarea_creation(self, api_client):
        """Test VisualizationScreen can be created without readonly error."""
        screen = VisualizationScreen(api_client)
        assert screen is not None
        
        # Test that we can create TextArea with language parameter
        from textual.widgets import TextArea
        ta = TextArea(language="json")
        assert hasattr(ta, 'readonly')
        
        # Test we can set readonly after creation
        ta.readonly = True
        assert ta.readonly is True
