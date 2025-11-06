# Setup Guide

## Prerequisites

- Python 3.10+ (managed via conda)
- Node.js (for OpenAPI generator)
- Access to Datamonkey API

## Initial Setup

### 1. Create Conda Environment

```bash
# Create environment with Python 3.11
conda create -n datamonkey-tui python=3.11 -y

# Activate environment
conda activate datamonkey-tui
```

### 2. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

### 3. Generate API Client

```bash
# Pull OpenAPI spec and generate client
make update
```

This will:
- Download the latest OpenAPI spec from api-datamonkey
- Generate Python client code in `generated/`
- Install the generated client

### 4. Configure Environment

```bash
# Copy example config
cp .env.example .env

# Edit .env with your settings
# Set DATAMONKEY_API_URL to your API endpoint
```

### 5. Test Installation

```bash
# Run the TUI (basic welcome screen)
python -m datamonkey_tui

# Or use make
make run
```

## Development Workflow

### Activate Environment

```bash
conda activate datamonkey-tui
```

### Run in Development Mode

```bash
# Hot reload enabled
make dev
```

### Update API Client

When the OpenAPI spec changes:

```bash
make update
```

### Run Tests

```bash
# Run all tests
make test

# With coverage
make test-coverage
```

### Code Formatting

```bash
# Format code
make format

# Lint code
make lint
```

## Project Structure

```
tui-datamonkey/
├── src/datamonkey_tui/    # Main application
│   ├── api/               # API wrapper (custom code)
│   ├── screens/           # TUI screens
│   ├── widgets/           # Custom widgets
│   ├── config/            # Configuration
│   └── utils/             # Utilities
├── generated/             # Auto-generated API client (gitignored)
├── tests/                 # Test suite
└── docs/                  # Documentation
```

## Troubleshooting

### Python Version Error

If you see "requires a different Python" error:
```bash
# Check Python version
python --version

# Should be 3.10 or higher
# If not, recreate conda environment
conda deactivate
conda remove -n datamonkey-tui --all
conda create -n datamonkey-tui python=3.11 -y
conda activate datamonkey-tui
```

### OpenAPI Generator Errors

If `make update` fails:
```bash
# Ensure Node.js is installed
node --version

# If not installed, install Node.js
# Ubuntu/Debian:
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS:
brew install node
```

### Import Errors

If you get import errors after `make update`:
```bash
# Reinstall generated client
pip install -e ./generated
```

## Next Steps

1. Review [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for development roadmap
2. Check [CODEGEN_STRATEGY.md](CODEGEN_STRATEGY.md) for API client details
3. Read [VEGA_EDITOR_INTEGRATION.md](VEGA_EDITOR_INTEGRATION.md) for visualization features
4. Start implementing Phase 1 features!
