"""
Spell corrector untuk Bahasa Indonesia menggunakan DatasetLoader.
"""

import difflib

from nahiarhdNLP.datasets.loaders import DatasetLoader


class SpellCorrector:
    """Spell correction untuk bahasa Indonesia menggunakan DatasetLoader."""

    def __init__(self):
        self.slang_dict = {}
        self.wordlist = set()
        self._load_data()

    def _load_data(self):
        """Load slang dictionary dan wordlist menggunakan DatasetLoader."""
        loader = DatasetLoader()
        slang_data = loader.load_slang_dataset()
        self.slang_dict = {item["slang"]: item["formal"] for item in slang_data}
        self.wordlist = set(loader.load_wordlist_dataset())

    def correct_word(self, word: str) -> str:
        """Koreksi satu kata."""
        if not word or len(word) < 2:
            return word

        word_lower = word.lower()

        # 1. Cek di slang dictionary dulu (prioritas tertinggi)
        if word_lower in self.slang_dict:
            return self.slang_dict[word_lower]

        # 2. Cek apakah kata sudah benar di wordlist
        if word_lower in self.wordlist:
            return word

        # 3. Cari kata yang mirip di wordlist
        if self.wordlist:
            matches = difflib.get_close_matches(
                word_lower, self.wordlist, n=1, cutoff=0.6
            )
            if matches:
                return matches[0]

        # 4. Jika tidak ada yang cocok, kembalikan kata asli
        return word

    def correct_sentence(self, sentence: str) -> str:
        """Koreksi kalimat (kata per kata)."""
        if not sentence:
            return sentence

        words = sentence.split()
        corrected_words = []

        for word in words:
            # Pisahkan tanda baca dari kata
            punctuation = ""
            clean_word = word

            # Ambil tanda baca di akhir kata
            while clean_word and clean_word[-1] in ".,!?;:":
                punctuation = clean_word[-1] + punctuation
                clean_word = clean_word[:-1]

            # Koreksi kata bersih
            if clean_word:
                corrected_word = self.correct_word(clean_word)
                corrected_words.append(corrected_word + punctuation)
            else:
                corrected_words.append(word)

        return " ".join(corrected_words)
