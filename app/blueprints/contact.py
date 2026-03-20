"""Contact blueprint: channels for visitors to reach the developer."""

from flask import Blueprint, render_template

contact_bp = Blueprint("contact", __name__)

CONTACT_CHANNELS = [
    {"label": "Email", "url": "mailto:loonaticvibe@gmail.com", "icon": "email"},
    {"label": "GitHub", "url": "https://github.com/JinVibe", "icon": "github"},
]


@contact_bp.route("/contact")
def index():
    """Display contact channels for collaboration inquiries."""
    return render_template("contact.html", channels=CONTACT_CHANNELS)
