"""JSON API for portfolio data; Flasgger reads OpenAPI fragments from view docstrings (after ``---``)."""

from flask import Blueprint, jsonify

from app.contact_display import enrich_channels_for_display
from app.site_data import load_contact_channels, load_projects

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.get("/projects")
def list_projects_json():
    """
    프로젝트 카드 목록
    ---
    tags:
      - Projects
    summary: List projects
    description: Returns project cards (title, stack, description) loaded from JSON.
    produces:
      - application/json
    responses:
      200:
        description: List of project objects
        schema:
          type: array
          items:
            type: object
            properties:
              title:
                type: string
              stack:
                type: array
                items:
                  type: string
              description:
                type: string
    """
    return jsonify(load_projects())


@api_bp.get("/contact/channels")
def list_contact_channels_json():
    """
    연락 채널 목록
    ---
    tags:
      - Contact
    summary: List contact channels
    description: >
      Returns contact rows with display hints (e.g. open_in_new_tab for http(s) links),
      same enrichment as the HTML contact page.
    produces:
      - application/json
    responses:
      200:
        description: List of channel objects
        schema:
          type: array
          items:
            type: object
            properties:
              label:
                type: string
              url:
                type: string
              open_in_new_tab:
                type: boolean
    """
    return jsonify(enrich_channels_for_display(load_contact_channels()))
