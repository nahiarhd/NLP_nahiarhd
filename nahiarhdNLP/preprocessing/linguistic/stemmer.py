"""
Stemmer for Indonesian text (menggunakan Sastrawi).
"""

try:
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

    _sastrawi_available = True
except ImportError:
    _sastrawi_available = False


class Stemmer:
    """Stemming kata bahasa Indonesia menggunakan Sastrawi."""

    def __init__(self):
        if not _sastrawi_available:
            raise ImportError(
                "Sastrawi belum terinstall. Install dengan: pip install PySastrawi"
            )
        factory = StemmerFactory()
        self.stemmer = factory.create_stemmer()

    def stem(self, text: str) -> str:
        return self.stemmer.stem(text) if text else text
