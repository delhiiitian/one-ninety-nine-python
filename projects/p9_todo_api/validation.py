"""Checking incoming JSON before it reaches the database."""

import re
from datetime import date


class ValidationError(ValueError):
    pass


DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def clean_todo(data, partial=False):
    """Return a dict of safe fields. partial=True is for updates (PATCH)."""
    if not isinstance(data, dict):
        raise ValidationError("body must be a JSON object")
    cleaned = {}
    if "title" in data or not partial:
        title = data.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValidationError("title is required and must be text")
        if len(title) > 200:
            raise ValidationError("title must be 200 characters or fewer")
        cleaned["title"] = title.strip()
    if "done" in data:
        if not isinstance(data["done"], bool):
            raise ValidationError("done must be true or false")
        cleaned["done"] = data["done"]
    if data.get("due") is not None:
        due = data["due"]
        if not isinstance(due, str) or not DATE_PATTERN.match(due):
            raise ValidationError("due must look like YYYY-MM-DD")
        try:
            date.fromisoformat(due)
        except ValueError:
            raise ValidationError(f"{due} is not a real date") from None
        cleaned["due"] = due
    unknown = set(data) - {"title", "done", "due"}
    if unknown:
        raise ValidationError(f"unknown field(s): {', '.join(sorted(unknown))}")
    return cleaned
