"""Register Flask blueprints on the application (keeps ``create_app`` slim)."""

from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Attach all URL blueprints to ``app``."""
    from app.blueprints.contact import contact_bp
    from app.blueprints.home import home_bp
    from app.blueprints.projects import projects_bp

    for bp in (home_bp, projects_bp, contact_bp):
        app.register_blueprint(bp, url_prefix="")
