"""
WSGI / ``flask run`` entry point.

Exposes ``app`` here so the Python package ``app/`` (application code) is not
confused with a top-level module named ``app`` when configuring ``FLASK_APP``.
"""

from app import create_app

app = create_app()
