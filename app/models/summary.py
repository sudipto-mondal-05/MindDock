"""Domain models representing document summaries."""

from datetime import datetime

from pydantic import BaseModel, Field


class Summary(BaseModel):
    """Represents a generated summary for a document.

    Attributes:
        id: Unique identifier for the summary.
        document_id: Identifier of the source document.
        content: The generated summary text.
        length: Requested summary length (e.g. short/medium/long).
        created_at: Timestamp when the summary was generated.
    """

    id: str
    document_id: str
    content: str = ""
    length: str = "medium"
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # TODO: add support for section-level / hierarchical summaries
