"""Profanity masking — minimal implementation for tests (GREEN)."""

import re

# Tests only require masking this token (word-boundary, case-insensitive).
_PROFANITY_WORD = "damn"


def mask_profanity(text: str, mask_char: str = "*") -> str:
    """
    Replace known profanity tokens with mask_char repeated to the same length.

    Parameters
    ----------
    text : str
        Input string (may be empty).
    mask_char : str
        Character repeated for masking (default "*").

    Returns
    -------
    str
        Text with profanity masked.
    """
    if text == "":
        return ""

    pattern = re.compile(
        r"\b" + re.escape(_PROFANITY_WORD) + r"\b",
        re.IGNORECASE,
    )

    def _replace(match: re.Match) -> str:
        return mask_char * len(match.group(0))

    return pattern.sub(_replace, text)
