"""Pydantic response schemas returned by the API layer."""

from pydantic import BaseModel, Field

from app.models.chat import ChatMessage
from app.models.document import Document
from app.models.quiz import Quiz
from app.models.summary import Summary


class HealthResponse(BaseModel):
    """Response body for the health check endpoint."""

    status: str = "ok"
    app_name: str
    environment: str


class DocumentResponse(BaseModel):
    """Response wrapping a single document."""

    document: Document


class DocumentListResponse(BaseModel):
    """Response wrapping a list of documents."""

    documents: list[Document] = Field(default_factory=list)
    total: int = 0


class ChatResponse(BaseModel):
    """Response body for a chat message exchange."""

    conversation_id: str
    message: ChatMessage | None = None

    # TODO: populate with real LLM-generated message once chat_service is implemented


class SummaryResponse(BaseModel):
    """Response wrapping a generated summary."""

    summary: Summary


class QuizResponse(BaseModel):
    """Response wrapping a generated quiz."""

    quiz: Quiz


class SearchResultItem(BaseModel):
    """A single semantic search result."""

    document_id: str
    chunk_text: str = ""
    score: float = 0.0


class SearchResponse(BaseModel):
    """Response wrapping semantic search results."""

    results: list[SearchResultItem] = Field(default_factory=list)


class DashboardStatsResponse(BaseModel):
    """Response wrapping dashboard analytics stats."""

    total_documents: int = 0
    total_chats: int = 0
    total_summaries: int = 0
    total_quizzes: int = 0

    # TODO: add time-series stats once dashboard_service is implemented
