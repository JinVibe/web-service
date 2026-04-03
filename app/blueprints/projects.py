"""Projects blueprint: list of projects with tech stack and descriptions."""

from flask import Blueprint, render_template

from app.site_data import load_projects

projects_bp = Blueprint("projects", __name__)


@projects_bp.route("/projects")
def list_projects():
    """Display project list with tech stack and details."""
    return render_template("projects.html", projects=load_projects())
