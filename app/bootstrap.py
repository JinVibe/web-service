"""Register Flask blueprints on the application (keeps ``create_app`` slim)."""

from flask import Flask


def register_blueprints(app: Flask) -> None:
    """Attach all URL blueprints to ``app``."""
    from app.blueprints.api import api_bp
    from app.blueprints.contact import contact_bp
    from app.blueprints.home import home_bp
    from app.blueprints.projects import projects_bp

    # 빈 url_prefix를 넘기면 블루프린트에 설정한 url_prefix(예: api의 /api)까지 지워지므로 생략한다.
    for bp in (home_bp, projects_bp, contact_bp, api_bp):
        app.register_blueprint(bp)

    _init_flasgger(app)


def _init_flasgger(app: Flask) -> None:
    """Swagger UI at ``/apidocs/``, merged spec at ``/apispec.json``."""
    if app.config.get("DISABLE_SWAGGER"):
        return

    app.config.setdefault(
        "SWAGGER",
        {
            "title": "Dev-Log API",
            "description": "Interactive JSON API for portfolio and contact data.",
            "version": "1.0.0",
            "uiversion": 3,
        },
    )

    from flasgger import Swagger

    Swagger(app)
