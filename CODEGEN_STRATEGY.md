# Code Generation Strategy

## Overview
Use OpenAPI Generator to auto-generate the Python API client from the OpenAPI spec, following the same pattern as service-datamonkey.

## Why Code Generation?

### Benefits
1. **Type Safety** - Generated Pydantic models match API exactly
2. **Consistency** - Same tool (openapi-generator-cli) as service-datamonkey
3. **Maintainability** - API changes automatically propagate via `make update`
4. **Less Boilerplate** - No manual HTTP client code
5. **Documentation** - Generated code includes docstrings from OpenAPI spec

### Comparison to Manual Implementation

| Aspect | Generated | Manual |
|--------|-----------|--------|
| Initial Setup | 5 minutes | 2-3 hours |
| API Updates | `make update` (30 sec) | Manual changes (30+ min) |
| Type Safety | ✅ Automatic | ⚠️ Manual typing |
| API Coverage | ✅ 100% | ⚠️ Only what we implement |
| Maintenance | ✅ Low | ❌ High |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        TUI Application                       │
│  (src/datamonkey_tui/)                                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Wrapper Layer                             │
│  (src/datamonkey_tui/api/)                                  │
│  - Session management                                        │
│  - Token injection                                           │
│  - Error handling                                            │
│  - TUI-specific helpers                                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Generated OpenAPI Client                        │
│  (generated/openapi_client/)                                │
│  - ChatApi, FileUploadAndQcApi, VisualizationsApi           │
│  - Pydantic models (ChatConversation, ChatMessage, etc.)    │
│  - HTTP client (httpx async)                                │
│  - Auto-generated from openapi.yaml                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ Datamonkey   │
                  │ API Service  │
                  └──────────────┘
```

## Workflow

### Initial Setup
```bash
# 1. Create openapitools.json config
# 2. Create Makefile with update target
# 3. Run code generation
make update

# 4. Install generated client
pip install -e ./generated
```

### Development Cycle
```bash
# When API spec changes:
make update              # Pull spec + regenerate
pip install -e ./generated  # Reinstall if models changed

# TUI code automatically uses new types/endpoints
```

### What Gets Generated

**APIs (generated/openapi_client/api/):**
- `ChatApi` - Conversation and message endpoints
- `FileUploadAndQcApi` - Dataset upload/management
- `VisualizationsApi` - Visualization retrieval
- `JobsApi`, `MethodsApi`, etc. - Other endpoints

**Models (generated/openapi_client/models/):**
- `ChatConversation` - Conversation object
- `ChatMessage` - Message object
- `Datasets` - Dataset list/details
- `Visualization` - Visualization object
- All other schema objects from OpenAPI spec

**Infrastructure:**
- `ApiClient` - HTTP client wrapper
- `Configuration` - Client configuration
- `RESTClientObject` - Async HTTP implementation
- `ApiException` - Error types

### What We Write (Wrapper Layer)

**src/datamonkey_tui/api/client.py:**
```python
class DatamonkeyClient:
    """Thin wrapper with session management."""
    
    def __init__(self, base_url: str, session_manager: SessionManager):
        # Initialize generated client
        config = Configuration(host=base_url)
        self.api_client = ApiClient(configuration=config)
        
        # Create API instances
        self.chat = ChatApi(self.api_client)
        self.datasets = FileUploadAndQcApi(self.api_client)
        self.visualizations = VisualizationsApi(self.api_client)
        
        self.session_manager = session_manager
    
    def _inject_token(self, kwargs: dict) -> dict:
        """Add user_token header to all requests."""
        token = self.session_manager.get_token()
        if token:
            kwargs.setdefault('_headers', {})['user_token'] = token
        return kwargs
    
    async def list_conversations(self, **kwargs):
        """Wrapper with automatic token injection."""
        kwargs = self._inject_token(kwargs)
        return await self.chat.list_user_conversations(**kwargs)
```

**src/datamonkey_tui/api/chat.py:**
```python
class ChatHelper:
    """Chat-specific helpers and utilities."""
    
    def __init__(self, client: DatamonkeyClient):
        self.client = client
    
    async def send_message_and_wait(self, conversation_id: str, message: str):
        """Send message and poll for response (if needed)."""
        # Use generated client methods
        response = await self.client.chat.send_conversation_message(
            conversation_id=conversation_id,
            body={"message": message},
            _headers={"user_token": self.client.session_manager.get_token()}
        )
        return response
```

## Generator Configuration

### openapi-generator-cli Options

**Generator:** `python`
- Generates Python 3.10+ code
- Uses Pydantic for models
- Async support with httpx

**Additional Properties:**
- `packageName=openapi_client` - Package name
- `library=asyncio` - Use async/await
- `useOneOfDiscriminatorLookup=true` - Better polymorphism support

### Alternative Generators Considered

1. **openapi-python-client** ⭐ Alternative
   - More modern, cleaner output
   - Better type hints
   - Consider if openapi-generator-cli has issues

2. **datamodel-code-generator**
   - Only generates models, not client
   - Would need manual HTTP client
   - Not suitable for our needs

## Files to Preserve (.openapi-generator-ignore)

```
# Our custom wrapper code
src/datamonkey_tui/api/*.py

# Configuration
.env
.env.example

# Documentation
README.md
IMPLEMENTATION_PLAN.md
CODEGEN_STRATEGY.md

# Tests
tests/
```

## Gitignore Strategy

**Commit to Git:**
- Makefile
- openapitools.json
- .openapi-generator-ignore
- Wrapper code (src/datamonkey_tui/api/)
- Documentation

**Ignore (regenerate on demand):**
- generated/ directory
- openapi.yaml (downloaded spec)
- .openapi-generator/ metadata

**Rationale:** Generated code can be recreated anytime with `make update`, so no need to commit it.

## Testing Strategy

### Generated Code
- No need to test (generated by trusted tool)
- Covered by OpenAPI spec validation

### Wrapper Layer
- Unit tests for token injection
- Unit tests for error handling
- Mock the generated client

### Integration Tests
- Test against real API
- Verify generated client works correctly
- Test full request/response cycle

## Troubleshooting

### Issue: Generated code doesn't match API
**Solution:** Regenerate with `make update`

### Issue: Import errors after regeneration
**Solution:** Reinstall generated package: `pip install -e ./generated`

### Issue: Type errors in wrapper
**Solution:** Check generated model definitions, update wrapper types

### Issue: Missing endpoints
**Solution:** Verify OpenAPI spec is up to date, regenerate

## Migration Path

If we later want to switch generators:

1. Update Makefile to use new generator
2. Run `make clean && make update`
3. Update wrapper imports
4. Fix any type differences
5. Test thoroughly

The wrapper layer isolates the TUI from generator changes.

## Benefits Realized

### Development Speed
- **Before:** Write HTTP client, models, serialization = 2-3 hours
- **After:** `make update` = 30 seconds

### Maintenance
- **Before:** Manual updates for each API change
- **After:** `make update` pulls latest spec

### Type Safety
- **Before:** Manual type hints, easy to get wrong
- **After:** Generated Pydantic models, always correct

### API Coverage
- **Before:** Only implement what we need now
- **After:** Full API available, can add features easily

## Conclusion

Using OpenAPI code generation:
1. Saves significant development time
2. Reduces maintenance burden
3. Ensures type safety and API consistency
4. Follows service-datamonkey's proven pattern
5. Allows focus on TUI logic, not HTTP plumbing

**Recommendation:** Proceed with openapi-generator-cli for Python client generation.
