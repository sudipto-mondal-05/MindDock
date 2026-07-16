"""Pydantic request schemas used by the API layer."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request body for sending a chat message.

    Attributes:
        conversation_id: Existing conversation id, or None to start a new one.
        document_ids: Documents to scope the chat context to.
        message: The user's message text.
    """

    conversation_id: str | None = None
    document_ids: list[str] = Field(default_factory=list)
    message: str


class SummaryRequest(BaseModel):
    """Request body for generating a document summary.

    Attributes:
        document_id: Document to summarize.
        length: Desired summary length (short/medium/long).
    """

    document_id: str
    length: str = "medium"


class QuizRequest(BaseModel):
    """Request body for generating a quiz.

    Attributes:
        document_id: Document to generate the quiz from.
        num_questions: Number of questions to generate.
        difficulty: Desired quiz difficulty.
    """

    document_id: str
    num_questions: int = 5
    difficulty: str = "medium"


class SearchRequest(BaseModel):
    """Request body for semantic search across documents.

    Attributes:
        query: The search query text.
        document_ids: Optional subset of documents to search within.
        top_k: Number of results to return.
    """

    query: str
    document_ids: list[str] = Field(default_factory=list)
    top_k: int = 5

    # TODO: add filters (date range, doc type) once retrieval is implemented
