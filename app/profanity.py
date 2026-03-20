"""Profanity masking — interface only (TDD step 1: Define Interface)."""


def mask_profanity(text: str, mask_char: str = "*") -> str:
    """
    Replace known profanity tokens with mask_char repeated to the same length.

    Parameters
    ----------
    text : str
        Input string (may be empty).
    mask_char : str
        Single character used for masking (default "*").

    Returns
    -------
    str
        Text with profanity masked (not implemented — RED phase).
    """
    pass
