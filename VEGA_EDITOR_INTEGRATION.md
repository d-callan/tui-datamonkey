# Vega Editor Integration

## Overview
The TUI includes built-in integration with the online Vega Editor, allowing users to open and interactively explore Vega-Lite visualizations directly in their browser.

## How It Works

### URL-Based Spec Loading
Vega Editor supports loading specifications via URL parameters:
```
https://vega.github.io/editor/#/url/vega-lite/{base64_encoded_spec}
```

### Workflow
1. User browses visualizations in TUI
2. Selects a visualization to view
3. Presses `V` to open in Vega Editor
4. Browser opens with spec pre-loaded
5. User can interactively modify, export, or share

## Features

### In TUI
- **[V] Open in Vega Editor** - Opens spec in browser
- **[C] Copy Editor URL** - Copies URL to clipboard for sharing
- **[E] Export JSON** - Save spec to local file
- **URL Preview** - Shows generated editor URL in status bar

### In Vega Editor (Browser)
- **Interactive Editing** - Modify spec in real-time
- **Live Preview** - See changes immediately
- **Export Options** - PNG, SVG, PDF
- **Share Links** - URL contains full spec, shareable
- **Documentation** - Built-in Vega-Lite docs
- **Examples** - Access to example gallery

## Implementation

### URL Generation
```python
import base64
import json

def generate_vega_editor_url(spec: dict) -> str:
    """Generate Vega Editor URL with pre-loaded spec."""
    # Compact JSON (no whitespace)
    spec_json = json.dumps(spec, separators=(',', ':'))
    
    # URL-safe base64 encoding
    spec_b64 = base64.urlsafe_b64encode(spec_json.encode()).decode()
    
    # Construct URL
    return f"https://vega.github.io/editor/#/url/vega-lite/{spec_b64}"
```

### Example
```python
# Sample Vega-Lite spec
spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "mark": "bar",
    "data": {
        "values": [
            {"category": "A", "value": 28},
            {"category": "B", "value": 55},
            {"category": "C", "value": 43}
        ]
    },
    "encoding": {
        "x": {"field": "category", "type": "nominal"},
        "y": {"field": "value", "type": "quantitative"}
    }
}

# Generate URL
url = generate_vega_editor_url(spec)
# https://vega.github.io/editor/#/url/vega-lite/eyIkc2NoZW1hIjoi...

# Open in browser
import webbrowser
webbrowser.open(url)
```

## Use Cases

### 1. Interactive Exploration
User wants to understand a complex phylogenetic tree visualization:
- Open in Vega Editor
- Adjust colors, sizes, labels
- Zoom into specific branches
- Export modified version

### 2. Presentation Preparation
User needs high-quality visualization for publication:
- Open in Vega Editor
- Fine-tune aesthetics
- Export as SVG (vector graphics)
- Use in paper/presentation

### 3. Collaboration
User wants to share visualization with colleague:
- Generate editor URL
- Copy to clipboard
- Send to colleague via email/chat
- Colleague opens same spec in browser

### 4. Learning
User wants to understand how visualization was created:
- Open in Vega Editor
- View full spec with syntax highlighting
- Read inline documentation
- Experiment with modifications

## Benefits

### For Users
- **No Installation** - Works in any browser
- **Full Features** - Complete Vega Editor toolset
- **Shareable** - URLs contain full spec
- **Export Options** - Multiple formats (PNG, SVG, PDF)
- **Interactive** - Real-time editing and preview

### For TUI
- **No Rendering** - Avoid terminal graphics limitations
- **Lightweight** - Just generate URLs
- **Standard Tool** - Users may already know Vega Editor
- **Future-Proof** - Vega Editor maintained by Vega team

## Limitations

### URL Length
- Base64 encoding increases size (~33% overhead)
- Very large specs may hit URL length limits (2048 chars in some browsers)
- **Solution:** For large specs, offer "Export JSON" instead

### Internet Required
- Requires internet connection to access Vega Editor
- **Solution:** Also provide local export option

### Browser Dependency
- Requires browser to be available
- **Solution:** Gracefully handle if browser can't open

## Error Handling

```python
def open_in_vega_editor(spec: dict) -> tuple[bool, str]:
    """Open spec in Vega Editor with error handling.
    
    Returns:
        (success, message) tuple
    """
    try:
        url = generate_vega_editor_url(spec)
        
        # Check URL length
        if len(url) > 2000:
            return False, "Spec too large for URL. Use 'Export JSON' instead."
        
        # Try to open browser
        webbrowser.open(url)
        return True, f"Opened in browser: {url[:50]}..."
        
    except Exception as e:
        return False, f"Failed to open browser: {e}"
```

## Future Enhancements

### Phase 1 (MVP)
- ✅ Generate editor URLs
- ✅ Open in browser
- ✅ Copy URL to clipboard

### Phase 2 (Nice-to-have)
- 🔲 QR code generation for mobile sharing
- 🔲 Shortened URLs (via URL shortener service)
- 🔲 Embed mode (open in embedded iframe)
- 🔲 Custom Vega Editor instance (self-hosted)

### Phase 3 (Advanced)
- 🔲 Vega Editor API integration (if available)
- 🔲 Save modified specs back to Datamonkey
- 🔲 Version history for visualizations
- 🔲 Collaborative editing (multiple users)

## Testing

### Unit Tests
```python
def test_generate_vega_editor_url():
    spec = {"$schema": "...", "mark": "bar"}
    url = generate_vega_editor_url(spec)
    
    assert url.startswith("https://vega.github.io/editor/#/url/vega-lite/")
    assert len(url) > 50
    
    # Decode and verify
    encoded_part = url.split("/")[-1]
    decoded = base64.urlsafe_b64decode(encoded_part).decode()
    assert json.loads(decoded) == spec
```

### Integration Tests
```python
def test_vega_editor_roundtrip():
    """Test that generated URLs work in actual Vega Editor."""
    spec = create_test_spec()
    url = generate_vega_editor_url(spec)
    
    # Could use Selenium/Playwright to verify URL loads correctly
    # For now, just verify URL structure
    assert "vega.github.io/editor" in url
```

### Manual Testing
1. Generate URL for sample spec
2. Open in browser
3. Verify spec loads correctly
4. Test editing functionality
5. Test export options
6. Verify shareable URL works

## Documentation

### User Guide
```markdown
## Opening Visualizations in Vega Editor

1. Navigate to Visualizations screen
2. Select a visualization from the list
3. Press `V` to open in Vega Editor
4. Your browser will open with the visualization pre-loaded
5. Explore, edit, and export as needed

### Sharing Visualizations

1. Select a visualization
2. Press `C` to copy the Vega Editor URL
3. Share the URL with colleagues
4. They can open it directly in their browser
```

### Keyboard Shortcuts
- `V` - Open in Vega Editor
- `C` - Copy editor URL to clipboard
- `E` - Export spec to JSON file
- `Esc` - Close visualization detail

## References

- [Vega Editor](https://vega.github.io/editor/)
- [Vega-Lite Documentation](https://vega.github.io/vega-lite/)
- [Vega-Lite Examples](https://vega.github.io/vega-lite/examples/)
- [URL Parameters Discussion](https://groups.google.com/g/vega-js/c/e1r80VDwi3U)

## Summary

Vega Editor integration provides a powerful, zero-installation way for users to:
- Interactively explore visualizations
- Make custom modifications
- Export high-quality graphics
- Share with collaborators

The implementation is simple (just URL generation) but provides significant value by leveraging the full capabilities of the Vega ecosystem.
