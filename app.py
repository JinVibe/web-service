"""
Lab / legacy CLI entry: re-exports the same ``app`` as :mod:`wsgi`.

권장 진입은 ``wsgi.py`` (또는 ``flask --app wsgi run``) — 패키지 ``app/`` 과 이름 혼동을 줄인다.
팩토리·Blueprint는 ``app`` 패키지, 도메인 헬퍼는 ``app.profanity`` 등에 둔다.
"""

from wsgi import app

__all__ = ["app"]
