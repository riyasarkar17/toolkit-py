"""String helper utilities."""

from __future__ import annotations

import re
import unicodedata


def _normalize(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii")


def slugify(value: str, separator: str = "-") -> str:
    """Convert text to a lowercase URL-safe slug."""
    value = _normalize(value).lower().strip()
    value = re.sub(r"[^a-z0-9]+", separator, value)
    value = re.sub(rf"{re.escape(separator)}+", separator, value)
    return value.strip(separator)


def snake_case(value: str) -> str:
    """Convert text to snake_case."""
    return slugify(value, separator="_")


def kebab_case(value: str) -> str:
    """Convert text to kebab-case."""
    return slugify(value, separator="-")


def camel_case(value: str) -> str:
    """Convert text to camelCase."""
    parts = [part for part in re.split(r"[^a-zA-Z0-9]+", _normalize(value)) if part]
    if not parts:
        return ""
    head = parts[0].lower()
    tail = "".join(part.capitalize() for part in parts[1:])
    return f"{head}{tail}"
