"""
Main functions for preprocessing Indonesian text.
"""

# Import kelas-kelas yang sudah ada
from .cleaning.text_cleaner import TextCleaner
from .cleaning.text_cleaner_word import TextCleanerWord as WordTextCleaner
from .cleaning.text_replace import TextReplace
from .linguistic.stemmer import Stemmer
from .linguistic.stopword import StopwordRemover
from .normalization.emoji import EmojiConverter
from .normalization.spell_corrector import SpellCorrector
from .tokenization.tokenizer import Tokenizer

# Inisialisasi instance global untuk fungsi-fungsi utility (lazy loading)
_text_cleaner = None
_text_cleaner_word = None
_text_replace = None
_stemmer = None
_stopword = None
_emoji = None
_spell_corrector = None
_tokenizer = None


def _get_text_cleaner():
    global _text_cleaner
    if _text_cleaner is None:
        _text_cleaner = TextCleaner()
    return _text_cleaner


def _get_text_cleaner_word():
    global _text_cleaner_word
    if _text_cleaner_word is None:
        _text_cleaner_word = WordTextCleaner()
    return _text_cleaner_word


def _get_text_replace():
    global _text_replace
    if _text_replace is None:
        _text_replace = TextReplace()
    return _text_replace


def _get_stemmer():
    global _stemmer
    if _stemmer is None:
        _stemmer = Stemmer()
    return _stemmer


def _get_stopword():
    global _stopword
    if _stopword is None:
        _stopword = StopwordRemover()
        _stopword._load_data()
    return _stopword


def _get_emoji():
    global _emoji
    if _emoji is None:
        _emoji = EmojiConverter()
        _emoji._load_data()
    return _emoji


def _get_spell_corrector():
    global _spell_corrector
    if _spell_corrector is None:
        _spell_corrector = SpellCorrector()
    return _spell_corrector


def _get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = Tokenizer()
    return _tokenizer


class Pipeline:
    """
    Pipeline config-only: hanya menerima dict config {step_name: True/False}.
    """

    def __init__(self, config: dict):
        if not isinstance(config, dict):
            raise TypeError("config must be a dict of {step_name: True/False}")
        self.config = config
        self.functions = tuple()
        self._build_functions_from_config()

    @classmethod
    def social(cls):
        """Clean social posts: keep usernames/tags, drop URLs and HTML."""
        return cls(
            {
                "clean_html": True,
                "clean_mentions": True,
                "clean_hashtags": True,
                "remove_urls": True,
                "remove_extra_spaces": True,
                "remove_repeated_chars": True,
            }
        )

    @classmethod
    def formal(cls):
        """Normalize prose for classical NLP: lower, stopwords, stem."""
        return cls(
            {
                "clean_html": True,
                "remove_urls": True,
                "remove_emoji": True,
                "remove_punctuation": True,
                "remove_lowercase": True,
                "remove_extra_spaces": True,
                "stopword": True,
                "stem": True,
            }
        )

    @classmethod
    def anonymize(cls):
        """Replace emails, URLs, and mentions with placeholders."""
        return cls(
            {
                "clean_html": True,
                "replace_email": True,
                "replace_link": True,
                "replace_user": True,
                "remove_phones": True,
            }
        )

    def _build_functions_from_config(self):

        # mapping step -> callable (internal only)
        # Use class methods bound at call-time to avoid instance attributes shadowing methods
        function_mapping = {
            "remove_html": lambda t, _m=TextCleaner.remove_html: _m(
                _get_text_cleaner(), t
            ),
            "remove_urls": lambda t, _m=TextCleaner.remove_urls: _m(
                _get_text_cleaner(), t
            ),
            "remove_mentions": lambda t, _m=TextCleaner.remove_mentions: _m(
                _get_text_cleaner(), t
            ),
            "remove_hashtags": lambda t, _m=TextCleaner.remove_hashtags: _m(
                _get_text_cleaner(), t
            ),
            "remove_punctuation": lambda t, _m=TextCleaner.remove_punctuation: _m(
                _get_text_cleaner(), t, force=True
            ),
            "remove_emoji": lambda t, _m=TextCleaner.remove_emoji: _m(
                _get_text_cleaner(), t, force=True
            ),
            "remove_lowercase": lambda t, _m=TextCleaner.remove_lowercase: _m(
                _get_text_cleaner(), t
            ),
            "remove_extra_spaces": lambda t, _m=TextCleaner.remove_extra_spaces: _m(
                _get_text_cleaner(), t
            ),
            "remove_repeated_chars": lambda t, _m=TextCleaner.remove_repeated_chars: _m(
                _get_text_cleaner(), t
            ),
            "remove_special_chars": lambda t, _m=TextCleaner.remove_special_chars: _m(
                _get_text_cleaner(), t
            ),
            "remove_whitespace": lambda t, _m=TextCleaner.remove_whitespace: _m(
                _get_text_cleaner(), t
            ),
            "remove_emails": lambda t, _m=TextCleaner.remove_emails: _m(
                _get_text_cleaner(), t, keep_text=False, force=True
            ),
            "remove_phones": lambda t, _m=TextCleaner.remove_phones: _m(
                _get_text_cleaner(), t, keep_numbers=False, force=True
            ),
            "remove_currency": lambda t, _m=TextCleaner.remove_currency: _m(
                _get_text_cleaner(), t, keep_numbers=False, force=True
            ),
            "remove_numbers": lambda t, _m=TextCleaner.remove_numbers: _m(
                _get_text_cleaner(), t, force=True
            ),
            "clean_urls": lambda t, _m=WordTextCleaner.clean_urls: _m(
                _get_text_cleaner_word(), t
            ),
            "clean_mentions": lambda t, _m=WordTextCleaner.clean_mentions: _m(
                _get_text_cleaner_word(), t
            ),
            "clean_hashtags": lambda t, _m=WordTextCleaner.clean_hashtags: _m(
                _get_text_cleaner_word(), t
            ),
            "clean_html": lambda t, _m=WordTextCleaner.clean_html: _m(
                _get_text_cleaner_word(), t
            ),
            "replace_email": lambda t, _m=TextReplace.replace_email: _m(
                _get_text_replace(), t
            ),
            "replace_link": lambda t, _m=TextReplace.replace_link: _m(
                _get_text_replace(), t
            ),
            "replace_user": lambda t, _m=TextReplace.replace_user: _m(
                _get_text_replace(), t
            ),
            "stem": lambda t, _m=Stemmer.stem: _m(_get_stemmer(), t),
            "stopword": lambda t, _m=StopwordRemover.remove_stopwords: _m(
                _get_stopword(), t
            ),
            "emoji_to_text": lambda t, _m=EmojiConverter.emoji_to_text_convert: _m(
                _get_emoji(), t
            ),
            "text_to_emoji": lambda t, _m=EmojiConverter.text_to_emoji_convert: _m(
                _get_emoji(), t
            ),
            "spell_corrector_word": lambda t, _m=SpellCorrector.correct_word: _m(
                _get_spell_corrector(), t
            ),
            "spell_corrector_sentence": lambda t, _m=SpellCorrector.correct_sentence: _m(
                _get_spell_corrector(), t
            ),
            "tokenizer": lambda t, _m=Tokenizer.tokenize: _m(_get_tokenizer(), t),
        }

        functions = []
        unknown_steps = []

        for key, enabled in self.config.items():
            if not enabled:
                continue

            func = function_mapping.get(key)

            if func is None:
                unknown_steps.append(key)
                continue

            functions.append(func)

        if unknown_steps:
            raise ValueError(
                f"Unknown preprocessing steps: {unknown_steps}. "
                f"Available: {sorted(function_mapping.keys())}"
            )

        self.functions = tuple(functions)

    def process(self, text: str):
        if not text:
            return text
        result = text
        last_index = len(self.functions) - 1
        for i, func in enumerate(self.functions):
            result = func(result)
            if i != last_index and not isinstance(result, str):
                raise TypeError("tokenizer must be the last pipeline step")
        return result

    def update_config(self, new_config: dict) -> None:
        if not isinstance(new_config, dict):
            raise TypeError("new_config must be dict {step_name: True/False}")
        self.config.update(new_config)
        self._build_functions_from_config()

    def get_enabled_steps(self) -> list:
        return [k for k, v in self.config.items() if v]

    @staticmethod
    def get_available_steps() -> dict:
        """Get all available preprocessing steps with their descriptions.

        Returns:
            dict: Dictionary mapping step names to their descriptions
        """
        return {
            # Text Cleaning - HTML & Tags
            "clean_html": "Remove HTML tags from text",
            # Text Cleaning - URLs
            "remove_urls": "Remove complete URLs from text",
            "clean_urls": "Remove URL protocols (http://, https://) but keep domain",
            # Text Cleaning - Social Media
            "remove_mentions": "Remove @mentions completely",
            "clean_mentions": "Remove @ symbol but keep username",
            "remove_hashtags": "Remove #hashtags completely",
            "clean_hashtags": "Remove # symbol but keep tag text",
            # Text Cleaning - Content Removal
            "remove_emoji": "Remove all emoji characters",
            "remove_punctuation": "Remove punctuation marks",
            "remove_numbers": "Remove all numbers",
            "remove_emails": "Remove email addresses",
            "remove_phones": "Remove phone numbers",
            "remove_currency": "Remove currency symbols",
            # Text Cleaning - Text Normalization
            "remove_special_chars": "Remove special characters",
            "remove_extra_spaces": "Normalize whitespace (multiple spaces to single)",
            "remove_repeated_chars": "Normalize repeated characters (e.g., 'haiiii' → 'haii')",
            "remove_whitespace": "Clean tabs, newlines, carriage returns",
            "remove_lowercase": "Convert text to lowercase",
            # Text Normalization
            "emoji_to_text": "Convert emojis to text descriptions",
            "text_to_emoji": "Convert text descriptions to emojis",
            "spell_corrector_word": "Correct spelling and slang for single words",
            "spell_corrector_sentence": "Correct spelling and slang for entire sentences",
            # Linguistic Processing
            "stem": "Apply Indonesian stemming (reduce to root form)",
            "stopword": "Remove Indonesian stopwords",
            "tokenizer": "Tokenize text into list of tokens",
            # Text Replacement
            "replace_email": "Replace email addresses with <email> token",
            "replace_link": "Replace URLs with <link> token",
            "replace_user": "Replace @mentions with <user> token",
        }

    @staticmethod
    def get_available_steps_by_category() -> dict:
        """Get all available preprocessing steps organized by category.

        Returns:
            dict: Dictionary mapping categories to lists of step names
        """
        return {
            "text_cleaning_html": ["clean_html"],
            "text_cleaning_urls": ["remove_urls", "clean_urls"],
            "text_cleaning_social": [
                "remove_mentions",
                "clean_mentions",
                "remove_hashtags",
                "clean_hashtags",
            ],
            "text_cleaning_content": [
                "remove_emoji",
                "remove_punctuation",
                "remove_numbers",
                "remove_emails",
                "remove_phones",
                "remove_currency",
            ],
            "text_cleaning_normalization": [
                "remove_special_chars",
                "remove_extra_spaces",
                "remove_repeated_chars",
                "remove_whitespace",
                "remove_lowercase",
            ],
            "text_normalization": [
                "emoji_to_text",
                "text_to_emoji",
                "spell_corrector_word",
                "spell_corrector_sentence",
            ],
            "linguistic_processing": ["stem", "stopword", "tokenizer"],
            "text_replacement": ["replace_email", "replace_link", "replace_user"],
        }

    def __call__(self, text: str):
        return self.process(text)

    def __repr__(self) -> str:
        return f"Pipeline(config={self.get_enabled_steps()})"
