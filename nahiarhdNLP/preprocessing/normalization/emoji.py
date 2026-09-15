"""
Emoji normalizer for Indonesian text processing.
"""

import re
from typing import Dict, List

from nahiarhdNLP.datasets.loaders import DatasetLoader


class EmojiConverter:
    """Converter for emoji to Indonesian text and vice versa."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize emoji converter.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.language = language
        self.emoji_to_text: Dict[str, str] = {}
        self.text_to_emoji: Dict[str, str] = {}
        self.emoji_data: List[Dict] = []

    def _load_data(self):
        """Load emoji data dari CSV."""
        try:
            loader = DatasetLoader()
            dataset = loader.load_emoji_dataset(language=self.language)

            self.emoji_data = dataset

            # Build emoji to text mapping
            for item in dataset:
                emoji = item.get("emoji", "")
                name_id = item.get("name_id", "")
                alias = item.get("alias", "")

                if emoji and name_id:
                    self.emoji_to_text[emoji] = name_id

                # Also map alias to emoji for reverse conversion
                if emoji and alias:
                    self.text_to_emoji[alias.lower()] = emoji

                # Add name_id to reverse mapping
                if emoji and name_id:
                    self.text_to_emoji[name_id.lower()] = emoji

                # Add individual alias words
                aliases = item.get("aliases", [])
                if isinstance(aliases, list):
                    for alias_word in aliases:
                        if alias_word and emoji:
                            self.text_to_emoji[alias_word.lower()] = emoji

        except OSError:
            self.emoji_data = []
            self.emoji_to_text = {}
            self.text_to_emoji = {}

    def emoji_to_text_convert(self, text: str) -> str:
        """Convert emoji to Indonesian text."""
        if not text:
            return text

        result = text
        for emoji, indonesia_text in self.emoji_to_text.items():
            # Replace emoji with Indonesian text
            result = result.replace(emoji, f" {indonesia_text} ")

        # Clean up extra spaces
        result = re.sub(r"\s+", " ", result).strip()
        return result

    def text_to_emoji_convert(self, text: str) -> str:
        """Convert Indonesian text to emoji.

        Args:
            text: Text containing Indonesian emoji descriptions

        Returns:
            Text with Indonesian emoji descriptions converted to emojis
        """
        if not text:
            return text

        result = text
        # Sort by length (longest first) to avoid partial matches
        sorted_texts = sorted(
            self.text_to_emoji.items(), key=lambda x: len(x[0]), reverse=True
        )

        for indonesia_text, emoji in sorted_texts:
            # Case insensitive replacement
            pattern = r"\b" + re.escape(indonesia_text) + r"\b"
            result = re.sub(pattern, emoji, result, flags=re.IGNORECASE)

        return result
