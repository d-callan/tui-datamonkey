"""Test Vega Editor utilities."""

import pytest
from datamonkey_tui.utils.vega_editor import generate_vega_editor_url


class TestVegaEditor:
    """Test Vega Editor URL generation."""
    
    def test_generate_url_simple(self):
        """Test generating URL with simple spec."""
        spec = {"mark": "bar", "data": {"values": [{"a": 1, "b": 2}]}}
        
        url = generate_vega_editor_url(spec)
        
        assert url.startswith("https://vega.github.io/editor/#/url/vega-lite/")
        # Should be base64 encoded
        encoded_part = url.split("/")[-1]
        assert len(encoded_part) > 50
    
    def test_generate_url_complex(self):
        """Test generating URL with complex spec."""
        spec = {
            "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
            "mark": "point",
            "encoding": {
                "x": {"field": "x", "type": "quantitative"},
                "y": {"field": "y", "type": "quantitative"}
            },
            "data": {"values": [{"x": 1, "y": 2}, {"x": 3, "y": 4}]}
        }
        
        url = generate_vega_editor_url(spec)
        
        assert url.startswith("https://vega.github.io/editor/#/url/vega-lite/")
        assert "vega-lite" in url
