"""Flask application factory for Dev-Log portfolio & blog."""

from flask import Flask

from app.bootstrap import register_blueprints


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    if config:
        app.config.update(config)

    register_blueprints(app)

    return app
