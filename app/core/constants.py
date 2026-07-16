"""Application-wide constant values and enumerations."""

from enum import Enum


class DocumentType(str, Enum):
    """Supported document types for upload and parsing."""

    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"


class DocumentStatus(str, Enum):
    """Lifecycle status of an uploaded document."""

    UPLOADED = "uploaded"
    PROCESSING = "processing"
    PROCESSED = "processed"
    FAILED = "failed"


class MessageRole(str, Enum):
    """Role of a message within a chat conversation."""

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


# TODO: Add chunking size / overlap constants once retrieval logic is implemented.
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}
