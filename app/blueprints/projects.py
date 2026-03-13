"""Projects blueprint: list of projects with tech stack and descriptions."""

from flask import Blueprint, render_template

projects_bp = Blueprint("projects", __name__)

PROJECTS = [
    {
        "title": "모바일 앱 (Kotlin)",
        "stack": ["Kotlin", "Android", "Jetpack Compose"],
        "description": "안드로이드 네이티브 앱 개발. Compose 기반 UI와 MVVM 구조 적용.",
    },
    {
        "title": "AI 기반 서비스",
        "stack": ["Python", "TensorFlow", "FastAPI"],
        "description": "머신러닝 모델을 활용한 추천 및 분류 서비스 백엔드 구축.",
    },
    {
        "title": "Dev-Log (본 서비스)",
        "stack": ["Python", "Flask", "HTML/CSS"],
        "description": "개인 포트폴리오 및 기술 블로그. Blueprint 기반 모듈화.",
    },
]


@projects_bp.route("/projects")
def list_projects():
    """Display project list with tech stack and details."""
    return render_template("projects.html", projects=PROJECTS)
