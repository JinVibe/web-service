"""
Web route specs (TDD).

Workflow (TADD with AI):
  RED  — Human (or pair) writes failing tests from README / 기능 명세.
  GREEN — Implement minimal code until tests pass.
  REFACTOR — Clean up while keeping tests green.

These tests encode R1–R3 from README (/, /home, /projects, /contact).
"""

from flask import url_for


def test_root_redirects_to_home(client):
    """R1: GET / must redirect visitors to /home."""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 302
    assert "/home" in (response.location or "")


def test_home_returns_welcome_content(client):
    """R1: /home returns 200 and shows service purpose / welcome."""
    response = client.get("/home")
    assert response.status_code == 200
    data = response.data.decode("utf-8")
    assert "Dev-Log에 오신 것을 환영합니다" in data
    assert "개인 포트폴리오" in data


def test_projects_lists_portfolio_content(client):
    """R2: /projects returns 200 and exposes at least one known project."""
    response = client.get("/projects")
    assert response.status_code == 200
    data = response.data.decode("utf-8")
    assert "프로젝트" in data
    assert "Kotlin" in data


def test_contact_exposes_channels(client):
    """R3: /contact returns 200 and shows contact labels (Email, GitHub)."""
    response = client.get("/contact")
    assert response.status_code == 200
    data = response.data.decode("utf-8")
    assert "연락처" in data
    assert "Email" in data
    assert "GitHub" in data


def test_nav_links_resolve_in_app_context(app):
    """Client-side nav: url_for names used in base template must exist."""
    with app.test_request_context("/"):
        assert url_for("home.index") == "/home"
        assert url_for("projects.list_projects") == "/projects"
        assert url_for("contact.index") == "/contact"
