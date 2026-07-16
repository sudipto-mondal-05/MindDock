"""Formatting helpers for presenting data to the frontend/API consumers."""


def format_file_size(size_bytes: int) -> str:
    """Format a byte count into a human-readable string.

    Args:
        size_bytes: File size in bytes.

    Returns:
        str: Human-readable size (e.g. '1.2 MB').
    """
    size = float(size_bytes)
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def truncate_text(text: str, max_length: int = 200) -> str:
    """Truncate text to a maximum length, appending an ellipsis if needed.

    Args:
        text: The text to truncate.
        max_length: Maximum allowed length.

    Returns:
        str: The possibly truncated text.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + "..."
