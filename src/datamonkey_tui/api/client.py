"""Main API client wrapper with session management."""

import logging
import os
from typing import Optional

import aiofiles

try:
    from openapi_client import ApiClient, Configuration
    from openapi_client.api import ChatApi, FileUploadAndQCApi, VisualizationsApi
    from openapi_client.models.dataset_meta import DatasetMeta
except ModuleNotFoundError as import_error:  # pragma: no cover - fallback only
    import sys
    from pathlib import Path

    fallback_root = Path(__file__).resolve().parent.parent.parent / "generated"
    candidate = fallback_root / "openapi_client"

    if candidate.exists():
        logging.getLogger("datamonkey_tui.api").debug(
            "Falling back to bundled generated client at %s", candidate
        )
        sys.path.insert(0, str(fallback_root))
        from openapi_client import ApiClient, Configuration  # type: ignore  # noqa
        from openapi_client.api import (  # type: ignore  # noqa
            ChatApi,
            FileUploadAndQCApi,
            VisualizationsApi,
        )
        from openapi_client.models.dataset_meta import DatasetMeta  # type: ignore  # noqa
    else:
        # Provide helpful error message
        raise ModuleNotFoundError(
            f"openapi_client module not found. Please run 'make update' to generate the API client, "
            f"or install it with 'pip install -e ./generated' if the generated/ directory exists. "
            f"Looked for bundled client at: {candidate}"
        ) from import_error

from ..config.session import session_manager

logger = logging.getLogger("datamonkey_tui.api")


class DatamonkeyClient:
    """Wrapper around generated OpenAPI client with session management."""
    
    def __init__(self, base_url: Optional[str] = None, on_token_extracted=None):
        """Initialize the API client.
        
        Args:
            base_url: API base URL. If None, uses settings.
            on_token_extracted: Callback function called when a new token is extracted
        """
        from ..config.settings import settings
        
        logger.info(f"Initializing API client with base URL: {base_url or settings.api_url}")
        
        # Configure generated client
        config = Configuration(host=base_url or settings.api_url)
        self.api_client = ApiClient(configuration=config)
        
        # Initialize API instances
        self.chat = ChatApi(self.api_client)
        self.datasets = FileUploadAndQCApi(self.api_client)
        self.visualizations = VisualizationsApi(self.api_client)
        
        self.session_manager = session_manager
        self.on_token_extracted = on_token_extracted
        logger.debug("API client initialized successfully")
    
    def _get_headers(self) -> dict:
        """Get headers with user token."""
        token = self.session_manager.get_token()
        if token:
            return {"user_token": token}
        return {}
    
    def _extract_and_save_token(self, response) -> None:
        """Extract token from response headers and save it."""
        header_source = None

        if hasattr(response, "raw_headers") and response.raw_headers:
            header_source = response.raw_headers
        elif hasattr(response, "headers") and response.headers:
            header_source = response.headers

        if header_source:
            # Normalize header keys for case-insensitive lookup
            try:
                header_items = header_source.items()
            except AttributeError:
                header_items = list(header_source)

            headers = {key.lower(): value for key, value in header_items}
            logger.info(f"Response headers from API call: {headers}")

            token_headers = ['x-session-token', 'user_token', 'x-user-token', 'authorization', 'x-auth-token']
            
            for header_name in token_headers:
                if header_name in headers:
                    token = headers[header_name]
                    if token and token != session_manager.get_token():
                        logger.info(f"Extracted new token from {header_name} header")
                        session_manager.set_token(token)
                        
                        # Call callback if provided
                        if self.on_token_extracted:
                            self.on_token_extracted()
                        
                        break
    
    async def list_conversations(self):
        """List user conversations - requires existing token."""
        logger.info("Fetching user conversations")
        token = session_manager.get_token()
        if not token:
            logger.warning("No token available for listing conversations")
            raise ValueError("Authentication required. Please create a conversation or upload a dataset first.")
        
        try:
            # Use headers for token as per OpenAPI spec
            headers = {"user_token": token}
            result = await self.chat.list_user_conversations(
                user_token=token,
                _headers=headers
            )
            logger.debug(f"Retrieved {len(result.conversations) if hasattr(result, 'conversations') else 0} conversations")
            return result
        except Exception as e:
            logger.error(f"Failed to fetch conversations: {e}")
            raise
    
    async def create_conversation(self, title: Optional[str] = None):
        """Create a new conversation - can generate new token."""
        logger.info("Creating new conversation")
        token = session_manager.get_token()
        
        # Use headers for token as per OpenAPI spec
        headers = {}
        if token:
            headers["user_token"] = token
        
        # Prepare request body
        body = None
        if title:
            body = {"title": title}
        
        try:
            logger.debug(f"Calling create_conversation with token in header: {token is not None}")
            logger.debug(f"Request headers: {headers}")
            logger.debug(f"Request body: {body}")
            
            result = await self.chat.create_conversation_with_http_info(
                user_token=token if token else None,
                _headers=headers,
                create_conversation_request=body
            )
            
            logger.debug(f"Response received: {result}")
            self._extract_and_save_token(result)
            logger.info("Conversation created successfully")
            return result.data
        except Exception as e:
            logger.error(f"Failed to create conversation: {e}")
            # Let's also log the API URL for debugging
            from ..config.settings import settings
            logger.error(f"API URL being used: {settings.api_url}")
            raise
    
    async def get_conversation(self, conversation_id: str):
        """Get a conversation by ID - requires existing token."""
        logger.info(f"Getting conversation {conversation_id}")
        token = session_manager.get_token()
        if not token:
            logger.warning("No token available for getting conversation")
            raise ValueError("Authentication required. Please create a conversation first.")
        
        try:
            # Use headers for token as per OpenAPI spec
            headers = {"user_token": token}
            result = await self.chat.get_conversation(
                conversation_id=conversation_id,
                user_token=token,
                _headers=headers
            )
            logger.debug("Conversation retrieved successfully")
            return result
        except Exception as e:
            logger.error(f"Failed to get conversation: {e}")
            raise
    
    async def send_message(self, conversation_id: str, message: str):
        """Send a message to a conversation - requires existing token."""
        logger.info(f"Sending message to conversation {conversation_id}")
        token = session_manager.get_token()
        if not token:
            logger.warning("No token available for sending message")
            raise ValueError("Authentication required. Please create a conversation first.")
        
        try:
            # Use headers for token as per OpenAPI spec
            headers = {"user_token": token}
            body = {"message": message}
            
            result = await self.chat.send_conversation_message(
                conversation_id=conversation_id,
                user_token=token,
                _headers=headers,
                send_conversation_message_request=body
            )
            logger.info("Message sent successfully")
            return result
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            raise
    
    async def get_messages(self, conversation_id: str):
        """Get messages from a conversation - requires existing token."""
        logger.info(f"Getting messages for conversation {conversation_id}")
        token = session_manager.get_token()
        if not token:
            logger.warning("No token available for getting messages")
            raise ValueError("Authentication required. Please create a conversation first.")
        
        try:
            # Use headers for token as per OpenAPI spec
            headers = {"user_token": token}
            result = await self.chat.get_conversation_messages(
                conversation_id=conversation_id,
                user_token=token,
                _headers=headers
            )
            logger.debug(f"Retrieved {len(result.messages) if hasattr(result, 'messages') else 0} messages")
            return result
        except Exception as e:
            logger.error(f"Failed to get messages: {e}")
            raise
    
    async def list_datasets(self):
        """List user datasets - requires existing token."""
        logger.info("Fetching user datasets")
        token = session_manager.get_token()
        if not token:
            logger.warning("No token available for listing datasets")
            raise ValueError("Authentication required. Please upload a dataset first.")
        
        try:
            # Use headers for token as per OpenAPI spec
            headers = {"user_token": token}
            result = await self.datasets.get_datasets_list(
                user_token=token,
                _headers=headers
            )
            dataset_count = len(result.datasets) if hasattr(result, 'datasets') and result.datasets else 0
            logger.info(f"Retrieved {dataset_count} datasets")
            if dataset_count == 0:
                logger.warning("No datasets found for this user token")
            return result
        except Exception as e:
            logger.error(f"Failed to fetch datasets: {e}")
            raise
    
    async def upload_dataset(
        self,
        file_path: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        dataset_type: Optional[str] = "fasta",
    ):
        """Upload a dataset - reuses existing token or creates a new one."""
        expanded_path = os.path.expanduser(file_path)
        logger.info(f"Uploading dataset: {expanded_path}")

        if not os.path.isfile(expanded_path):
            raise FileNotFoundError(f"Dataset file not found: {expanded_path}")

        token = session_manager.get_token()

        headers = {}
        if token:
            headers["user_token"] = token

        meta_kwargs = {}
        if name:
            meta_kwargs["name"] = name
        if description:
            meta_kwargs["description"] = description
        if dataset_type:
            meta_kwargs["type"] = dataset_type

        meta = DatasetMeta(**meta_kwargs) if meta_kwargs else None

        async with aiofiles.open(expanded_path, "rb") as file_handle:
            file_bytes = await file_handle.read()

        file_tuple = (
            os.path.basename(expanded_path),
            file_bytes,
        )

        try:
            response = await self.datasets.post_dataset_with_http_info(
                user_token=token if token else None,
                user_token2=token if token else None,
                meta=meta,
                file=file_tuple,
                _headers=headers,
            )

            self._extract_and_save_token(response)
            logger.info("Dataset uploaded successfully")
            return response.data
        except Exception as e:
            logger.error(f"Failed to upload dataset: {e}")
            raise

    async def delete_dataset(self, dataset_id: str) -> None:
        """Delete a dataset owned by the authenticated user."""
        logger.info(f"Deleting dataset: {dataset_id}")
        token = session_manager.get_token()
        if not token:
            raise ValueError("Authentication required. Please upload a dataset first.")

        headers = {"user_token": token}

        try:
            await self.datasets.delete_dataset(
                dataset_id=dataset_id,
                user_token=token,
                _headers=headers,
            )
            logger.info("Dataset deleted successfully")
        except Exception as e:
            logger.error(f"Failed to delete dataset: {e}")
            raise
    
    async def list_visualizations(self, job_id: Optional[str] = None, dataset_id: Optional[str] = None):
        """List visualizations - requires existing token."""
        logger.info("Fetching visualizations")
        token = session_manager.get_token()
        if not token:
            logger.warning("No token available for listing visualizations")
            raise ValueError("Authentication required. Please create a job or visualization first.")
        
        # Use headers for token as per OpenAPI spec
        headers = {"user_token": token}
        params = {}
        if job_id:
            params["job_id"] = job_id
        if dataset_id:
            params["dataset_id"] = dataset_id
        
        try:
            result = await self.visualizations.get_visualizations_list(
                user_token=token,
                _headers=headers,
                **params,
            )
            viz_count = len(result.visualizations) if hasattr(result, 'visualizations') and result.visualizations else 0
            logger.info(f"Retrieved {viz_count} visualizations")
            if viz_count == 0:
                logger.warning("No visualizations found for this user token")
            return result
        except Exception as e:
            logger.error(f"Failed to fetch visualizations: {e}")
            raise
    
    async def create_visualization(self, job_id: str, spec: dict):
        """Create a visualization - can generate new token."""
        logger.info(f"Creating visualization for job {job_id}")
        token = session_manager.get_token()
        
        # Use headers for token as per OpenAPI spec
        headers = {}
        if token:
            headers["user_token"] = token
        
        try:
            result = await self.visualizations.create_visualization(
                job_id=job_id,
                visualization_spec=spec,
                _headers=headers
            )
            self._extract_and_save_token(result)
            logger.info("Visualization created successfully")
            return result
        except Exception as e:
            logger.error(f"Failed to create visualization: {e}")
            raise

    async def delete_visualization(self, viz_id: str) -> None:
        """Delete a visualization owned by the authenticated user."""
        logger.info(f"Deleting visualization: {viz_id}")
        token = session_manager.get_token()
        if not token:
            raise ValueError("Authentication required. Please create a visualization first.")

        headers = {"user_token": token}

        try:
            await self.visualizations.delete_visualization(
                viz_id=viz_id,
                user_token=token,
                _headers=headers,
            )
            logger.info("Visualization deleted successfully")
        except Exception as e:
            logger.error(f"Failed to delete visualization: {e}")
            raise
