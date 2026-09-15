"""Named pipeline presets encode common Indonesian preprocessing jobs."""

from nahiarhdNLP.preprocessing import Pipeline


def test_social_keeps_username_text_and_drops_urls():
    result = Pipeline.social().process(
        "Hai @teman cek https://example.com #NLP"
    )
    assert "https://" not in result
    assert "@" not in result
    assert "#" not in result
    assert "teman" in result
    assert "NLP" in result


def test_anonymize_replaces_email_link_and_mention():
    result = Pipeline.anonymize().process(
        "hubungi john@example.com atau @admin di https://site.com"
    )
    assert "<email>" in result
    assert "<user>" in result
    assert "<link>" in result
    assert "john@example.com" not in result
    assert "https://site.com" not in result


def test_formal_lowercases_and_removes_stopwords():
    result = Pipeline.formal().process("Saya sedang belajar pemrograman")
    assert result == result.lower()
    assert "saya" not in result.split()
    assert "sedang" not in result.split()
    assert "belajar" in result or "ajar" in result
