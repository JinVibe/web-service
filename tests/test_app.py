"""
RED 단계: 비속어 마스킹 (mask_profanity)

워크플로우 (AI 협업 TDD):
  1. Define Interface — app/profanity.py 에 시그니처만 정의
  2. Generate Tests — 요구사항 기반 테스트 작성·검토 후 본 파일에 저장
  3. Implement Code — mask_profanity 구현으로 GREEN
  4. Verify & Refactor — 코드 리뷰·품질 개선 후 승인

현재: 구현 없음 → 이 파일의 테스트는 반드시 실패해야 함 (RED).
"""

from app.profanity import mask_profanity


def test_mask_profanity_empty_string():
    """빈 문자열은 빈 문자열을 반환한다."""
    assert mask_profanity("") == ""


def test_mask_profanity_no_profanity_unchanged():
    """비속어가 없으면 원문과 동일하다."""
    assert mask_profanity("hello world") == "hello world"


def test_mask_profanity_masks_lowercase_word():
    """명세 비속어 'damn'은 길이만큼 mask_char로 치환된다."""
    assert mask_profanity("damn") == "****"


def test_mask_profanity_case_insensitive():
    """대소문자와 무관하게 동일 비속어를 마스킹한다."""
    assert mask_profanity("Damn") == "****"


def test_mask_profanity_within_sentence_all_occurrences():
    """문장 안에서 등장하는 모든 비속어를 치환하고 나머지는 유지한다."""
    assert mask_profanity("oh damn it") == "oh **** it"


def test_mask_profanity_custom_mask_char():
    """mask_char를 '#'로 주면 해당 문자로 길이만큼 치환한다."""
    assert mask_profanity("damn", mask_char="#") == "####"
