"""Vega Editor URL generation utilities."""

import json
import logging
import webbrowser
from typing import Any, Dict

from lzstring import LZString

logger = logging.getLogger(__name__)


def _ensure_spec_dict(spec: Any) -> Dict[str, Any]:
    """Normalize specification to a dictionary."""
    if isinstance(spec, dict):
        return spec

    if isinstance(spec, str):
        try:
            maybe_dict = json.loads(spec)
            if isinstance(maybe_dict, dict):
                return maybe_dict
        except json.JSONDecodeError:
            pass

    raise ValueError("Visualization spec must be a dict or JSON string")


def generate_vega_editor_url(spec: Any) -> str:
    """Generate Vega Editor URL with pre-loaded spec.
    
    Args:
        spec: Vega-Lite specification dictionary
        
    Returns:
        URL to Vega Editor with spec pre-loaded
    """
    spec_dict = _ensure_spec_dict(spec)
    spec_keys = list(spec_dict.keys())[:10]
    logger.info(
        "Preparing Vega spec for editor | type=%s keys=%s",
        type(spec).__name__,
        spec_keys,
    )

    # Serialize spec to JSON (compact)
    spec_json = json.dumps(spec_dict, separators=(',', ':'))
    logger.info(
        "Serialized Vega spec | length=%d preview=%s",
        len(spec_json),
        spec_json[:200],
    )
    
    # LZ-string encode for Vega Editor route, then verify round-trip
    encoder = LZString()
    encoded = encoder.compressToEncodedURIComponent(spec_json)
    decoded_preview = encoder.decompressFromEncodedURIComponent(encoded)
    logger.info(
        "Encoded Vega spec | length=%d decompressed_preview=%s",
        len(encoded),
        (decoded_preview or "")[:200] if decoded_preview else "<decode_failed>",
    )

    # Construct editor URL pointing to documented /url route
    return f"https://vega.github.io/editor/#/url/vega-lite/{encoded}"


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
