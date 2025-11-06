"""Test that all screens can be imported successfully."""

import pytest
from unittest.mock import Mock

from datamonkey_tui.api.client import DatamonkeyClient
from datamonkey_tui.screens.main import MainScreen
from datamonkey_tui.screens.chat import ChatScreen
from datamonkey_tui.screens.datasets import DatasetScreen
from datamonkey_tui.screens.visualizations import VisualizationScreen


class TestScreenImports:
    """Test that all screens can be imported and initialized."""
    
    @pytest.fixture
    def api_client(self):
        """Create a mock API client."""
        return Mock(spec=DatamonkeyClient)
    
    def test_main_screen_init(self, api_client):
        """Test MainScreen initialization."""
        screen = MainScreen(api_client)
        assert screen is not None
        assert screen.api_client == api_client
    
    def test_chat_screen_init(self, api_client):
        """Test ChatScreen initialization."""
        screen = ChatScreen(api_client)
        assert screen is not None
        assert screen.api_client == api_client
        assert screen.current_conversation_id is None
    
    def test_dataset_screen_init(self, api_client):
        """Test DatasetScreen initialization."""
        screen = DatasetScreen(api_client)
        assert screen is not None
        assert screen.api_client == api_client
        assert screen.datasets == []
    
    def test_visualization_screen_init(self, api_client):
        """Test VisualizationScreen initialization."""
        screen = VisualizationScreen(api_client)
        assert screen is not None
        assert screen.api_client == api_client
        assert screen.visualizations == []
        assert screen.current_viz is None
