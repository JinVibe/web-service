"""Load portfolio content from JSON under ``app/data/`` (no extra dependencies)."""

import json
from pathlib import Path
from typing import Any

_DATA_DIR = Path(__file__).resolve().parent / "data"


def _load_json(filename: str, default: Any) -> Any:
    path = _DATA_DIR / filename
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return default


def load_projects() -> list[dict[str, Any]]:
    """Project cards: title, stack[], description."""
    raw = _load_json("projects.json", [])
    if not isinstance(raw, list):
        return []
    return [p for p in raw if isinstance(p, dict)]


def load_contact_channels() -> list[dict[str, Any]]:
    """Contact rows: label, url, optional icon."""
    raw = _load_json("contact.json", [])
    if not isinstance(raw, list):
        return []
    return [c for c in raw if isinstance(c, dict)]
