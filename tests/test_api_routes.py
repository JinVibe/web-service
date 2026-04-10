"""JSON API and Flasgger / Swagger UI (OpenAPI from docstrings)."""


def test_api_projects_returns_json_list(client):
    response = client.get("/api/projects")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert isinstance(data, list)
    if data:
        assert "title" in data[0]


def test_api_contact_channels_returns_json_list(client):
    response = client.get("/api/contact/channels")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert isinstance(data, list)
    if data:
        assert "label" in data[0]
        assert "open_in_new_tab" in data[0]


def test_swagger_spec_json(client):
    response = client.get("/apispec_1.json")
    assert response.status_code == 200
    spec = response.get_json()
    assert spec is not None
    assert "swagger" in spec or "openapi" in spec
    paths = spec.get("paths") or {}
    assert "/api/projects" in paths
    assert "/api/contact/channels" in paths


def test_swagger_ui_page(client):
    response = client.get("/apidocs/")
    assert response.status_code == 200
    body = response.data.decode("utf-8").lower()
    assert "swagger" in body
