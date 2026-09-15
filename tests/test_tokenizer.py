"""Tokenizer keeps emails/URLs as tokens and splits punctuation."""

import pytest

from nahiarhdNLP.preprocessing import Pipeline
from nahiarhdNLP.preprocessing.tokenization.tokenizer import Tokenizer


def test_tokenize_plain_words_splits_on_whitespace():
    assert Tokenizer().tokenize("satu dua tiga") == ["satu", "dua", "tiga"]


def test_tokenize_empty_returns_empty_list():
    assert Tokenizer().tokenize("") == []


def test_tokenize_splits_punctuation_from_words():
    assert Tokenizer().tokenize("Halo, dunia!") == ["Halo", ",", "dunia", "!"]


def test_tokenize_keeps_email_and_url_as_single_tokens():
    tokens = Tokenizer().tokenize(
        "kirim ke test@example.com atau https://example.com/docs"
    )
    assert "test@example.com" in tokens
    assert "https://example.com/docs" in tokens


def test_tokenize_keeps_mentions_and_hashtags():
    tokens = Tokenizer().tokenize("halo @john_doe #NLP")
    assert "@john_doe" in tokens
    assert "#NLP" in tokens


def test_tokenize_keeps_hyphenated_indonesian_words():
    assert "aba-aba" in Tokenizer().tokenize("beri aba-aba")


def test_tokenizer_must_be_the_last_pipeline_step():
    with pytest.raises(TypeError, match="tokenizer must be the last"):
        Pipeline({"tokenizer": True, "clean_html": True}).process("satu dua")
