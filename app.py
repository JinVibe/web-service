"""
Lab / legacy CLI entry: re-exports the same ``app`` as :mod:`wsgi`.

Prefer ``wsgi.py`` (or ``flask --app wsgi run``) to avoid confusion with the
``app`` package directory.
"""

from wsgi import app

__all__ = ["app"]
