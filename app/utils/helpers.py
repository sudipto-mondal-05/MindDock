"""General-purpose helper functions."""

import uuid
from datetime import datetime


def generate_id() -> str:
    """Generate a unique identifier string.

    Returns:
        str: A UUID4 hex string.
    """
    return uuid.uuid4().hex


def utc_now_iso() -> str:
    """Get the current UTC timestamp in ISO 8601 format.

    Returns:
        str: The current UTC time as an ISO string.
    """
    return datetime.utcnow().isoformat()
