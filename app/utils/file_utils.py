"""Filesystem utility helpers for managing storage directories."""

from pathlib import Path


def ensure_directories(paths: list[str]) -> None:
    """Ensure that all given directories exist, creating them if needed.

    Args:
        paths: List of directory paths to ensure.
    """
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


def get_file_extension(filename: str) -> str:
    """Extract the lowercase file extension from a filename.

    Args:
        filename: The filename to inspect.

    Returns:
        str: The extension including the leading dot (e.g. '.pdf').
    """
    return Path(filename).suffix.lower()
