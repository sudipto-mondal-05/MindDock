"""Domain models representing uploaded documents."""

from datetime import datetime

from pydantic import BaseModel, Field

from app.core.constants import DocumentStatus, DocumentType


class Document(BaseModel):
    """Represents a single uploaded document and its metadata.

    Attributes:
        id: Unique identifier for the document.
        filename: Original filename as uploaded by the user.
        doc_type: Detected document type (pdf/docx/txt).
        status: Current processing lifecycle status.
        size_bytes: File size in bytes.
        created_at: Timestamp when the document was uploaded.
        updated_at: Timestamp when the document was last updated.
        chunk_count: Number of chunks generated during processing.
    """

    id: str
    filename: str
    doc_type: DocumentType
    status: DocumentStatus = DocumentStatus.UPLOADED
    size_bytes: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    chunk_count: int = 0
    summary: str | None = None

    # TODO: add owner/user_id once multi-user support is introduced
