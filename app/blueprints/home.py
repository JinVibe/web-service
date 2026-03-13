"""Home blueprint: service purpose and developer introduction."""

from flask import Blueprint, render_template, redirect, url_for

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def root():
    """Redirect root to home."""
    return redirect(url_for("home.index"))


@home_bp.route("/home")
def index():
    """Display developer introduction and service purpose."""
    return render_template("home.html")
