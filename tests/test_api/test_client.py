"""Test the API client wrapper."""

import pytest
from unittest.mock import Mock, AsyncMock, patch

from datamonkey_tui.api.client import DatamonkeyClient
from datamonkey_tui.config.session import session_manager


class TestDatamonkeyClient:
    """Test the DatamonkeyClient wrapper."""
    
    @pytest.fixture
    def client(self):
        """Create a test client instance."""
        return DatamonkeyClient("http://test.example.com")
    
    def test_init(self, client):
        """Test client initialization."""
        assert client is not None
        assert client.api_client.configuration.host == "http://test.example.com"
        assert client.chat is not None
        assert client.datasets is not None
        assert client.visualizations is not None
    
    def test_get_headers_with_token(self, client):
        """Test header generation with token."""
        # Mock session manager
        client.session_manager.get_token = Mock(return_value="test-token")
        
        headers = client._get_headers()
        assert headers == {"user_token": "test-token"}
    
    def test_get_headers_without_token(self, client):
        """Test header generation without token."""
        # Mock session manager
        client.session_manager.get_token = Mock(return_value=None)
        
        headers = client._get_headers()
        assert headers == {}
    
    @pytest.mark.asyncio
    async def test_list_conversations(self, client):
        """Test listing conversations."""
        # Mock the generated API (needs to be async)
        mock_response = Mock()
        client.chat.list_user_conversations = AsyncMock(return_value=mock_response)
        
        # Mock session manager
        client.session_manager.get_token = Mock(return_value="test-token")
        
        # Call the method
        result = await client.list_conversations()
        
        # Verify the call
        client.chat.list_user_conversations.assert_called_once_with(user_token="test-token")
        assert result == mock_response
