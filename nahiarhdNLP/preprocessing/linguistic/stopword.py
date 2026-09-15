"""
Stopword remover for Indonesian text processing.
"""

import re

from nahiarhdNLP.datasets.loaders import DatasetLoader


class StopwordRemover:
    """Remove stopwords from Indonesian text."""

    def __init__(self, language: str = "indonesian", **kwargs):
        """Initialize stopword remover.

        Args:
            language: Language code
            **kwargs: Additional arguments
        """
        self.language = language
        self.stopwords: set = set()

    def _load_data(self):
        """Load stopwords data dari CSV."""
        loader = DatasetLoader()
        self.stopwords = set(loader.load_stopwords_dataset(language=self.language))

    def is_stopword(self, word: str) -> bool:
        """Check if a word is a stopword."""
        return word.lower() in self.stopwords

    def remove_stopwords(self, text: str) -> str:
        """Remove stopwords from text."""
        if not text:
            return text

        # Split text into words
        words = text.split()

        # Filter out stopwords
        filtered_words = []
        for word in words:
            # Clean word (remove punctuation)
            clean_word = re.sub(r"[^\w\s]", "", word)
            if clean_word and not self.is_stopword(clean_word):
                filtered_words.append(word)
            elif not clean_word:  # Keep punctuation-only words
                filtered_words.append(word)

        result = " ".join(filtered_words)
        # Bersihkan spasi ganda
        result = re.sub(r"\s+", " ", result).strip()
        return result
