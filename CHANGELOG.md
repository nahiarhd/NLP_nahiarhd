# Changelog

## [1.6.2] - 2026-09-15

### Changed
- GitHub repository renamed from `NLP_nahiarhd` to `nahiarhdNLP`

## [1.6.1] - 2026-09-15

### Fixed
- Project URLs, CI badge, and clone path now point at `nahiarhd/NLP_nahiarhd`

## [1.6.0] - 2026-09-15

### Added
- `Pipeline.social()`, `Pipeline.formal()`, and `Pipeline.anonymize()` presets
- CI on Python 3.10–3.13
- Real unit tests under `tests/`
- `py.typed` marker for inline type information

### Changed
- Requires Python >= 3.10 (3.8 and 3.9 are end-of-life)
- Runtime dependency is PySastrawi only; pandas and rich are gone
- Tokenizer splits punctuation and keeps emails, URLs, mentions, and hashtags
- Spell/stopword lookups use sets

### Fixed
- `TextCleaner` / `TextReplace` methods were overwritten by boolean flags
- Emoji aliases were parsed with `eval`
- `tokenizer` in the middle of a pipeline raised a cryptic TypeError

### Removed
- Unused `kamus.txt` and `kata_dasar_kbbi.csv` from the wheel
