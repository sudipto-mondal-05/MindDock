"""Security utilities: API key checks, sanitization, and future auth hooks."""

from fastapi import Header, HTTPException, status


async def verify_request(x_api_key: str | None = Header(default=None)) -> None:
    """Placeholder dependency for request verification.

    Args:
        x_api_key: Optional API key passed via header.

    Raises:
        HTTPException: If verification fails (not yet enforced).

    TODO: Implement real API key / auth-token verification logic.
    """
    # TODO: implement real security checks
    return None


def sanitize_filename(filename: str) -> str:
    """Sanitize an uploaded filename to prevent path traversal.

    Args:
        filename: The raw filename provided by the client.

    Returns:
        str: A sanitized, safe filename.
    """
    # TODO: implement more robust sanitization (unicode, length limits, etc.)
    return filename.replace("..", "").replace("/", "_").replace("\\", "_")
