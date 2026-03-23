"""File and path helper utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_dir(path: str | Path) -> Path:
    """Create a directory if it does not already exist."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Read a text file and return its contents."""
    return Path(path).read_text(encoding=encoding)


def write_text(path: str | Path, content: str, encoding: str = "utf-8") -> Path:
    """Write text to a file, creating parent directories as needed."""
    file_path = Path(path)
    if file_path.parent != Path("."):
        file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding=encoding)
    return file_path


def list_files(path: str | Path, pattern: str = "*") -> Iterable[Path]:
    """Yield files from a directory matching a glob pattern."""
    base = Path(path)
    return (item for item in sorted(base.rglob(pattern)) if item.is_file())
