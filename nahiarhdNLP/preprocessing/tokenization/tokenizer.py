"""Tokenizer for Indonesian text."""

import re


class Tokenizer:
    """Split text into tokens, keeping URLs, emails, mentions, and hashtags.

    Source: https://docs.python.org/3/library/re.html#re.findall
    Alternation is tried left to right, so structured tokens match before
    generic words or single punctuation characters.
    """

    _token_re = re.compile(
        r"https?://[^\s]+"
        r"|www\.[^\s]+"
        r"|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
        r"|@\w+"
        r"|#\w+"
        r"|[\w]+(?:-[\w]+)*"
        r"|[^\s\w]"
    )

    def tokenize(self, text: str) -> list:
        if not text:
            return []
        return self._token_re.findall(text)
