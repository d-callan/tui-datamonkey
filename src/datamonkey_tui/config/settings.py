"""Application settings and configuration."""

import logging
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """Application settings."""
    
    def __init__(self) -> None:
        self.api_url: str = os.getenv("DATAMONKEY_API_URL", "http://localhost:9300/api/v1")
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.config_dir: Path = Path(os.getenv("CONFIG_DIR", "~/.config/datamonkey")).expanduser()
        
        # Ensure config directory exists
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Configure logging
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """Set up logging configuration."""
        # Create logs directory
        logs_dir = self.config_dir / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        # Configure logging
        log_file = logs_dir / "datamonkey_tui.log"
        
        # Set up logger
        logger = logging.getLogger("datamonkey_tui")
        logger.setLevel(getattr(logging, self.log_level.upper(), logging.INFO))
        
        # Remove existing handlers to avoid duplicates
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, self.log_level.upper(), logging.INFO))
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)  # Only warnings and errors to console
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Store log file path for reference
        self._log_file = log_file
    
    @property
    def log_file(self) -> Path:
        """Path to the log file."""
        return getattr(self, '_log_file', self.config_dir / "logs" / "datamonkey_tui.log")
    
    @property
    def session_file(self) -> Path:
        """Path to session file."""
        return self.config_dir / "session.json"
    
    @property
    def config_file(self) -> Path:
        """Path to config file."""
        return self.config_dir / "config.json"


# Global settings instance
settings = Settings()
