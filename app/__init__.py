"""Flask application factory for Dev-Log portfolio & blog."""

from flask import Flask


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    if config:
        app.config.update(config)

    from app.blueprints.home import home_bp
    from app.blueprints.projects import projects_bp

    app.register_blueprint(home_bp, url_prefix="")
    app.register_blueprint(projects_bp, url_prefix="")

    return app
