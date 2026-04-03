"""Entry point for running the Dev-Log Flask application."""

import os

from wsgi import app


def _debug_from_env() -> bool:
    """True only when FLASK_DEBUG or DEBUG is set to a truthy value (default: off)."""
    val = os.environ.get("FLASK_DEBUG", os.environ.get("DEBUG", ""))
    return val.strip().lower() in ("1", "true", "yes", "on")


if __name__ == "__main__":
    app.run(debug=_debug_from_env(), host="127.0.0.1", port=5000)
