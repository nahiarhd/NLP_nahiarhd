<div align="center">

# 🇮🇩 nahiarhdNLP

### Advanced Indonesian Natural Language Processing Library

[![CI](https://github.com/nahiarhd/NLP_nahiarhd/actions/workflows/ci.yml/badge.svg)](https://github.com/nahiarhd/NLP_nahiarhd/actions)
[![PyPI version](https://img.shields.io/pypi/v/nahiarhdNLP.svg)](https://pypi.org/project/nahiarhdNLP/)
[![Python Version](https://img.shields.io/pypi/pyversions/nahiarhdNLP.svg)](https://pypi.org/project/nahiarhdNLP/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/nahiarhdNLP.svg)](https://pypi.org/project/nahiarhdNLP/)

**Lightweight, powerful, and easy-to-use Indonesian text preprocessing library**

[Installation](#-installation) • [Quick Start](#-quick-start) • [Features](#-features) • [Examples](#-comprehensive-examples) • [Documentation](#-api-documentation)

</div>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Features](#-features)
- [Comprehensive Examples](#-comprehensive-examples)
  - [Pipeline Configuration](#1-pipeline-configuration)
  - [Text Cleaning](#2-text-cleaning)
  - [Text Normalization](#3-text-normalization)
  - [Linguistic Processing](#4-linguistic-processing)
  - [Text Replacement](#5-text-replacement)
  - [Dataset Loaders](#6-dataset-loaders)
- [Pipeline Configuration Options](#-pipeline-configuration-options)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**nahiarhdNLP** adalah library Python yang dirancang khusus untuk preprocessing teks Bahasa Indonesia. Library ini menyediakan berbagai fungsi untuk membersihkan, menormalisasi, dan memproses teks dengan mudah dan efisien.

### ✨ Key Features

- 🔧 **Configurable Pipeline** - Build custom text processing workflows
- 🧹 **Comprehensive Text Cleaning** - Remove HTML, URLs, mentions, hashtags, emojis, and more
- 📝 **Text Normalization** - Emoji conversion, spell correction, slang normalization
- 🔤 **Linguistic Processing** - Stemming, stopword removal, tokenization
- 🔄 **Text Replacement** - Replace emails, links, and mentions with tokens
- 📊 **Built-in Datasets** - Indonesian stopwords, slang dictionary, emoji mappings
- ⚡ **High Performance** - Lazy loading and optimized processing
- 🎯 **Easy to Use** - Simple, intuitive API

---

## 📦 Installation

### Using pip

```bash
pip install nahiarhdNLP
```

### From source

```bash
git clone https://github.com/nahiarhd/NLP_nahiarhd.git
cd nahiarhdNLP
pip install -e .
```

### Requirements

- Python >= 3.10
- PySastrawi >= 1.2.0

---

## 🚀 Quick Start

```python
from nahiarhdNLP.preprocessing import Pipeline

# Create a pipeline with configuration
config = {
    "clean_html": True,
    "clean_mentions": True,
    "remove_urls": True,
    "stopword": True
}

pipeline = Pipeline(config)

# Process text
text = "Haii @user!! Cek website kita di https://example.com ya 😊"
result = pipeline.process(text)

print(result)
# Output: "Haii Cek website kita ya 😊"
```

Named presets for the three jobs people actually run:

```python
from nahiarhdNLP.preprocessing import Pipeline

Pipeline.social().process("Hai @teman cek https://example.com #NLP")
Pipeline.formal().process("Saya sedang belajar pemrograman")
Pipeline.anonymize().process("hubungi john@example.com atau @admin")
```

---

## 🎯 Features

### 🧹 Text Cleaning

| Feature                  | Description                | Config Key              |
| ------------------------ | -------------------------- | ----------------------- |
| **HTML Removal**         | Remove HTML tags           | `clean_html`            |
| **URL Removal**          | Remove complete URLs       | `remove_urls`           |
| **URL Cleaning**         | Remove URL protocols only  | `clean_urls`            |
| **Mention Removal**      | Remove @mentions           | `remove_mentions`       |
| **Mention Cleaning**     | Remove @ but keep username | `clean_mentions`        |
| **Hashtag Removal**      | Remove #hashtags           | `remove_hashtags`       |
| **Hashtag Cleaning**     | Remove # but keep tag text | `clean_hashtags`        |
| **Emoji Removal**        | Remove all emojis          | `remove_emoji`          |
| **Punctuation Removal**  | Remove punctuation marks   | `remove_punctuation`    |
| **Number Removal**       | Remove all numbers         | `remove_numbers`        |
| **Email Removal**        | Remove email addresses     | `remove_emails`         |
| **Phone Removal**        | Remove phone numbers       | `remove_phones`         |
| **Currency Removal**     | Remove currency symbols    | `remove_currency`       |
| **Special Char Removal** | Remove special characters  | `remove_special_chars`  |
| **Extra Spaces**         | Normalize whitespace       | `remove_extra_spaces`   |
| **Repeated Chars**       | Normalize repeated chars   | `remove_repeated_chars` |
| **Whitespace Cleaning**  | Clean tabs, newlines, etc. | `remove_whitespace`     |

### 📝 Text Normalization

| Feature                         | Description                              | Config Key                 |
| ------------------------------- | ---------------------------------------- | -------------------------- |
| **Emoji to Text**               | Convert emojis to text                   | `emoji_to_text`            |
| **Text to Emoji**               | Convert text to emojis                   | `text_to_emoji`            |
| **Spell Correction (Word)**     | Correct spelling & slang (single word)   | `spell_corrector_word`     |
| **Spell Correction (Sentence)** | Correct spelling & slang (full sentence) | `spell_corrector_sentence` |
| **Lowercase**                   | Convert to lowercase                     | `remove_lowercase`         |

### 🔤 Linguistic Processing

| Feature              | Description                 | Config Key  |
| -------------------- | --------------------------- | ----------- |
| **Stemming**         | Reduce words to root form   | `stem`      |
| **Stopword Removal** | Remove Indonesian stopwords | `stopword`  |
| **Tokenization**     | Split text into tokens      | `tokenizer` |

### 🔄 Text Replacement

| Feature               | Description                    | Config Key      |
| --------------------- | ------------------------------ | --------------- |
| **Email Replacement** | Replace emails with `<email>`  | `replace_email` |
| **Link Replacement**  | Replace URLs with `<link>`     | `replace_link`  |
| **User Replacement**  | Replace mentions with `<user>` | `replace_user`  |

---

## 💡 Comprehensive Examples

### 1. Pipeline Configuration

#### Example 1.1: Basic Pipeline

```python
from nahiarhdNLP.preprocessing import Pipeline

# Configure pipeline
config = {
    "clean_html": True,
    "clean_mentions": True,
    "remove_urls": True
}

pipeline = Pipeline(config)

# Input
text = "Hello <b>World</b>! Mention @user123 and visit https://example.com"

# Process
result = pipeline.process(text)

print(f"Input : {text}")
print(f"Output: {result}")
```

**Output:**

```
Input : Hello <b>World</b>! Mention @user123 and visit https://example.com
Output: Hello World! Mention user123 and visit
```

#### Example 1.2: Social Media Text Cleaning

```python
from nahiarhdNLP.preprocessing import Pipeline

config = {
    "clean_html": True,
    "clean_mentions": True,
    "clean_hashtags": True,
    "remove_urls": True,
    "remove_emoji": True,
    "remove_extra_spaces": True
}

pipeline = Pipeline(config)

# Input - Typical social media post
text = """
Haiii gengs!! 😍😍
Jangan lupa follow @nahiarhdNLP ya!
Cek website kita di https://github.com/nahiarhd
#NLP #IndonesianNLP #TextProcessing 🚀
"""

result = pipeline.process(text)

print("=" * 60)
print("INPUT:")
print(text)
print("=" * 60)
print("OUTPUT:")
print(result)
print("=" * 60)
```

**Output:**

```
============================================================
INPUT:

Haiii gengs!! 😍😍
Jangan lupa follow @nahiarhdNLP ya!
Cek website kita di https://github.com/nahiarhd
#NLP #IndonesianNLP #TextProcessing 🚀

============================================================
OUTPUT:
Haiii gengs!! Jangan lupa follow nahiarhdNLP ya! Cek website kita di NLP IndonesianNLP TextProcessing
============================================================
```

#### Example 1.3: Update Pipeline Configuration

```python
from nahiarhdNLP.preprocessing import Pipeline

# Initial configuration
config = {"clean_html": True, "remove_urls": True}
pipeline = Pipeline(config)

text = "<p>Visit https://example.com for more info</p>"

print(f"Initial Output: {pipeline.process(text)}")
# Output: Visit for more info

# Update configuration
pipeline.update_config({"remove_punctuation": True})

print(f"Updated Output: {pipeline.process(text)}")
# Output: Visit for more info

# Check enabled steps
print(f"Enabled steps: {pipeline.get_enabled_steps()}")
# Output: ['clean_html', 'remove_urls', 'remove_punctuation']
```

#### Example 1.4: Feature Discovery

```python
from nahiarhdNLP.preprocessing import Pipeline

# Get all available features
all_features = Pipeline.get_available_steps()

print("All Available Features:")
for feature_name, description in sorted(all_features.items()):
    print(f"  {feature_name:25} - {description}")

print(f"\nTotal Features: {len(all_features)}")

# Get features organized by category
features_by_category = Pipeline.get_available_steps_by_category()

print("\nFeatures by Category:")
for category, feature_names in features_by_category.items():
    print(f"\n{category}:")
    for feature_name in feature_names:
        description = all_features.get(feature_name, "No description")
        print(f"  {feature_name:25} - {description}")
```

**Output:**

```
All Available Features:
  clean_hashtags           - Remove # symbol but keep tag text
  clean_html               - Remove HTML tags from text
  clean_mentions           - Remove @ symbol but keep username
  clean_urls               - Remove URL protocols (http://, https://) but keep domain
  emoji_to_text            - Convert emojis to Indonesian text description
  remove_currency          - Remove currency symbols
  remove_emails            - Remove email addresses
  remove_emoji             - Remove all emoji characters
  ... (28 features total)

Total Features: 28

Features by Category:

HTML & Tags:
  clean_html               - Remove HTML tags from text

URLs:
  remove_urls              - Remove complete URLs from text
  clean_urls               - Remove URL protocols (http://, https://) but keep domain

... (8 categories total)
```

---

### 2. Text Cleaning

#### Example 2.1: HTML Tag Removal

```python
from nahiarhdNLP.preprocessing import Pipeline

config = {"clean_html": True}
pipeline = Pipeline(config)

# Test various HTML tags
examples = [
    "<p>This is a paragraph</p>",
    "<div class='container'>Content here</div>",
    "Normal text <b>bold text</b> <i>italic</i>",
    "<script>alert('test')</script>Clean text"
]

for text in examples:
    result = pipeline.process(text)
    print(f"Input : {text}")
    print(f"Output: {result}")
    print("-" * 60)
```

**Output:**

```
Input : <p>This is a paragraph</p>
Output: This is a paragraph
------------------------------------------------------------
Input : <div class='container'>Content here</div>
Output: Content here
------------------------------------------------------------
Input : Normal text <b>bold text</b> <i>italic</i>
Output: Normal text bold text italic
------------------------------------------------------------
Input : <script>alert('test')</script>Clean text
Output: Clean text
------------------------------------------------------------
```

#### Example 2.2: URL Processing

```python
from nahiarhdNLP.preprocessing import Pipeline

# Remove URLs completely
config_remove = {"remove_urls": True}
pipeline_remove = Pipeline(config_remove)

# Clean URLs (remove protocol only)
config_clean = {"clean_urls": True}
pipeline_clean = Pipeline(config_clean)

text = "Visit https://github.com and http://example.com for more info"

print(f"Original     : {text}")
print(f"Remove URLs  : {pipeline_remove.process(text)}")
print(f"Clean URLs   : {pipeline_clean.process(text)}")
```

**Output:**

```
Original     : Visit https://github.com and http://example.com for more info
Remove URLs  : Visit and for more info
Clean URLs   : Visit github.com and example.com for more info
```

#### Example 2.3: Mention & Hashtag Processing

```python
from nahiarhdNLP.preprocessing import Pipeline

text = "Hey @john_doe and @jane! Check out #Python #MachineLearning #AI"

# Remove mentions and hashtags
config_remove = {"remove_mentions": True, "remove_hashtags": True}
pipeline_remove = Pipeline(config_remove)

# Clean mentions and hashtags (keep text)
config_clean = {"clean_mentions": True, "clean_hashtags": True}
pipeline_clean = Pipeline(config_clean)

print(f"Original        : {text}")
print(f"Remove @#       : {pipeline_remove.process(text)}")
print(f"Clean @# (keep) : {pipeline_clean.process(text)}")
```

**Output:**

```
Original        : Hey @john_doe and @jane! Check out #Python #MachineLearning #AI
Remove @#       : Hey and ! Check out
Clean @# (keep) : Hey john_doe and jane! Check out Python MachineLearning AI
```

#### Example 2.4: Emoji Handling

```python
from nahiarhdNLP.preprocessing import Pipeline

config = {"remove_emoji": True}
pipeline = Pipeline(config)

examples = [
    "I love Python 🐍❤️",
    "Great work! 👍😊🎉",
    "Weather today ☀️🌧️⛈️",
]

for text in examples:
    result = pipeline.process(text)
    print(f"Input : {text}")
    print(f"Output: {result}")
    print()
```

**Output:**

```
Input : I love Python 🐍❤️
Output: I love Python

Input : Great work! 👍😊🎉
Output: Great work!

Input : Weather today ☀️🌧️⛈️
Output: Weather today
```

#### Example 2.5: Repeated Characters Normalization

```python
from nahiarhdNLP.preprocessing import Pipeline

config = {"remove_repeated_chars": True}
pipeline = Pipeline(config)

examples = [
    "Haiiiii guys!!!",
    "Kangennnnn bangetttt",
    "Wowwwww kerennn",
    "Makasiiih yaaaa"
]

for text in examples:
    result = pipeline.process(text)
    print(f"Input : {text}")
    print(f"Output: {result}")
```

**Output:**

```
Input : Haiiiii guys!!!
Output: Haiii guys!!

Input : Kangennnnn bangetttt
Output: Kangenn bangett

Input : Wowwwww kerennn
Output: Wowww kerenn

Input : Makasiiih yaaaa
Output: Makasiih yaa
```

---

### 3. Text Normalization

#### Example 3.1: Emoji Conversion

```python
from nahiarhdNLP.preprocessing.normalization.emoji import EmojiConverter

emoji = EmojiConverter()
emoji._load_data()

# Emoji to Text
text_with_emoji = "Hari ini cuaca cerah ☀️ dan saya senang 😊"
result = emoji.emoji_to_text_convert(text_with_emoji)
print(f"Emoji to Text:")
print(f"Input : {text_with_emoji}")
print(f"Output: {result}")
print()

# Text to Emoji (example - depends on your emoji dataset)
text = "saya senang wajah tersenyum"
result = emoji.text_to_emoji_convert(text)
print(f"Text to Emoji:")
print(f"Input : {text}")
print(f"Output: {result}")
```

**Output:**

```
Emoji to Text:
Input : Hari ini cuaca cerah ☀️ dan saya senang 😊
Output: Hari ini cuaca cerah matahari dan saya senang wajah_tersenyum

Text to Emoji:
Input : saya senang wajah tersenyum
Output: saya senang 😊
```

#### Example 3.2: Spell Correction & Slang Normalization

```python
from nahiarhdNLP.preprocessing.normalization.spell_corrector import SpellCorrector

spell = SpellCorrector()

# Single word correction
words = ["sya", "tdk", "gk", "org", "yg", "dgn"]
print("Word Correction:")
for word in words:
    corrected = spell.correct_word(word)
    print(f"  {word:10s} → {corrected}")

print("\n" + "="*60 + "\n")

# Sentence correction
sentences = [
    "gw lg di rmh",
    "gmn kabar lo?",
    "knp gk dtg?",
    "jgn lupa ya"
]

print("Sentence Correction:")
for sent in sentences:
    corrected = spell.correct_sentence(sent)
    print(f"Input : {sent}")
    print(f"Output: {corrected}")
    print()
```

**Output:**

```
Word Correction:
  sya        → saya
  tdk        → tidak
  gk         → tidak
  org        → orang
  yg         → yang
  dgn        → dengan

============================================================

Sentence Correction:
Input : gw lg di rmh
Output: gue lagi di rumah

Input : gmn kabar lo?
Output: gimana kabar kamu?

Input : knp gk dtg?
Output: kenapa tidak datang?

Input : jgn lupa ya
Output: jangan lupa ya
```

#### Example 3.3: Complete Text Normalization Pipeline

```python
from nahiarhdNLP.preprocessing import Pipeline

# Comprehensive normalization pipeline
config = {
    "clean_html": True,
    "clean_mentions": True,
    "clean_hashtags": True,
    "remove_urls": True,
    "remove_emoji": True,
    "remove_extra_spaces": True,
    "remove_repeated_chars": True,
    "spell_corrector_sentence": True,
    "remove_lowercase": True
}

pipeline = Pipeline(config)

# Messy Indonesian text
text = """
Haiii @temans!! 😍 Kmrn gw udh coba apps baruu loh di https://example.com
#KerenBanget #Recommended Gkkkk nyesel dehhhh!!! 🚀🚀
"""

result = pipeline.process(text)

print("=" * 70)
print("ORIGINAL TEXT:")
print(text)
print("=" * 70)
print("NORMALIZED TEXT:")
print(result)
print("=" * 70)
```

**Output:**

```
======================================================================
ORIGINAL TEXT:

Haiii @temans!! 😍 Kmrn gw udh coba apps baruu loh di https://example.com
#KerenBanget #Recommended Gkkkk nyesel dehhhh!!! 🚀🚀

======================================================================
NORMALIZED TEXT:
haiii temans!! kemarin gue sudah coba apps baruu loh di kerenbangett recommendedd gkk nyesell dehh!!!
======================================================================
```

---

### 4. Linguistic Processing

#### Example 4.1: Stemming

```python
from nahiarhdNLP.preprocessing.linguistic.stemmer import Stemmer

stemmer = Stemmer()

# Test various Indonesian words
words = [
    "bermain",      # playing
    "berlari",      # running
    "kebahagiaan",  # happiness
    "pembelajaran", # learning
    "menyenangkan", # enjoyable
    "berkomunikasi" # communicate
]

print("Indonesian Stemming:")
print(f"{'Word':<20} → {'Stem'}")
print("-" * 40)
for word in words:
    stem = stemmer.stem(word)
    print(f"{word:<20} → {stem}")

print("\n" + "="*60 + "\n")

# Sentence stemming
sentences = [
    "Saya sedang belajar pemrograman Python",
    "Mereka bermain bola di lapangan",
    "Kebahagiaan adalah kunci kesuksesan"
]

print("Sentence Stemming:")
for sent in sentences:
    stemmed = stemmer.stem(sent)
    print(f"Input : {sent}")
    print(f"Output: {stemmed}")
    print()
```

**Output:**

```
Indonesian Stemming:
Word                 → Stem
----------------------------------------
bermain              → main
berlari              → lari
kebahagiaan          → bahagia
pembelajaran         → ajar
menyenangkan         → senang
berkomunikasi        → komunikasi

============================================================

Sentence Stemming:
Input : Saya sedang belajar pemrograman Python
Output: saya sedang ajar program python

Input : Mereka bermain bola di lapangan
Output: mereka main bola di lapang

Input : Kebahagiaan adalah kunci kesuksesan
Output: bahagia adalah kunci sukses
```

#### Example 4.2: Stopword Removal

```python
from nahiarhdNLP.preprocessing.linguistic.stopword import StopwordRemover

stopword = StopwordRemover()
stopword._load_data()

# Test sentences
sentences = [
    "Saya sedang belajar bahasa pemrograman Python untuk data science",
    "Mereka akan pergi ke pasar besok pagi",
    "Ini adalah contoh kalimat dengan banyak stopwords yang harus dihapus"
]

print("Stopword Removal:")
print("=" * 70)
for sent in sentences:
    cleaned = stopword.remove_stopwords(sent)
    print(f"Original: {sent}")
    print(f"Cleaned : {cleaned}")
    print("-" * 70)
```

**Output:**

```
Stopword Removal:
======================================================================
Original: Saya sedang belajar bahasa pemrograman Python untuk data science
Cleaned : belajar bahasa pemrograman Python data science
----------------------------------------------------------------------
Original: Mereka akan pergi ke pasar besok pagi
Cleaned : pasar besok pagi
----------------------------------------------------------------------
Original: Ini adalah contoh kalimat dengan banyak stopwords yang harus dihapus
Cleaned : contoh kalimat stopwords dihapus
----------------------------------------------------------------------
```

#### Example 4.3: Complete Linguistic Pipeline

```python
from nahiarhdNLP.preprocessing import Pipeline

# Linguistic processing pipeline
config = {
    "remove_lowercase": True,
    "stopword": True,
    "stem": True,
    "remove_extra_spaces": True
}

pipeline = Pipeline(config)

texts = [
    "Saya sedang mengembangkan aplikasi pembelajaran online",
    "Mereka bermain musik dengan sangat menyenangkan",
    "Kebahagiaan adalah perjalanan bukan tujuan"
]

print("Complete Linguistic Processing:")
print("=" * 70)
for text in texts:
    result = pipeline.process(text)
    print(f"Original : {text}")
    print(f"Processed: {result}")
    print("-" * 70)
```

**Output:**

```
Complete Linguistic Processing:
======================================================================
Original : Saya sedang mengembangkan aplikasi pembelajaran online
Processed: kembang aplikasi ajar online
----------------------------------------------------------------------
Original : Mereka bermain musik dengan sangat menyenangkan
Processed: main musik senang
----------------------------------------------------------------------
Original : Kebahagiaan adalah perjalanan bukan tujuan
Processed: bahagia jalan tuju
----------------------------------------------------------------------
```

#### Example 4.4: Tokenization

```python
from nahiarhdNLP.preprocessing.tokenization.tokenizer import Tokenizer

tokenizer = Tokenizer()

texts = [
    "Ini adalah contoh kalimat sederhana",
    "Python, Java, dan JavaScript adalah bahasa pemrograman",
    "Email: test@example.com, Website: https://example.com"
]

print("Tokenization Examples:")
print("=" * 70)
for text in texts:
    tokens = tokenizer.tokenize(text)
    print(f"Text  : {text}")
    print(f"Tokens: {tokens}")
    print("-" * 70)
```

**Output:**

```
Tokenization Examples:
======================================================================
Text  : Ini adalah contoh kalimat sederhana
Tokens: ['Ini', 'adalah', 'contoh', 'kalimat', 'sederhana']
----------------------------------------------------------------------
Text  : Python, Java, dan JavaScript adalah bahasa pemrograman
Tokens: ['Python', ',', 'Java', ',', 'dan', 'JavaScript', 'adalah', 'bahasa', 'pemrograman']
----------------------------------------------------------------------
Text  : Email: test@example.com, Website: https://example.com
Tokens: ['Email', ':', 'test@example.com', ',', 'Website', ':', 'https://example.com']
----------------------------------------------------------------------
```

---

### 5. Text Replacement

#### Example 5.1: Email, Link, and Mention Replacement

```python
from nahiarhdNLP.preprocessing import Pipeline

# Configure replacement pipeline
config = {
    "replace_email": True,
    "replace_link": True,
    "replace_user": True
}

pipeline = Pipeline(config)

examples = [
    "Contact me at john.doe@gmail.com for more info",
    "Visit https://github.com/nahiarhd for the code",
    "Thanks @john and @jane for your help!",
    "Email: info@company.com | Web: https://company.com | Twitter: @company"
]

print("Text Replacement:")
print("=" * 70)
for text in examples:
    result = pipeline.process(text)
    print(f"Input : {text}")
    print(f"Output: {result}")
    print("-" * 70)
```

**Output:**

```
Text Replacement:
======================================================================
Input : Contact me at john.doe@gmail.com for more info
Output: Contact me at <email> for more info
----------------------------------------------------------------------
Input : Visit https://github.com/nahiarhd for the code
Output: Visit <link> for the code
----------------------------------------------------------------------
Input : Thanks @john and @jane for your help!
Output: Thanks <user> and <user> for your help!
----------------------------------------------------------------------
Input : Email: info@company.com | Web: https://company.com | Twitter: @company
Output: Email: <email> | Web: <link> | Twitter: <user>
----------------------------------------------------------------------
```

#### Example 5.2: Data Anonymization Pipeline

```python
from nahiarhdNLP.preprocessing import Pipeline

# Complete anonymization pipeline
config = {
    "replace_email": True,
    "replace_link": True,
    "replace_user": True,
    "remove_phones": True,
    "clean_html": True
}

pipeline = Pipeline(config)

# Sensitive data example
text = """
<div class="contact">
Customer: @johndoe
Email: john.doe@email.com
Phone: +62-812-3456-7890
Website: https://customer-site.com
</div>
"""

result = pipeline.process(text)

print("DATA ANONYMIZATION")
print("=" * 70)
print("ORIGINAL:")
print(text)
print("=" * 70)
print("ANONYMIZED:")
print(result)
print("=" * 70)
```

**Output:**

```
DATA ANONYMIZATION
======================================================================
ORIGINAL:

<div class="contact">
Customer: @johndoe
Email: john.doe@email.com
Phone: +62-812-3456-7890
Website: https://customer-site.com
</div>

======================================================================
ANONYMIZED:
Customer: <user> Email: <email> Phone: Website: <link>
======================================================================
```

---

### 6. Dataset Loaders

#### Example 6.1: Loading Built-in Datasets

```python
from nahiarhdNLP.datasets import DatasetLoader

loader = DatasetLoader()

# Load stopwords
stopwords = loader.load_stopwords_dataset()
print(f"📚 Stopwords Dataset:")
print(f"   Total words: {len(stopwords)}")
print(f"   Sample: {stopwords[:10]}")
print()

# Load slang dictionary
slang_dict = loader.load_slang_dataset()
print(f"💬 Slang Dictionary:")
print(f"   Total entries: {len(slang_dict)}")
print(f"   Sample mappings:")
for slang, formal in list(slang_dict.items())[:5]:
    print(f"      {slang:10s} → {formal}")
print()

# Load emoji dictionary
emoji_dict = loader.load_emoji_dataset()
print(f"😊 Emoji Dictionary:")
print(f"   Total emojis: {len(emoji_dict)}")
print(f"   Sample mappings:")
for emoji, text in list(emoji_dict.items())[:5]:
    print(f"      {emoji:5s} → {text}")
print()

# Load wordlist
wordlist = loader.load_wordlist_dataset()
print(f"📖 Wordlist Dataset:")
print(f"   Total words: {len(wordlist)}")
print(f"   Sample: {wordlist[:10]}")
```

**Output:**

```
📚 Stopwords Dataset:
   Total words: 758
   Sample: ['ada', 'adalah', 'adanya', 'adapun', 'agak', 'agaknya', 'agar', 'akan', 'akankah', 'akhir']

💬 Slang Dictionary:
   Total entries: 3592
   Sample mappings:
      gw         → gue
      lo         → kamu
      gak        → tidak
      yg         → yang
      dgn        → dengan

😊 Emoji Dictionary:
   Total emojis: 1800
   Sample mappings:
      😀     → wajah_tersenyum
      😁     → wajah_gembira
      😂     → tertawa_terbahak
      🤣     → tertawa_guling
      😃     → senyum_lebar

📖 Wordlist Dataset:
   Total words: 28526
   Sample: ['a', 'aa', 'aaa', 'aaai', 'aai', 'aak', 'aal', 'aalim', 'aam', 'aan']
```

---

## ⚙️ Pipeline Configuration Options

### Complete Configuration Reference

```python
config = {
    # ===== TEXT CLEANING =====
    # HTML & Tags
    "clean_html": True,              # Remove HTML tags

    # URLs
    "remove_urls": True,             # Remove complete URLs
    "clean_urls": True,              # Remove URL protocols (http://, https://)

    # Social Media
    "remove_mentions": True,         # Remove @mentions completely
    "clean_mentions": True,          # Remove @ but keep username
    "remove_hashtags": True,         # Remove #hashtags completely
    "clean_hashtags": True,          # Remove # but keep tag text

    # Content Removal
    "remove_emoji": True,            # Remove emoji characters
    "remove_punctuation": True,      # Remove punctuation marks
    "remove_numbers": True,          # Remove numbers
    "remove_emails": True,           # Remove email addresses
    "remove_phones": True,           # Remove phone numbers
    "remove_currency": True,         # Remove currency symbols

    # Text Cleaning
    "remove_special_chars": True,    # Remove special characters
    "remove_extra_spaces": True,     # Normalize whitespace
    "remove_repeated_chars": True,   # Normalize repeated characters (e.g., "haiiii" → "haii")
    "remove_whitespace": True,       # Clean tabs, newlines, etc.
    "remove_lowercase": True,        # Convert to lowercase

    # ===== TEXT NORMALIZATION =====
    "emoji_to_text": True,           # Convert emojis to text description
    "text_to_emoji": True,           # Convert text to emojis
    "spell_corrector_word": True,    # Correct spelling for single words
    "spell_corrector_sentence": True, # Correct spelling for sentences

    # ===== LINGUISTIC PROCESSING =====
    "stem": True,                    # Apply stemming (reduce to root form)
    "stopword": True,                # Remove stopwords
    "tokenizer": True,               # Tokenize text

    # ===== TEXT REPLACEMENT =====
    "replace_email": True,           # Replace emails with <email>
    "replace_link": True,            # Replace URLs with <link>
    "replace_user": True,            # Replace mentions with <user>
}
```

### Configuration Tips

1. **For Social Media**: Use `clean_*` instead of `remove_*` to keep the text content
2. **For Formal Text**: Use `spell_corrector_sentence` to normalize slang
3. **For ML/NLP**: Combine `stem`, `stopword`, and `remove_lowercase`
4. **For Anonymization**: Use `replace_*` options

---

## 📖 API Documentation

### Pipeline Class

```python
class Pipeline:
    """
    Configurable text preprocessing pipeline for Indonesian text.

    Args:
        config (dict): Dictionary of preprocessing steps {step_name: True/False}

    Methods:
        process(text: str) -> str: Process text through the pipeline
        update_config(new_config: dict) -> None: Update pipeline configuration
        get_enabled_steps() -> list: Get list of enabled processing steps
        __call__(text: str) -> str: Allow pipeline to be called as a function

    Example:
        >>> config = {"clean_html": True, "stopword": True}
        >>> pipeline = Pipeline(config)
        >>> result = pipeline.process("<p>Saya sedang belajar NLP</p>")
        >>> # or use as callable
        >>> result = pipeline("<p>Saya sedang belajar NLP</p>")
    """
```

### Available Processing Steps

See [Pipeline Configuration Options](#-pipeline-configuration-options) for complete list.

---

## 🛠️ Development

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

### Building Package

```bash
# Install build tools
pip install build twine

# Build distributions
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Add examples for new functionality

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Raihan Hidayatullah Djunaedi**

- Email: raihanhd.dev@gmail.com
- GitHub: [@raihanhd12](https://github.com/raihanhd12)

---

## 🙏 Acknowledgments

- **Sastrawi** - Indonesian stemming library
- **Indonesian NLP Community** - For datasets and inspiration
- All contributors who helped improve this library

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/nahiarhd/NLP_nahiarhd?style=social)
![GitHub forks](https://img.shields.io/github/forks/nahiarhd/NLP_nahiarhd?style=social)
![GitHub issues](https://img.shields.io/github/issues/nahiarhd/NLP_nahiarhd)
![GitHub pull requests](https://img.shields.io/github/issues-pr/nahiarhd/NLP_nahiarhd)

---

<div align="center">

**Made with ❤️ for Indonesian NLP Community**

[⬆ Back to Top](#-nahiarhdnlp)

</div>
