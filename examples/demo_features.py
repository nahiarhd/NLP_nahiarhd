"""
Demo script to showcase ALL 28 nahiarhdNLP features individually.

This script demonstrates EVERY single feature with input/output examples.
"""

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from nahiarhdNLP.preprocessing import Pipeline

console = Console()


def print_header(title: str):
    """Print a styled header."""
    console.print(f"\n[bold cyan]{title}[/bold cyan]", justify="center")
    console.print("=" * 80, style="cyan")


def demo_single_feature(feature_name: str, test_text: str, description: str = ""):
    """Demonstrate a single feature with input/output."""
    config = {feature_name: True}
    pipeline = Pipeline(config)
    result = pipeline.process(test_text)

    title = f"{feature_name}"
    if description:
        title += f" - {description}"

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{test_text}\n\n[green]Output:[/green]\n{result}",
            title=title,
            border_style="blue",
        )
    )


def demo_all_28_features():
    """Demonstrate all 28 features individually."""
    print_header("🎯 ALL 28 FEATURES - INDIVIDUAL DEMOS")

    console.print("\n[bold yellow]━━━ TEXT CLEANING - HTML ━━━[/bold yellow]\n")

    # 1. clean_html
    demo_single_feature(
        "clean_html",
        "<p>Hello <b>World</b>! <script>alert('test')</script></p>",
        "Remove HTML tags",
    )

    console.print("\n[bold yellow]━━━ TEXT CLEANING - URLs ━━━[/bold yellow]\n")

    # 2. remove_urls
    demo_single_feature(
        "remove_urls",
        "Visit https://github.com and http://example.com for info",
        "Remove complete URLs",
    )

    # 3. clean_urls
    demo_single_feature(
        "clean_urls",
        "Check https://github.com or http://example.com",
        "Remove protocols, keep domain",
    )

    console.print("\n[bold yellow]━━━ TEXT CLEANING - SOCIAL MEDIA ━━━[/bold yellow]\n")

    # 4. remove_mentions
    demo_single_feature(
        "remove_mentions",
        "Thanks @john and @jane for helping!",
        "Remove @mentions completely",
    )

    # 5. clean_mentions
    demo_single_feature(
        "clean_mentions",
        "Thanks @john and @jane for helping!",
        "Remove @ but keep usernames",
    )

    # 6. remove_hashtags
    demo_single_feature(
        "remove_hashtags",
        "Learning #Python #NLP #MachineLearning today",
        "Remove #hashtags completely",
    )

    # 7. clean_hashtags
    demo_single_feature(
        "clean_hashtags",
        "Learning #Python #NLP #MachineLearning today",
        "Remove # but keep tag text",
    )

    console.print(
        "\n[bold yellow]━━━ TEXT CLEANING - CONTENT REMOVAL ━━━[/bold yellow]\n"
    )

    # 8. remove_emoji
    demo_single_feature(
        "remove_emoji", "I love Python 🐍❤️ Great work! 👍😊🎉", "Remove all emojis"
    )

    # 9. remove_punctuation
    demo_single_feature(
        "remove_punctuation",
        "Hello, World! How are you? (Great!)",
        "Remove punctuation marks",
    )

    # 10. remove_numbers
    demo_single_feature(
        "remove_numbers",
        "I have 123 apples and 456 oranges in 2024",
        "Remove all numbers",
    )

    # 11. remove_emails
    demo_single_feature(
        "remove_emails",
        "Contact me at john.doe@example.com or info@company.org",
        "Remove email addresses",
    )

    # 12. remove_phones
    demo_single_feature(
        "remove_phones",
        "Call me at +62-812-3456-7890 or (021) 123-4567",
        "Remove phone numbers",
    )

    # 13. remove_currency
    demo_single_feature(
        "remove_currency",
        "Price: $99.99 or Rp150,000 or €50",
        "Remove currency symbols",
    )

    console.print(
        "\n[bold yellow]━━━ TEXT CLEANING - NORMALIZATION ━━━[/bold yellow]\n"
    )

    # 14. remove_special_chars
    demo_single_feature(
        "remove_special_chars",
        "Hello@World! #Test $Symbol %Value &More",
        "Remove special characters",
    )

    # 15. remove_extra_spaces
    demo_single_feature(
        "remove_extra_spaces",
        "Hello    World     Test      Example",
        "Normalize whitespace",
    )

    # 16. remove_repeated_chars
    demo_single_feature(
        "remove_repeated_chars",
        "Haiiiiii bangetttt kerennnnn",
        "Normalize repeated chars",
    )

    # 17. remove_whitespace
    demo_single_feature(
        "remove_whitespace", "Hello\tWorld\nNew\rLine\tTab", "Clean tabs, newlines, etc"
    )

    # 18. remove_lowercase
    demo_single_feature(
        "remove_lowercase", "HELLO WoRLd TeST ExAmPlE", "Convert to lowercase"
    )

    console.print("\n[bold yellow]━━━ TEXT NORMALIZATION ━━━[/bold yellow]\n")

    # 19. emoji_to_text
    demo_single_feature(
        "emoji_to_text",
        "Cuaca hari ini cerah ☀️ dan saya senang 😊",
        "Convert emojis to text",
    )

    # 20. text_to_emoji
    demo_single_feature(
        "text_to_emoji", "saya senang wajah tersenyum", "Convert text to emojis"
    )

    # 21. spell_corrector_word
    demo_single_feature("spell_corrector_word", "sya", "Correct single word spelling")

    # 22. spell_corrector_sentence
    demo_single_feature(
        "spell_corrector_sentence",
        "gw lg di rmh dgn teman",
        "Correct sentence spelling/slang",
    )

    console.print("\n[bold yellow]━━━ LINGUISTIC PROCESSING ━━━[/bold yellow]\n")

    # 23. stem
    demo_single_feature(
        "stem", "bermain belajar pembelajaran kebahagiaan", "Indonesian stemming"
    )

    # 24. stopword
    demo_single_feature(
        "stopword",
        "saya sedang belajar bahasa pemrograman python untuk data science",
        "Remove Indonesian stopwords",
    )

    # 25. tokenizer
    demo_single_feature("tokenizer", "Hello World, this is a test!", "Tokenize text")

    console.print("\n[bold yellow]━━━ TEXT REPLACEMENT ━━━[/bold yellow]\n")

    # 26. replace_email
    demo_single_feature(
        "replace_email",
        "Contact: john@example.com or info@company.org",
        "Replace with <email> token",
    )

    # 27. replace_link
    demo_single_feature(
        "replace_link",
        "Visit https://github.com or www.example.com",
        "Replace with <link> token",
    )

    # 28. replace_user
    demo_single_feature(
        "replace_user",
        "Thanks @john and @jane for the help!",
        "Replace with <user> token",
    )


def demo_feature_discovery():
    """Demonstrate feature discovery methods."""
    print_header("🔍 FEATURE DISCOVERY")

    # Get all available steps
    all_steps = Pipeline.get_available_steps()

    console.print(
        f"\n[green]Total available features:[/green] [bold]{len(all_steps)}[/bold]\n"
    )

    # Create a table
    table = Table(title="All Available Features", box=box.ROUNDED)
    table.add_column("Feature Name", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")

    for step_name, description in sorted(all_steps.items()):
        table.add_row(step_name, description)

    console.print(table)


def demo_features_by_category():
    """Demonstrate features organized by category."""
    print_header("📁 FEATURES BY CATEGORY")

    categories = Pipeline.get_available_steps_by_category()

    for category_name, steps in categories.items():
        console.print(
            f"\n[bold yellow]{category_name.replace('_', ' ').title()}:[/bold yellow]"
        )
        for step in steps:
            console.print(f"  • {step}", style="green")


def demo_html_cleaning():
    """Demonstrate HTML cleaning."""
    print_header("🧹 HTML CLEANING")

    config = {"clean_html": True}
    pipeline = Pipeline(config)

    text = "<p>Hello <b>World</b>! This is <i>amazing</i>.</p>"
    result = pipeline.process(text)

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{text}\n\n[green]Output:[/green]\n{result}",
            title="HTML Cleaning Demo",
            border_style="blue",
        )
    )


def demo_social_media_cleaning():
    """Demonstrate social media cleaning."""
    print_header("📱 SOCIAL MEDIA CLEANING")

    config = {
        "clean_mentions": True,
        "clean_hashtags": True,
        "remove_urls": True,
        "remove_emoji": True,
    }
    pipeline = Pipeline(config)

    text = "Hey @user123! Check out #Python #NLP 😊 at https://github.com 🚀"
    result = pipeline.process(text)

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{text}\n\n[green]Output:[/green]\n{result}",
            title="Social Media Cleaning Demo",
            border_style="blue",
        )
    )


def demo_text_normalization():
    """Demonstrate text normalization."""
    print_header("✨ TEXT NORMALIZATION")

    config = {
        "remove_lowercase": True,
        "remove_extra_spaces": True,
        "remove_repeated_chars": True,
    }
    pipeline = Pipeline(config)

    text = "HELLOOO    WORLD!!!   Kangennnnn   bangetttt"
    result = pipeline.process(text)

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{text}\n\n[green]Output:[/green]\n{result}",
            title="Text Normalization Demo",
            border_style="blue",
        )
    )


def demo_text_replacement():
    """Demonstrate text replacement."""
    print_header("🔄 TEXT REPLACEMENT (Anonymization)")

    config = {"replace_email": True, "replace_link": True, "replace_user": True}
    pipeline = Pipeline(config)

    text = "Contact @john at john@example.com or visit https://example.com"
    result = pipeline.process(text)

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{text}\n\n[green]Output:[/green]\n{result}",
            title="Text Replacement Demo",
            border_style="blue",
        )
    )


def demo_linguistic_processing():
    """Demonstrate linguistic processing."""
    print_header("🔤 LINGUISTIC PROCESSING")

    config = {"remove_lowercase": True, "stopword": True, "stem": True}
    pipeline = Pipeline(config)

    text = "Saya sedang belajar pemrograman Python untuk pembelajaran mesin"
    result = pipeline.process(text)

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{text}\n\n[green]Output:[/green]\n{result}",
            title="Linguistic Processing Demo (Lowercase + Stopword + Stem)",
            border_style="blue",
        )
    )


def demo_complete_pipeline():
    """Demonstrate a complete preprocessing pipeline."""
    print_header("🚀 COMPLETE PREPROCESSING PIPELINE")

    config = {
        "clean_html": True,
        "clean_mentions": True,
        "clean_hashtags": True,
        "remove_urls": True,
        "remove_emoji": True,
        "remove_extra_spaces": True,
        "remove_repeated_chars": True,
        "remove_lowercase": True,
        "stopword": True,
    }
    pipeline = Pipeline(config)

    text = """
    <p>Haiii @temans!! 😍 Kmrn saya udh coba apps baruu loh
    di https://example.com #KerenBanget Gkkkk nyesel dehhhh!!! 🚀</p>
    """

    result = pipeline.process(text)

    console.print(
        Panel(
            f"[yellow]Input:[/yellow]\n{text}\n\n[green]Output:[/green]\n{result}",
            title="Complete Pipeline Demo",
            border_style="blue",
        )
    )

    console.print(f"\n[cyan]Enabled steps:[/cyan] {pipeline.get_enabled_steps()}")


def demo_dynamic_config():
    """Demonstrate dynamic configuration updates."""
    print_header("⚙️ DYNAMIC CONFIGURATION")

    # Start with basic config
    config = {"clean_html": True}
    pipeline = Pipeline(config)

    text = "<p>Hello @user at https://example.com</p>"

    console.print("[cyan]Step 1: Initial config (only clean_html)[/cyan]")
    console.print(f"Enabled: {pipeline.get_enabled_steps()}")
    result1 = pipeline.process(text)
    console.print(f"Result: {result1}\n")

    # Add more steps
    pipeline.update_config({"clean_mentions": True, "remove_urls": True})

    console.print("[cyan]Step 2: After adding clean_mentions and remove_urls[/cyan]")
    console.print(f"Enabled: {pipeline.get_enabled_steps()}")
    result2 = pipeline.process(text)
    console.print(f"Result: {result2}\n")


def main():
    """Run all demos."""
    console.print(
        "\n[bold magenta]╔═══════════════════════════════════════════════════════════════════════╗[/bold magenta]"
    )
    console.print(
        "[bold magenta]║                   nahiarhdNLP Feature Showcase                       ║[/bold magenta]"
    )
    console.print(
        "[bold magenta]║              ALL 28 FEATURES DEMONSTRATED                            ║[/bold magenta]"
    )
    console.print(
        "[bold magenta]╚═══════════════════════════════════════════════════════════════════════╝[/bold magenta]\n"
    )

    # Feature discovery
    demo_feature_discovery()
    demo_features_by_category()

    # ALL 28 INDIVIDUAL FEATURES
    demo_all_28_features()

    # Category examples
    demo_html_cleaning()
    demo_social_media_cleaning()
    demo_text_normalization()
    demo_text_replacement()
    demo_linguistic_processing()
    demo_complete_pipeline()
    demo_dynamic_config()

    # Final summary
    print_header("✅ DEMO COMPLETE")
    console.print(
        "\n[green]All 28 features demonstrated successfully![/green]", justify="center"
    )
    console.print(
        "[cyan]For more information, visit: https://github.com/raihanhd12/nahiarhdNLP[/cyan]\n",
        justify="center",
    )


if __name__ == "__main__":
    main()
