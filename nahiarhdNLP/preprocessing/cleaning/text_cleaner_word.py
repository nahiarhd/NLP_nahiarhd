"""
Text cleaner for Indonesian text processing.
"""

import re


class TextCleanerWord:
    """Clean and normalize Indonesian text."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize text cleaner.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self._flags = {
            "clean_urls": kwargs.get("clean_urls", True),
            "clean_mentions": kwargs.get("clean_mentions", True),
            "clean_hashtags": kwargs.get("clean_hashtags", True),
            "clean_html": kwargs.get("clean_html", True),
        }

    def clean_urls(self, text: str, force: bool = False) -> str:
        """Remove URL protocols (http:// or https://) but keep the rest of the URL.

        Args:
            text: Input text
            force: Force remove protocols even if remove_urls flag is False

        Returns:
            Text with URL protocols removed
        """
        if not self._flags["clean_urls"] and not force:
            return text

        # Pattern untuk URL protocols
        url_pattern = r"http[s]?://"
        result = re.sub(url_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_mentions(self, text: str, force: bool = False) -> str:
        """Remove @ from mentions but keep the username text.

        Args:
            text: Input text
            force: Force remove @ even if remove_mentions flag is False

        Returns:
            Text with @ removed from mentions
        """
        if not self._flags["clean_mentions"] and not force:
            return text

        # Pattern untuk mentions, remove @ but keep the word with space
        mention_pattern = r"@(\w+)"
        result = re.sub(mention_pattern, r" \1", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_hashtags(self, text: str, force: bool = False) -> str:
        """Remove # from hashtags but keep the tag text.

        Args:
            text: Input text
            force: Force remove # even if remove_hashtags flag is False

        Returns:
            Text with # removed from hashtags
        """
        if not self._flags["clean_hashtags"] and not force:
            return text

        # Pattern untuk hashtags, remove # but keep the word with space
        hashtag_pattern = r"#(\w+)"
        result = re.sub(hashtag_pattern, r" \1", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def clean_html(self, text: str, force: bool = False) -> str:
        """Remove HTML tags from text.

        Args:
            text: Input text with HTML tags
            force: Force remove HTML even if enable_html_cleaning flag is False

        Returns:
            Text with HTML tags removed
        """
        if not self._flags["clean_html"] and not force:
            return text

        # Pattern untuk HTML tags - replace with space to preserve word boundaries
        html_pattern = r"<[^>]+>"
        result = re.sub(html_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def get_options(self) -> dict:
        """Get current cleaning options.

        Returns:
            Dictionary of current options
        """
        return dict(self._flags)
