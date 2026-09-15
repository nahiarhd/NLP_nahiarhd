"""TextCleaner instance methods must stay callable after __init__."""

from nahiarhdNLP.preprocessing.cleaning.text_cleaner import TextCleaner
from nahiarhdNLP.preprocessing.cleaning.text_cleaner_word import TextCleanerWord
from nahiarhdNLP.preprocessing.cleaning.text_replace import TextReplace


def test_remove_urls_is_callable_on_instance():
    cleaner = TextCleaner()
    result = cleaner.remove_urls("visit https://example.com please")
    assert "https://" not in result
    assert "visit" in result
    assert "please" in result


def test_remove_mentions_is_callable_on_instance():
    cleaner = TextCleaner()
    result = cleaner.remove_mentions("hello @user and friends")
    assert "@user" not in result
    assert "hello" in result
    assert "friends" in result


def test_get_options_returns_booleans_not_methods():
    options = TextCleaner().get_options()
    assert options["remove_urls"] is True
    assert options["remove_emoji"] is False
    assert all(isinstance(v, bool) for v in options.values())


def test_clean_html_is_callable_on_word_cleaner():
    cleaner = TextCleanerWord()
    result = cleaner.clean_html("<p>Hello <b>World</b></p>")
    assert "<" not in result
    assert "Hello" in result
    assert "World" in result


def test_replace_email_is_callable_on_instance():
    replacer = TextReplace()
    result = replacer.replace_email("mail me at john.doe@gmail.com thanks")
    assert result == "mail me at <email> thanks"
