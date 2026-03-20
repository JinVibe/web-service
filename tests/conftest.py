"""Pytest fixtures: Flask app and test client (TDD / integration-style checks)."""

import pytest

from app import create_app


@pytest.fixture
def app():
    """Flask app with TESTING=True for isolated test runs."""
    application = create_app({"TESTING": True})
    return application


@pytest.fixture
def client(app):
    """HTTP client without starting a real server (in-process)."""
    return app.test_client()
