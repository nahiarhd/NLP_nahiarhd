"""
Text cleaner for Indonesian text processing.
"""

import re


class TextCleaner:
    """Clean and normalize Indonesian text."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize text cleaner.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        # Flags live in _flags so they do not shadow the methods of the same name.
        self._flags = {
            "remove_html": kwargs.get("remove_html", True),
            "remove_urls": kwargs.get("remove_urls", True),
            "remove_mentions": kwargs.get("remove_mentions", True),
            "remove_hashtags": kwargs.get("remove_hashtags", True),
            "remove_punctuation": kwargs.get("remove_punctuation", False),
            "remove_emoji": kwargs.get("remove_emoji", False),
            "remove_lowercase": kwargs.get("remove_lowercase", True),
            "remove_extra_spaces": kwargs.get("remove_extra_spaces", True),
            "remove_repeated_chars": kwargs.get("remove_repeated_chars", True),
            "remove_special_chars": kwargs.get("remove_special_chars", True),
            "remove_whitespace": kwargs.get("remove_whitespace", True),
            "remove_emails": kwargs.get("remove_emails", False),
            "remove_phones": kwargs.get("remove_phones", False),
            "remove_currency": kwargs.get("remove_currency", False),
            "remove_numbers": kwargs.get("remove_numbers", False),
        }

    def remove_urls(self, text: str, force: bool = False) -> str:
        """Remove URLs from text.

        Args:
            text: Input text
            force: Force remove URLs even if remove_urls flag is False

        Returns:
            Text with URLs removed
        """
        if not self._flags["remove_urls"] and not force:
            return text

        # Pattern untuk URL - replace with space to preserve word boundaries
        url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        result = re.sub(url_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_mentions(self, text: str, force: bool = False) -> str:
        """Remove mentions (@username) from text.

        Args:
            text: Input text
            force: Force remove mentions even if remove_mentions flag is False

        Returns:
            Text with mentions removed
        """
        if not self._flags["remove_mentions"] and not force:
            return text

        # Pattern untuk mentions - replace with space to preserve word boundaries
        mention_pattern = r"@\w+"
        result = re.sub(mention_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_hashtags(self, text: str, force: bool = False) -> str:
        """Remove hashtags (#tag) from text.

        Args:
            text: Input text
            force: Force remove hashtags even if remove_hashtags flag is False

        Returns:
            Text with hashtags removed
        """
        if not self._flags["remove_hashtags"] and not force:
            return text

        # Pattern untuk hashtags - replace with space to preserve word boundaries
        hashtag_pattern = r"#\w+"
        result = re.sub(hashtag_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_punctuation(self, text: str, force: bool = False) -> str:
        """Remove punctuation from text.

        Args:
            text: Input text
            force: Force remove punctuation even if remove_punctuation flag is False

        Returns:
            Text with punctuation removed
        """
        if not self._flags["remove_punctuation"] and not force:
            return text

        # Pattern untuk punctuation - replace with space to preserve word boundaries
        punctuation_pattern = r"[^\w\s]"
        result = re.sub(punctuation_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_lowercase(self, text: str) -> str:
        """Convert text to lowercase.

        Args:
            text: Input text

        Returns:
            Lowercase text
        """
        if not self._flags["remove_lowercase"]:
            return text

        return text.lower()

    def remove_extra_spaces(self, text: str) -> str:
        """Remove extra whitespace from text.

        Args:
            text: Input text

        Returns:
            Text with extra spaces removed
        """
        if not self._flags["remove_extra_spaces"]:
            return text

        # Replace multiple spaces with single space
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def remove_repeated_chars(self, text: str) -> str:
        """Remove repeated characters (e.g., 'bangetttt' -> 'banget').

        Args:
            text: Input text

        Returns:
            Text with repeated characters normalized
        """
        if not self._flags["remove_repeated_chars"]:
            return text

        # Pattern untuk repeated characters (3+ times)
        repeated_pattern = r"(.)\1{2,}"
        return re.sub(repeated_pattern, r"\1\1", text)

    def remove_special_chars(self, text: str) -> str:
        """Remove special characters that are not alphanumeric or spaces.

        Args:
            text: Input text

        Returns:
            Text with special characters removed
        """
        # Keep alphanumeric, spaces, and common punctuation
        special_pattern = r'[^\w\s.,!?;:()"\'-]'
        result = re.sub(special_pattern, "", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_html(self, text: str, force: bool = False) -> str:
        """Remove HTML tags from text.

        Args:
            text: Input text with HTML tags
            force: Force remove HTML even if remove_html flag is False

        Returns:
            Text with HTML tags removed
        """
        if not self._flags["remove_html"] and not force:
            return text

        # Pattern untuk HTML tags - replace with space to preserve word boundaries
        html_pattern = r"<[^>]+>"
        result = re.sub(html_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_emoji(self, text: str, force: bool = False) -> str:
        """Remove emoji from text.

        Args:
            text: Input text with emoji
            force: Force remove emoji even if remove_emoji flag is False

        Returns:
            Text with emoji removed
        """
        if not self._flags["remove_emoji"] and not force:
            return text

        # Pattern untuk emoji (Unicode ranges)
        # Menangkap semua karakter emoji berdasarkan Unicode blocks
        emoji_pattern = r"[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|[\U0001F780-\U0001F7FF]|[\U0001F800-\U0001F8FF]|[\U0001F900-\U0001F9FF]|[\U0001FA00-\U0001FA6F]|[\U0001FA70-\U0001FAFF]|[\U00002600-\U000026FF]|[\U00002700-\U000027BF]"
        result = re.sub(emoji_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_whitespace(self, text: str) -> str:
        """Clean whitespace characters.

        Args:
            text: Input text

        Returns:
            Text with cleaned whitespace
        """
        # Replace tabs, newlines, etc. with spaces
        text = re.sub(r"\t", " ", text)
        text = re.sub(r"\n", " ", text)
        text = re.sub(r"\r", " ", text)
        result = re.sub(r"\s+", " ", text).strip()
        return result

    def remove_emails(
        self, text: str, keep_text: bool = True, force: bool = False
    ) -> str:
        """Extract or remove email addresses from text.

        Args:
            text: Input text
            keep_text: If True, remove @ symbol from email but keep the text
                      If False, remove entire email
            force: Force cleaning even if remove_emails flag is False

        Returns:
            Text with emails processed
        """
        if not self._flags["remove_emails"] and not force:
            return text

        if keep_text:
            # Remove @ and . from emails but keep the text parts
            # More comprehensive pattern to handle various email formats
            email_pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})"
            result = re.sub(email_pattern, r"\1 \2 \3", text)
        else:
            # Remove entire email
            email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            result = re.sub(email_pattern, "", text)

        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_phones(
        self, text: str, keep_numbers: bool = True, force: bool = False
    ) -> str:
        """Extract or remove phone numbers from text.

        Args:
            text: Input text
            keep_numbers: If True, remove formatting but keep numbers
                         If False, remove entire phone number
            force: Force cleaning even if remove_phones flag is False

        Returns:
            Text with phone numbers processed
        """
        if not self._flags["remove_phones"] and not force:
            return text

        result = text
        if keep_numbers:
            # Remove phone formatting but keep numbers using regex substitution
            # Pattern to match phone numbers with formatting (more precise)
            phone_pattern = r"(\+62|62|0)([\d\-\(\)]{8,})(?=\s|$)|(\([\d]{3,4}\)\s?[\d\-\(\)]{6,})(?=\s|$)|([\+\d][\d\-\(\)]{8,})(?=\s|$)"

            def remove_phone_match(match):
                if match.group(1):  # Indonesian format (+62/62/0)
                    prefix = match.group(1)
                    numbers = re.sub(r"[\-\(\)\s]", "", match.group(2))
                    return prefix + numbers
                elif match.group(3):  # Parenthetical format like (021) 123-4567
                    numbers = re.sub(r"[\-\(\)\s]", "", match.group(3))
                    return numbers
                else:  # International format
                    numbers = re.sub(r"[\-\(\)\s]", "", match.group(4))
                    return numbers

            result = re.sub(phone_pattern, remove_phone_match, text)
        else:
            # Remove entire phone numbers
            phone_pattern = r"[\+]?[\d\-\(\)\s]{8,}\d"
            result = re.sub(phone_pattern, "", text)

        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_currency(
        self, text: str, keep_numbers: bool = True, force: bool = False
    ) -> str:
        """Clean currency symbols from text.

        Args:
            text: Input text
            keep_numbers: If True, remove currency symbols but keep numbers
                         If False, remove entire currency mentions
            force: Force cleaning even if remove_currency flag is False

        Returns:
            Text with currency processed
        """
        if not self._flags["remove_currency"] and not force:
            return text

        if keep_numbers:
            # Remove currency symbols but keep numbers
            currency_pattern = r"([$€£¥₹Rp\.,])(\d+(?:[\.,]\d+)*)"
            result = re.sub(currency_pattern, r"\2", text)
        else:
            # Remove entire currency mentions
            currency_pattern = r"[$€£¥₹Rp\.,]?\d+(?:[\.,]\d+)*[$€£¥₹Rp]?"
            result = re.sub(currency_pattern, "", text)

        result = re.sub(r"\s+", " ", result).strip()
        return result

    def remove_numbers(self, text: str, force: bool = False) -> str:
        """Remove numbers from text.

        Args:
            text: Input text
            force: Force remove numbers even if remove_numbers flag is False

        Returns:
            Text with numbers removed
        """
        if not self._flags["remove_numbers"] and not force:
            return text

        # Pattern untuk numbers - replace with space to preserve word boundaries
        number_pattern = r"\d+"
        result = re.sub(number_pattern, " ", text)
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def get_options(self) -> dict:
        """Get current cleaning options.

        Returns:
            Dictionary of current options
        """
        return dict(self._flags)
