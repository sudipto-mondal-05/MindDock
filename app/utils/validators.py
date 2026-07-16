"""Input validation helpers shared across the application."""

from app.core.constants import ALLOWED_EXTENSIONS


def is_allowed_file(filename: str) -> bool:
    """Check whether a filename has an allowed document extension.

    Args:
        filename: The filename to check.

    Returns:
        bool: True if the extension is allowed, False otherwise.
    """
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)


def is_valid_document_id(document_id: str) -> bool:
    """Validate the format of a document identifier.

    Args:
        document_id: The identifier to validate.

    Returns:
        bool: True if the identifier looks valid.

    TODO: Enforce UUID format once ID generation strategy is finalized.
    """
    return bool(document_id) and len(document_id) > 0
