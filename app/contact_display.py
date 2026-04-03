"""Presentation rules for contact channels (keeps logic out of templates)."""

from typing import Any


def enrich_channels_for_display(channels: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Add display flags from raw JSON rows.

    External http(s) links open in a new tab with rel=noopener; mailto/tel stay same tab.
    """
    out: list[dict[str, Any]] = []
    for row in channels:
        url = str(row.get("url", ""))
        is_http = url.lower().startswith(("http://", "https://"))
        out.append({**row, "open_in_new_tab": is_http})
    return out
