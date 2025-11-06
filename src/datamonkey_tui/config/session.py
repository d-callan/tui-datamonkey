"""Session management for Datamonkey API."""

import json
from datetime import datetime
from typing import Optional

from .settings import settings


class SessionManager:
    """Manages user session tokens."""
    
    def __init__(self) -> None:
        self._token: Optional[str] = None
    
    def get_token(self) -> Optional[str]:
        """Get current session token."""
        if self._token:
            return self._token
        
        # Try to load from file
        try:
            with open(settings.session_file, "r") as f:
                data = json.load(f)
                self._token = data.get("token")
                return self._token
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return None
    
    def set_token(self, token: str) -> None:
        """Set and save session token."""
        self._token = token
        
        # Save to file
        session_data = {
            "token": token,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "last_used": datetime.utcnow().isoformat() + "Z"
        }
        
        with open(settings.session_file, "w") as f:
            json.dump(session_data, f, indent=2)
    
    def clear_token(self) -> None:
        """Clear session token."""
        self._token = None
        
        # Remove session file
        try:
            settings.session_file.unlink()
        except FileNotFoundError:
            pass
    
    def update_last_used(self) -> None:
        """Update the last used timestamp."""
        if not self._token:
            return
        
        try:
            with open(settings.session_file, "r") as f:
                data = json.load(f)
            
            data["last_used"] = datetime.utcnow().isoformat() + "Z"
            
            with open(settings.session_file, "w") as f:
                json.dump(data, f, indent=2)
        except (FileNotFoundError, json.JSONDecodeError):
            pass


# Global session manager instance
session_manager = SessionManager()
