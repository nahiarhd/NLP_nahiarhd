"""Spell correction: slang first, then exact wordlist membership."""

from nahiarhdNLP.preprocessing.normalization.spell_corrector import SpellCorrector


def test_correct_word_expands_slang():
    spell = SpellCorrector()
    assert spell.correct_word("yg") == "yang"
    assert spell.correct_word("gk") == "tidak"
    assert spell.correct_word("tdk") == "tidak"


def test_correct_word_keeps_known_wordlist_entry():
    spell = SpellCorrector()
    assert spell.correct_word("gadisnya") == "gadisnya"


def test_correct_sentence_preserves_trailing_punctuation():
    spell = SpellCorrector()
    assert spell.correct_sentence("yg gk?") == "yang tidak?"
