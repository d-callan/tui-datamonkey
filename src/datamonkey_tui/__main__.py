"""Entry point for the Datamonkey TUI application."""

import sys
from .app import DatamonkeyApp


def main() -> int:
    """Run the Datamonkey TUI application."""
    app = DatamonkeyApp()
    return app.run()


if __name__ == "__main__":
    sys.exit(main())
