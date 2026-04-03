"""Contact blueprint: channels for visitors to reach the developer."""

from flask import Blueprint, render_template

from app.site_data import load_contact_channels

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact")
def index():
    """Display contact channels for collaboration inquiries."""
    return render_template("contact.html", channels=load_contact_channels())
