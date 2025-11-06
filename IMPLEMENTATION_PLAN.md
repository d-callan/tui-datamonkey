# Datamonkey TUI Client - Implementation Plan

## Overview
A terminal user interface (TUI) client for interacting with the Datamonkey service API. Built with Python Textual for a modern, responsive terminal experience.

## Technology Stack

### Code Generation: OpenAPI Generator

**Strategy:** Auto-generate API client from OpenAPI spec (same approach as service-datamonkey)

**Generator Options:**

1. **openapi-generator-cli (Python client)** ⭐ RECOMMENDED
   - Same tool service-datamonkey uses (for Go server)
   - Supports Python client generation
   - Generates typed models with Pydantic
   - Async support with httpx
   - Command: `npx @openapitools/openapi-generator-cli generate -i openapi.yaml -g python -o ./generated`

2. **openapi-python-client**
   - Modern, actively maintained
   - Generates clean, typed code with attrs/pydantic
   - Built-in httpx async support
   - Command: `openapi-python-client generate --url https://raw.githubusercontent.com/d-callan/api-datamonkey/refs/heads/master/dist/openapi.yaml`

3. **datamodel-code-generator** (models only)
   - Only generates Pydantic models, not client
   - Would still need to write HTTP client manually
   - Less suitable for our needs

**Decision:** Use **openapi-generator-cli** for consistency with service-datamonkey workflow.

**Integration:**
- `make update` target pulls spec and regenerates client
- Generated code in `generated/` directory (gitignored)
- Thin wrapper layer in `src/datamonkey_tui/api/` for TUI-specific logic
- `.openapi-generator-ignore` to preserve custom code

### Primary: Python Textual
**Pros:**
- Modern, reactive framework with excellent async support
- Rich widget library (DataTable, Tree, Input, TextArea, etc.)
- Built-in CSS-like styling system
- Active development and great documentation
- Hot reload during development
- Excellent for complex layouts and real-time updates

**Alternatives Considered:**
- **Rich** - Great for simple output, but not interactive
- **urwid** - Mature but older API, steeper learning curve
- **py-cui** - Simpler but less feature-rich
- **prompt_toolkit** - Excellent for prompts/forms, less suited for full TUI apps

**Decision:** Textual is the best fit for a chat-focused, multi-panel interface with real-time updates.

## Core Features

### 1. Authentication & Session Management
- **Session Token Handling**
  - Store token in `~/.config/datamonkey/session.json`
  - Auto-create session on first use (via POST /chat or POST /datasets)
  - Display session info in status bar
  - Command to clear/reset session

### 2. Chat Interface (Primary Feature)
- **Conversation Management**
  - List all conversations (GET /chat)
  - Create new conversation (POST /chat)
  - Switch between conversations
  - Delete conversations (DELETE /chat/{conversationId})
  
- **Message Interface**
  - Split-pane layout: conversation list (left) + messages (right)
  - Send messages (POST /chat/{conversationId}/messages)
  - Display message history (GET /chat/{conversationId}/messages)
  - Real-time message streaming (if supported)
  - Markdown rendering for AI responses
  - Syntax highlighting for code blocks
  
- **Chat Features**
  - Message input with multi-line support
  - Conversation search/filter
  - Export conversation to file
  - Copy messages to clipboard

### 3. Dataset Management
- **Upload Interface**
  - File picker for dataset selection
  - Support for FASTA/NEXUS formats
  - Upload progress indicator
  - POST /datasets with multipart/form-data
  
- **Dataset List**
  - View all user datasets (GET /datasets)
  - Display dataset metadata (name, format, upload date)
  - Delete datasets
  - Filter/search datasets

### 4. Visualization Retrieval
- **Visualization Browser**
  - List visualizations (GET /visualizations)
  - Filter by job_id or dataset_id
  - Display Vega-Lite specs
  - Export visualizations to JSON
  - Preview visualization metadata
  - **Open in Vega Editor** - Generate URLs to pre-populated Vega Editor
    - Format: `https://vega.github.io/editor/#/url/vega-lite/{base64_spec}`
    - Users can interactively explore and modify visualizations
    - Copy shareable editor links

### 5. UI Layout

**Main Chat Screen:**
```
┌─────────────────────────────────────────────────────────────────┐
│ Datamonkey TUI                        Session: abc123...   [F1] │
├─────────────────┬───────────────────────────────────────────────┤
│ Conversations   │ Chat: "Analysis Discussion"                   │
│                 │                                                │
│ > New Analysis  │ User: Can you analyze my dataset?             │
│   Debug Session │                                                │
│   Test Run      │ AI: I'd be happy to help! Let me check...     │
│                 │                                                │
│                 │ [Tool Call: listDatasets]                     │
│                 │ Found 3 datasets...                            │
│                 │                                                │
│ [Datasets]      │                                                │
│ [Visualizations]│                                                │
│ [Settings]      │                                                │
│                 │                                                │
│                 ├────────────────────────────────────────────────┤
│                 │ > Type your message...                         │
└─────────────────┴───────────────────────────────────────────────┘
│ Ctrl+C: Quit | Tab: Switch Panel | Enter: Send | F1: Help       │
└─────────────────────────────────────────────────────────────────┘
```

**Visualization Browser Screen:**
```
┌─────────────────────────────────────────────────────────────────┐
│ Visualizations                        Filter: [Job ID] [Dataset]│
├─────────────────────────────────────────────────────────────────┤
│ ID          │ Type      │ Job ID    │ Dataset   │ Created       │
│ viz_abc123  │ Tree Plot │ job_001   │ ds_xyz    │ 2024-11-05    │
│ viz_def456  │ Bar Chart │ job_002   │ ds_xyz    │ 2024-11-04    │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Selected: viz_abc123 - Tree Plot                                │
│                                                                  │
│ {                                                                │
│   "$schema": "https://vega.github.io/schema/vega-lite/v5.json",│
│   "mark": "bar",                                                │
│   "data": {...}                                                  │
│ }                                                                │
│                                                                  │
│ [E] Export JSON  [C] Copy Spec  [V] Open in Vega Editor         │
└─────────────────────────────────────────────────────────────────┘
│ Vega Editor: https://vega.github.io/editor/#/url/vega-lite/...  │
└─────────────────────────────────────────────────────────────────┘
```

## Project Structure

```
tui-datamonkey/
├── README.md
├── IMPLEMENTATION_PLAN.md
├── Makefile                    # Build targets (update, install, run)
├── pyproject.toml              # Poetry/uv project config
├── requirements.txt            # Pip dependencies
├── openapitools.json           # OpenAPI generator config
├── .openapi-generator-ignore   # Files to preserve during regen
├── .gitignore
├── .env.example
├── openapi.yaml                # Downloaded spec (gitignored)
│
├── generated/                  # Auto-generated API client (gitignored)
│   ├── openapi_client/
│   │   ├── api/
│   │   ├── models/
│   │   └── ...
│   └── README.md
│
├── src/
│   └── datamonkey_tui/
│       ├── __init__.py
│       ├── __main__.py         # Entry point
│       ├── app.py              # Main Textual app
│       │
│       ├── api/                # Thin wrapper over generated client
│       │   ├── __init__.py
│       │   ├── client.py       # Wrapper with session management
│       │   ├── chat.py         # Chat-specific helpers
│       │   ├── datasets.py     # Dataset upload helpers
│       │   └── visualizations.py
│       │
│       ├── screens/            # Textual screens
│       │   ├── __init__.py
│       │   ├── main.py         # Main chat screen
│       │   ├── datasets.py     # Dataset management screen
│       │   ├── visualizations.py
│       │   └── settings.py
│       │
│       ├── widgets/            # Custom widgets
│       │   ├── __init__.py
│       │   ├── conversation_list.py
│       │   ├── message_view.py
│       │   ├── message_input.py
│       │   └── dataset_table.py
│       │
│       ├── config/             # Configuration
│       │   ├── __init__.py
│       │   ├── settings.py     # App settings
│       │   └── session.py      # Session management
│       │
│       └── utils/              # Utilities
│           ├── __init__.py
│           ├── markdown.py     # Markdown rendering
│           ├── file_picker.py  # File selection
│           └── vega_editor.py  # Vega Editor URL generation
│
└── tests/
    ├── __init__.py
    ├── test_api/
    ├── test_models/
    └── test_widgets/
```

## Implementation Phases

### Phase 1: Foundation (Days 1-2)
**Goal:** Basic project setup and API client

- [ ] Initialize Python project with Poetry/uv
- [ ] Set up dependencies (textual, httpx, pydantic)
- [ ] Create basic project structure
- [ ] Set up OpenAPI code generation
  - Create `Makefile` with `update` target
  - Create `openapitools.json` config
  - Create `.openapi-generator-ignore`
  - Run `make update` to generate initial client
- [ ] Create API wrapper layer
  - Wrap generated client with session management
  - Token injection into requests
  - Error handling and retries
- [ ] Implement session management
  - Load/save token from config file
  - Auto-create session if missing
- [ ] Basic Textual app skeleton
- [ ] Configuration management (.env, config files)

**Deliverable:** Can make authenticated API calls using generated client, store session token

### Phase 2: Chat Interface - Core (Days 3-5)
**Goal:** Basic chat functionality working

- [ ] Use generated API client for chat endpoints
  - ChatApi methods already generated
  - Models (ChatConversation, ChatMessage) already generated
  - Create thin wrapper for TUI-specific logic
- [ ] Build main chat screen layout
  - Conversation list widget (left panel)
  - Message view widget (right panel)
  - Message input widget (bottom)
- [ ] Basic message display
  - User vs AI message styling
  - Timestamps
  - Scrolling
- [ ] Send/receive messages
- [ ] Conversation switching

**Deliverable:** Can chat with AI in TUI

### Phase 3: Chat Interface - Polish (Days 6-7)
**Goal:** Enhanced chat experience

- [ ] Markdown rendering for AI responses
  - Code blocks with syntax highlighting
  - Lists, headers, emphasis
- [ ] Display tool calls in messages
  - Collapsible tool call sections
  - Tool call results
- [ ] Message actions
  - Copy message
  - Export conversation
- [ ] Conversation management
  - Create new conversation with title
  - Delete conversation
  - Rename conversation
- [ ] Search/filter conversations
- [ ] Loading indicators for API calls
- [ ] Error handling and user feedback

**Deliverable:** Polished chat experience with all features

### Phase 4: Dataset Management (Days 8-9)
**Goal:** Upload and manage datasets

- [ ] Use generated API client for dataset endpoints
  - FileUploadAndQcApi methods already generated
  - Handle multipart/form-data upload
- [ ] Create dataset screen
  - Dataset table widget
  - Upload dialog
  - File picker
- [ ] Dataset upload flow
  - File selection
  - Progress indicator
  - Success/error feedback
- [ ] Dataset list features
  - Sort by date/name
  - Filter datasets
  - View dataset details
  - Delete datasets

**Deliverable:** Can upload and manage datasets from TUI

### Phase 5: Visualization Browser (Days 10-11)
**Goal:** View and export visualizations

- [ ] Use generated API client for visualization endpoints
  - VisualizationsApi methods already generated
- [ ] Create visualization screen
  - Visualization list/table
  - Filter controls
  - Detail view
- [ ] Visualization features
  - Display Vega-Lite spec (formatted JSON)
  - Export to file
  - Copy to clipboard
  - Link to associated job/dataset
  - **Generate Vega Editor URL**
    - Base64 encode spec
    - Create editor URL with spec
    - Open in browser or copy link
    - Allow users to interactively explore/modify viz

**Deliverable:** Can browse and export visualizations

### Phase 6: Polish & Testing (Days 12-14)
**Goal:** Production-ready TUI

- [ ] Keyboard shortcuts
  - Document all shortcuts
  - Help screen (F1)
  - Vim-style navigation (optional)
- [ ] Settings screen
  - API endpoint configuration
  - Theme selection
  - Behavior preferences
- [ ] Error handling improvements
  - Network errors
  - API errors
  - User-friendly messages
- [ ] Performance optimization
  - Lazy loading for large lists
  - Message pagination
- [ ] Testing
  - Unit tests for API client
  - Widget tests
  - Integration tests
- [ ] Documentation
  - README with installation
  - Usage guide
  - Screenshots/GIFs
  - API endpoint documentation

**Deliverable:** Production-ready TUI client

## Dependencies

### Core
- **textual** (>=0.47.0) - TUI framework
- **httpx** (>=0.26.0) - Async HTTP client
- **pydantic** (>=2.5.0) - Data validation
- **python-dotenv** (>=1.0.0) - Environment variables

### Optional/Nice-to-have
- **rich** (included with textual) - Terminal formatting
- **pygments** (>=2.17.0) - Syntax highlighting
- **python-magic** (>=0.4.27) - File type detection
- **aiofiles** (>=23.2.0) - Async file operations
- **pytest** (>=7.4.0) - Testing
- **pytest-asyncio** (>=0.23.0) - Async test support
- **webbrowser** (stdlib) - Open URLs in browser

## Configuration

### Environment Variables
```bash
# .env
DATAMONKEY_API_URL=http://localhost:8080
DATAMONKEY_SESSION_TOKEN=  # Auto-populated
LOG_LEVEL=INFO
```

### Config File
```json
// ~/.config/datamonkey/config.json
{
  "api_url": "http://localhost:8080",
  "theme": "dark",
  "auto_save_conversations": true,
  "message_page_size": 50
}
```

### Session File
```json
// ~/.config/datamonkey/session.json
{
  "token": "abc123...",
  "created_at": "2024-11-05T22:00:00Z",
  "last_used": "2024-11-05T22:30:00Z"
}
```

## Vega Editor Integration

### URL Format
Vega Editor supports loading specs via URL:
```
https://vega.github.io/editor/#/url/vega-lite/{base64_encoded_spec}
```

### Implementation
```python
# src/datamonkey_tui/utils/vega_editor.py
import base64
import json
import webbrowser
from typing import Dict, Any

def generate_vega_editor_url(spec: Dict[str, Any]) -> str:
    """Generate Vega Editor URL with pre-loaded spec.
    
    Args:
        spec: Vega-Lite specification dictionary
        
    Returns:
        URL to Vega Editor with spec pre-loaded
    """
    # Serialize spec to JSON
    spec_json = json.dumps(spec, separators=(',', ':'))
    
    # Base64 encode (URL-safe)
    spec_b64 = base64.urlsafe_b64encode(spec_json.encode()).decode()
    
    # Construct editor URL
    return f"https://vega.github.io/editor/#/url/vega-lite/{spec_b64}"

def open_in_vega_editor(spec: Dict[str, Any]) -> str:
    """Open Vega-Lite spec in browser's Vega Editor.
    
    Args:
        spec: Vega-Lite specification dictionary
        
    Returns:
        The generated URL
    """
    url = generate_vega_editor_url(spec)
    webbrowser.open(url)
    return url
```

### Widget Integration
```python
# In visualization detail widget
class VisualizationDetail(Widget):
    def on_key(self, event: Key) -> None:
        if event.key == "v":  # Press 'V' to open in Vega Editor
            url = open_in_vega_editor(self.current_viz.spec)
            self.app.notify(f"Opened in browser: {url[:50]}...")
        elif event.key == "c":  # Press 'C' to copy URL
            url = generate_vega_editor_url(self.current_viz.spec)
            pyperclip.copy(url)
            self.app.notify("Vega Editor URL copied to clipboard!")
```

### Benefits
- **Interactive Exploration** - Users can modify visualizations in real-time
- **Shareable Links** - URLs can be shared with collaborators
- **No Local Rendering** - Avoid terminal rendering limitations
- **Full Vega Features** - Access to complete Vega Editor toolset
- **Export Options** - Vega Editor supports PNG, SVG, PDF export

### Example URLs
```
# Simple bar chart
https://vega.github.io/editor/#/url/vega-lite/eyIkc2NoZW1hIjoiaHR0cHM6Ly92ZWdhLmdpdGh1Yi5pby9zY2hlbWEvdmVnYS1saXRlL3Y1Lmpzb24iLCJtYXJrIjoiYmFyIiwiZGF0YSI6eyJ2YWx1ZXMiOlt7ImEiOiJBIiwiYiI6MjB9LHsiYSI6IkIiLCJiIjozMH1dfSwiZW5jb2RpbmciOnsieCI6eyJmaWVsZCI6ImEiLCJ0eXBlIjoibm9taW5hbCJ9LCJ5Ijp7ImZpZWxkIjoiYiIsInR5cGUiOiJxdWFudGl0YXRpdmUifX19

# User clicks link → Opens in browser with spec pre-loaded
# Can immediately edit, export, or share
```

## Key Technical Decisions

### 1. Async/Await Throughout
- Use `httpx.AsyncClient` for all API calls
- Textual is async-native
- Better performance for concurrent operations

### 2. Pydantic Models
- Type-safe data models
- Automatic validation
- Easy serialization/deserialization
- Matches OpenAPI schemas

### 3. Separation of Concerns
- API client layer isolated from UI
- Models independent of API/UI
- Screens compose widgets
- Easy to test each layer

### 4. Configuration Hierarchy
1. Environment variables (highest priority)
2. Config file (`~/.config/datamonkey/config.json`)
3. Defaults (lowest priority)

### 5. Error Handling Strategy
- Network errors: Retry with exponential backoff
- API errors: Display user-friendly messages
- Validation errors: Highlight in UI
- Graceful degradation when possible

## Testing Strategy

### Unit Tests
- API client methods (mocked responses)
- Data model validation
- Utility functions

### Integration Tests
- API client with real endpoints (test environment)
- Widget interactions
- Screen navigation

### Manual Testing
- Full user workflows
- Edge cases (network failures, large datasets)
- Performance testing

## Future Enhancements (Post-MVP)

### Phase 7+
- [ ] Job monitoring interface
  - List jobs
  - View job status
  - Cancel jobs
  - View job results
- [ ] Method execution interface
  - Select method (ABSREL, BGM, etc.)
  - Configure parameters
  - Submit jobs
- [ ] Streaming responses
  - Real-time AI message streaming
  - Progress updates for long-running operations
- [ ] Offline mode
  - Cache conversations locally
  - Queue operations when offline
- [ ] Multi-session support
  - Switch between different users/sessions
  - Session management UI
- [ ] Advanced visualization
  - Render simple plots in terminal (plotext)
  - Open visualizations in browser
- [ ] Plugins/Extensions
  - Custom themes
  - Custom commands
  - Integration with other tools

## Success Metrics

### MVP Success Criteria
1. Can authenticate and maintain session
2. Can create conversations and send/receive messages
3. Can upload datasets
4. Can browse visualizations
5. Stable, no crashes during normal use
6. Clear error messages for common issues
7. Documentation complete

### Performance Targets
- Message send/receive: < 2s (network dependent)
- UI responsiveness: < 100ms for interactions
- Startup time: < 1s
- Memory usage: < 100MB for typical session

## Code Generation Setup

### Makefile
```makefile
.PHONY: update
update:
	@echo "Pulling down latest OpenAPI Specification"
	wget https://raw.githubusercontent.com/d-callan/api-datamonkey/refs/heads/master/dist/openapi.yaml -O openapi.yaml
	@echo "OpenAPI Specification retrieved!"
	@echo "Starting client code generation"
	npx @openapitools/openapi-generator-cli generate \
		-i openapi.yaml \
		-g python \
		-o ./generated \
		--additional-properties=packageName=openapi_client,library=asyncio,useOneOfDiscriminatorLookup=true
	@echo "Code generation complete"
	@echo "Installing generated client..."
	pip install -e ./generated

.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	pip install -e .

.PHONY: run
run:
	python -m datamonkey_tui

.PHONY: dev
dev:
	textual run --dev src/datamonkey_tui/app.py

.PHONY: clean
clean:
	@echo "Cleaning generated files..."
	rm -rf generated/
	rm -f openapi.yaml
```

### openapitools.json
```json
{
  "$schema": "./node_modules/@openapitools/openapi-generator-cli/config.schema.json",
  "spaces": 2,
  "generator-cli": {
    "version": "7.11.0"
  }
}
```

### .openapi-generator-ignore
```
# Preserve custom wrapper code
src/datamonkey_tui/api/*.py

# Preserve config
.env
.env.example

# Preserve documentation
README.md
IMPLEMENTATION_PLAN.md
```

### .gitignore additions
```
# Generated code
generated/
openapi.yaml
.openapi-generator/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
.venv

# Config
.env

# IDE
.vscode/
.idea/
*.swp
```

### Generated Client Structure
After running `make update`, the generated client will have:

```
generated/
├── openapi_client/
│   ├── __init__.py
│   ├── api/
│   │   ├── chat_api.py              # Chat endpoints
│   │   ├── file_upload_and_qc_api.py # Dataset endpoints
│   │   ├── visualizations_api.py     # Viz endpoints
│   │   └── ...
│   ├── models/
│   │   ├── chat_conversation.py
│   │   ├── chat_message.py
│   │   ├── datasets.py
│   │   ├── visualization.py
│   │   └── ...
│   ├── api_client.py
│   ├── configuration.py
│   ├── exceptions.py
│   └── rest.py
├── setup.py
├── requirements.txt
└── README.md
```

### Wrapper Example
```python
# src/datamonkey_tui/api/client.py
from openapi_client import ApiClient, Configuration
from openapi_client.api import ChatApi, FileUploadAndQcApi, VisualizationsApi
from ..config.session import SessionManager

class DatamonkeyClient:
    """Wrapper around generated OpenAPI client with session management."""
    
    def __init__(self, base_url: str, session_manager: SessionManager):
        self.session_manager = session_manager
        
        # Configure generated client
        config = Configuration(host=base_url)
        self.api_client = ApiClient(configuration=config)
        
        # Initialize API instances
        self.chat = ChatApi(self.api_client)
        self.datasets = FileUploadAndQcApi(self.api_client)
        self.visualizations = VisualizationsApi(self.api_client)
    
    def _get_headers(self) -> dict:
        """Get headers with user token."""
        token = self.session_manager.get_token()
        if token:
            return {"user_token": token}
        return {}
    
    async def list_conversations(self):
        """List user conversations with automatic token injection."""
        return await self.chat.list_user_conversations(
            **self._get_headers()
        )
```

## Development Setup

### Prerequisites
- Python 3.10+
- Access to Datamonkey API (local or remote)
- Terminal with true color support (recommended)

### Quick Start
```bash
# Clone/create repo
cd ~/Documents/veg
mkdir tui-datamonkey
cd tui-datamonkey

# Setup Python environment
python -m venv venv
source venv/bin/activate

# Generate API client from OpenAPI spec
make update

# Install dependencies
make install

# Configure
cp .env.example .env
# Edit .env with API URL

# Run
make run

# Development mode (hot reload)
make dev
```

### Regenerating Client After API Changes
```bash
# Pull latest spec and regenerate
make update

# Reinstall if models changed
pip install -e ./generated
```

## Timeline Summary

- **Phase 1 (Foundation):** 2 days
- **Phase 2 (Chat Core):** 3 days
- **Phase 3 (Chat Polish):** 2 days
- **Phase 4 (Datasets):** 2 days
- **Phase 5 (Visualizations):** 2 days
- **Phase 6 (Polish & Testing):** 3 days

**Total MVP:** ~14 days (2-3 weeks)

## Open Questions

1. **API Base URL:** Should default to localhost:8080 or production URL?
   - Recommendation: localhost for dev, make configurable

2. **Session Persistence:** How long should sessions be kept?
   - Recommendation: Keep until explicitly cleared, show age in UI

3. **File Upload Size Limits:** Any restrictions on dataset size?
   - Need to check API limits

4. **Visualization Rendering:** Should we attempt terminal-based rendering?
   - Phase 1: Just show JSON spec
   - Future: Consider plotext or browser integration

5. **Multi-user Support:** Should TUI support multiple sessions/users?
   - Phase 1: Single session
   - Future: Session switcher

## Notes

- Focus on chat interface first (primary use case)
- Keep UI simple and keyboard-driven
- Prioritize stability over features
- Document as we go
- Test with real API early and often
