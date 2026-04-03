"""Contact blueprint: channels for visitors to reach the developer."""

from flask import Blueprint, render_template

from app.contact_display import enrich_channels_for_display
from app.site_data import load_contact_channels

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact")
def index():
    """Display contact channels for collaboration inquiries."""
    channels = enrich_channels_for_display(load_contact_channels())
    return render_template("contact.html", channels=channels)
