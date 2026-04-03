"""
Profanity masking for user-visible text.

Word list is loaded from ``app/data/profanity_words.json`` (see ``site_data.load_profanity_words``).
"""

from __future__ import annotations

import re
from typing import Iterable, Match

from app.site_data import load_profanity_words


def _compile_word_pattern(word: str) -> re.Pattern[str]:
    """Build a case-insensitive, word-boundary pattern for one token."""
    return re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)


def _replacement_for_match(match: Match[str], mask_char: str) -> str:
    """Preserve original span length so layout stays stable."""
    return mask_char * len(match.group(0))


def _mask_words(text: str, words: Iterable[str], mask_char: str) -> str:
    """Sequentially apply masking for each configured word."""
    result = text
    for word in words:
        pattern = _compile_word_pattern(word)
        result = pattern.sub(
            lambda m, mc=mask_char: _replacement_for_match(m, mc),
            result,
        )
    return result


def mask_profanity(text: str, mask_char: str = "*") -> str:
    """
    Replace configured profanity tokens with ``mask_char`` repeated to the same length.

    Parameters
    ----------
    text : str
        Input string (may be empty).
    mask_char : str
        Character repeated for each masked character (default ``"*"``).

    Returns
    -------
    str
        Text with profanity masked.
    """
    if not text:
        return ""

    return _mask_words(text, load_profanity_words(), mask_char)
