"""
RED 단계: 사용자 로그인 (User Login)

실제 로그인 라우트·세션 처리 코드는 아직 없음.
구현 후 GREEN 단계에서 이 테스트들이 통과하도록 맞춘다.

실행 시 기대: 이 파일의 테스트는 모두 실패(404 등)해야 함.
"""

import pytest


# --- 명세 상수 (구현 시 앱과 맞출 것) ---
LOGIN_PATH = "/login"
LOGOUT_PATH = "/logout"
DEMO_USERNAME = "demo"
DEMO_PASSWORD = "correct-password"


def test_login_page_renders_form(client):
    """GET /login: 로그인 폼이 200으로 표시되고 username/password 입력 필드가 있다."""
    response = client.get(LOGIN_PATH)
    assert response.status_code == 200
    html = response.data.decode("utf-8", errors="replace").lower()
    assert "username" in html or "user" in html
    assert "password" in html


def test_login_post_valid_redirects_and_sets_session(client):
    """POST /login (올바른 자격증명): 리다이렉트 + 세션에 로그인 사용자 식별자가 저장된다."""
    response = client.post(
        LOGIN_PATH,
        data={"username": DEMO_USERNAME, "password": DEMO_PASSWORD},
        follow_redirects=False,
    )
    assert response.status_code in (302, 303), "expected redirect on successful login"
    location = response.location or ""
    assert "/home" in location or "/dashboard" in location.lower()

    with client.session_transaction() as sess:
        assert "user_id" in sess or "username" in sess


def test_login_post_invalid_shows_error(client):
    """POST /login (잘못된 비밀번호): 로그인 페이지에 오류 메시지가 보인다."""
    response = client.post(
        LOGIN_PATH,
        data={"username": DEMO_USERNAME, "password": "wrong-password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    html = response.data.decode("utf-8", errors="replace")
    assert any(
        phrase in html
        for phrase in ("잘못", "오류", "Invalid", "failed", "incorrect")
    )


def test_logout_clears_session_and_redirects(client):
    """GET /logout: 세션이 비워지고 홈 등으로 리다이렉트된다."""
    # 로그인 구현 전에는 세션 없이도 /logout 응답 자체가 명세대로여야 함 (RED에서는 404로 실패)
    client.post(
        LOGIN_PATH,
        data={"username": DEMO_USERNAME, "password": DEMO_PASSWORD},
        follow_redirects=True,
    )
    response = client.get(LOGOUT_PATH, follow_redirects=False)
    assert response.status_code in (302, 303)

    with client.session_transaction() as sess:
        assert not sess.get("user_id") and not sess.get("username")
