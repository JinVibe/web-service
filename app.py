"""
WSGI/CLI entry: exposes ``app`` for ``flask run`` and hosting docs.

Application factory and blueprints live under the ``app`` package (``app/__init__.py``).
Domain helpers (e.g. profanity masking) live in sibling modules such as ``app.profanity``.
"""

from app import create_app

app = create_app()
