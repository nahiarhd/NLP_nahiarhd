"""DatasetLoader: CSV via stdlib, aliases parsed as literals only."""

from pathlib import Path

from nahiarhdNLP.datasets.loaders import DatasetLoader


def test_load_stopwords_includes_known_words():
    words = DatasetLoader().load_stopwords_dataset()
    assert "adalah" in words
    assert "akan" in words
    assert all(isinstance(w, str) for w in words)


def test_load_slang_maps_yg_to_yang():
    rows = DatasetLoader().load_slang_dataset()
    mapping = {row["slang"]: row["formal"] for row in rows}
    assert mapping["yg"] == "yang"
    assert mapping["gk"] == "tidak"


def test_load_emoji_aliases_are_a_list_of_strings():
    rows = DatasetLoader().load_emoji_dataset()
    grinning = next(row for row in rows if row["emoji"] == "😀")
    assert grinning["name_id"] == "wajah_gembira"
    assert grinning["aliases"] == ["wajah", "gembira", "bahagia", "muka", "senang"]


def test_load_wordlist_is_a_non_empty_sequence_of_strings():
    words = DatasetLoader().load_wordlist_dataset()
    assert len(words) > 1000
    assert "gadisnya" in words


def test_emoji_aliases_do_not_execute_python(tmp_path: Path):
    (tmp_path / "emoji.csv").write_text(
        "emoji,name_id,alias,aliases\n"
        "😀,wajah_gembira,wajah,\"__import__('sys')\"\n",
        encoding="utf-8",
    )
    rows = DatasetLoader(datasets_dir=tmp_path).load_emoji_dataset()
    assert rows[0]["aliases"] == []
