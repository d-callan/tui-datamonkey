# Datamonkey TUI Client

A modern terminal user interface (TUI) for interacting with the Datamonkey phylogenetic analysis service.

## Features

- 💬 **AI Chat Interface** - Interactive conversations with AI assistant
- 📊 **Dataset Management** - Upload and manage FASTA/NEXUS files
- 📈 **Visualization Browser** - View and explore Vega-Lite visualizations
- 🔗 **Vega Editor Integration** - Open visualizations in browser for interactive editing
- 🔐 **Session Management** - Automatic authentication and token handling

## Quick Start

```bash
# Generate API client from OpenAPI spec
make update

# Install dependencies
make install

# Configure API endpoint
cp .env.example .env
# Edit .env with your API URL

# Run the TUI
make run
```

## Development

```bash
# Development mode with hot reload
make dev

# Run tests
pytest

# Update API client after spec changes
make update
```

## Project Structure

```
tui-datamonkey/
├── src/datamonkey_tui/    # Main application code
│   ├── api/               # API client wrapper
│   ├── screens/           # TUI screens
│   ├── widgets/           # Custom widgets
│   ├── config/            # Configuration
│   └── utils/             # Utilities
├── generated/             # Auto-generated OpenAPI client
├── tests/                 # Test suite
└── docs/                  # Documentation
```

## Requirements

- Python 3.10+
- Node.js (for OpenAPI generator)
- Access to Datamonkey API

## Technology Stack

- **Textual** - Modern TUI framework
- **httpx** - Async HTTP client
- **Pydantic** - Data validation
- **OpenAPI Generator** - Auto-generated API client
