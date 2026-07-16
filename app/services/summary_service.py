"""Handles generation and retrieval of document summaries."""

from app.core.logger import get_logger
from app.models.summary import Summary
from app.repositories.file_repository import FileRepository
from app.services.document_service import DocumentService

logger = get_logger()


class SummaryService:
    """Handles generation and retrieval of document summaries."""

    def __init__(self, file_repository: FileRepository) -> None:
        """Initialize the service with required repositories."""
        self.document_service = DocumentService(file_repository)

    def generate_summary(self, document_id: str, length: str = "medium") -> Summary:
        """Generate a summary for a previously uploaded document."""
        content = self.document_service.summarize_document(document_id, length)
        return Summary(id=document_id, document_id=document_id, content=content, length=length)
