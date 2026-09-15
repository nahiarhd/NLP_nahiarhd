import ast
import csv
import json
from pathlib import Path


def _parse_aliases(raw):
    """Parse the aliases CSV cell as a Python list literal.

    Source: https://docs.python.org/3/library/ast.html#ast.literal_eval
    """
    if not raw or raw.strip() in {"nan"}:
        return []
    try:
        parsed = ast.literal_eval(raw)
    except (ValueError, SyntaxError):
        return []
    if isinstance(parsed, list):
        return [str(item) for item in parsed if item]
    return []


class DatasetLoader:
    """Loader untuk dataset NLP Indonesia dari file CSV/JSON lokal."""

    def __init__(self, datasets_dir=None):
        self.datasets_dir = Path(datasets_dir) if datasets_dir is not None else Path(__file__).parent

    def _open_csv(self, filename):
        # newline="" is required so the csv module handles embedded newlines.
        # Source: https://docs.python.org/3/library/csv.html#csv.reader
        path = self.datasets_dir / filename
        return path.open(newline="", encoding="utf-8")

    def load_stopwords_dataset(self, language="indonesian"):
        """Load stopwords dari CSV."""
        del language
        try:
            with self._open_csv("stop_word.csv") as handle:
                reader = csv.DictReader(handle)
                return [
                    row["stopword"]
                    for row in reader
                    if row.get("stopword")
                ]
        except OSError:
            return []

    def load_slang_dataset(self, language="indonesian"):
        """Load slang dari CSV."""
        del language
        try:
            with self._open_csv("slang.csv") as handle:
                reader = csv.DictReader(handle)
                data = []
                for row in reader:
                    slang_val = row.get("slang")
                    formal_val = row.get("formal")
                    if slang_val and formal_val:
                        data.append({"slang": slang_val, "formal": formal_val})
                return data
        except OSError:
            return []

    def load_emoji_dataset(self, language="indonesian"):
        """Load emoji dari CSV."""
        del language
        try:
            with self._open_csv("emoji.csv") as handle:
                reader = csv.DictReader(handle)
                data = []
                for row in reader:
                    data.append(
                        {
                            "emoji": row.get("emoji") or "",
                            "name_id": row.get("name_id") or "",
                            "alias": row.get("alias") or "",
                            "aliases": _parse_aliases(row.get("aliases") or ""),
                        }
                    )
                return data
        except OSError:
            return []

    def load_wordlist_dataset(self, language="indonesian"):
        """Load wordlist dari JSON."""
        del language
        json_path = self.datasets_dir / "wordlist.json"
        try:
            with json_path.open(encoding="utf-8") as handle:
                data = json.load(handle)
            return data if isinstance(data, list) else []
        except (OSError, json.JSONDecodeError):
            return []
