"""Vega Editor URL generation utilities."""

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
    # Serialize spec to JSON (compact)
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
