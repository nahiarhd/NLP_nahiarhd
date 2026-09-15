"""
Text replacement utilities: replace emails, links, and user mentions with tokens.

This module provides simple, well-documented functions used by the pipeline.
"""

import re


class TextReplace:
    def __init__(self, **kwargs):
        self._flags = {
            "replace_email": kwargs.get("replace_email", True),
            "replace_link": kwargs.get("replace_link", True),
            "replace_user": kwargs.get("replace_user", True),
        }

    def replace_email(self, text: str, force: bool = False) -> str:
        """Replace email addresses in `text` with `token`.

        Example:
            replace_email("Contact me at john.doe@gmail.com")
            -> "Contact me at <email>"
        """
        if not self._flags["replace_email"] and not force:
            return text

        email_pattern = re.compile(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        )
        result = re.sub(email_pattern, "<email>", text)
        return result

    def replace_link(self, text: str, force: bool = False) -> str:
        """Replace URLs in `text` with `token`.

        Example:
            replace_link("Visit http://example.com for more info")
            -> "Visit <link> for more info"
        """
        if not self._flags["replace_link"] and not force:
            return text

        url_pattern = re.compile(r"(https?://[^\s]+|www\.[^\s]+)")
        result = re.sub(url_pattern, "<link>", text)
        return result

    def replace_user(self, text: str, force: bool = False) -> str:
        """Replace user mentions in `text` with `token`.

        Example:
            replace_user("Hello @user1 and @user2")
            -> "Hello <user> and <user>"
        """
        if not self._flags["replace_user"] and not force:
            return text

        user_pattern = re.compile(r"@\w+")
        result = re.sub(user_pattern, "<user>", text)
        return result

    def get_options(self) -> dict:
        """Get current replacement options."""
        return dict(self._flags)
