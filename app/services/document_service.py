"""Handles document upload, parsing orchestration, and lifecycle management."""

from datetime import datetime
from uuid import uuid4

from app.core.constants import DocumentType, DocumentStatus
from app.core.logger import get_logger
from app.core.security import sanitize_filename
from app.llm.ollama_client import OllamaClient
from app.llm.prompt_manager import PromptManager
from app.models.document import Document
from app.parsers.parser_factory import ParserFactory
from app.repositories.file_repository import FileRepository
from app.core.exceptions import ParsingError

logger = get_logger()


class DocumentService:
    """Handles document upload, parsing orchestration, and lifecycle management."""

    def __init__(self, file_repository: FileRepository) -> None:
        """Initialize the service with the file repository."""
        self.file_repository = file_repository
        self.ollama_client = OllamaClient()
        self.prompt_manager = PromptManager()

    def upload_document(self, filename: str, content: bytes, summary_length: str = "short") -> Document:
        """Save an uploaded document to disk and return its metadata."""
        sanitized = sanitize_filename(filename)
        self.file_repository.save_file(sanitized, content)

        doc_type = self._detect_document_type(sanitized)
        try:
            text = self._extract_text(sanitized, doc_type)
            if not text or not text.strip():
                # No extractable text found (common with scanned/image PDFs)
                raise ValueError(
                    "No extractable text found in the document. The file may be a scanned PDF or image-only; enable OCR or upload a text-based PDF."
                )
        except ParsingError as exc:
            # Surface parsing-specific errors to the API layer with details
            logger.info("Parsing failed for %s: %s", sanitized, exc)
            raise ValueError(str(exc)) from exc
        except ValueError:
            # Let explicit ValueErrors (e.g., empty-extraction) bubble up
            raise
        except Exception as exc:
            logger.exception("Failed to parse uploaded document %s", sanitized)
            raise ValueError("Unable to parse uploaded document.") from exc

        summary = self._summarize_text(text, summary_length)
        chunk_count = self._count_chunks(text)

        document = Document(
            id=sanitized,
            filename=sanitized,
            doc_type=doc_type,
            status=DocumentStatus.PROCESSED if summary else DocumentStatus.UPLOADED,
            size_bytes=len(content),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            chunk_count=chunk_count,
            summary=summary,
        )

        logger.info(
            "Uploaded document %s with %s chunks and summary length=%s",
            sanitized,
            chunk_count,
            summary_length,
        )
        return document

    def _count_chunks(self, text: str) -> int:
        from app.retrieval.chunker import Chunker

        return len(Chunker().split(text))

    def summarize_document(self, document_id: str, summary_length: str = "medium") -> str:
        """Generate a summary for an already uploaded document."""
        doc_type = self._detect_document_type(document_id)
        file_path = self.file_repository.base_dir / document_id
        if not file_path.exists():
            raise ValueError("Document not found.")

        try:
            text = self._extract_text(document_id, doc_type)
            if not text or not text.strip():
                raise ValueError(
                    "No extractable text found in the document. The file may be a scanned PDF or image-only; enable OCR or upload a text-based PDF."
                )
        except ParsingError as exc:
            logger.info("Parsing failed for %s during summarization: %s", document_id, exc)
            raise ValueError(str(exc)) from exc

        return self._summarize_text(text, summary_length)

    def list_documents(self) -> list[Document]:
        """List documents currently stored in the upload directory."""
        documents: list[Document] = []
        for filename in self.file_repository.list_files():
            try:
                doc_type = self._detect_document_type(filename)
            except ValueError:
                continue

            path = self.file_repository.base_dir / filename
            documents.append(
                Document(
                    id=filename,
                    filename=filename,
                    doc_type=doc_type,
                    status=DocumentStatus.UPLOADED,
                    size_bytes=path.stat().st_size,
                    created_at=datetime.utcfromtimestamp(path.stat().st_ctime),
                    updated_at=datetime.utcfromtimestamp(path.stat().st_mtime),
                )
            )
        return documents

    def _extract_text(self, filename: str, doc_type: DocumentType) -> str:
        parser = ParserFactory.get_parser(doc_type)
        file_path = str(self.file_repository.base_dir / filename)
        return parser.parse(file_path)

    def _summarize_text(self, text: str, length: str) -> str:
        trimmed = text.strip()
        if not trimmed:
            return ""

        max_chars = 5000
        if len(trimmed) > max_chars:
            trimmed = trimmed[:max_chars]

        prompt = self.prompt_manager.get_summary_prompt(trimmed, length)
        return self.ollama_client.generate(prompt)

    def _detect_document_type(self, filename: str) -> DocumentType:
        if filename.lower().endswith(".pdf"):
            return DocumentType.PDF
        if filename.lower().endswith(".docx"):
            return DocumentType.DOCX
        if filename.lower().endswith(".txt"):
            return DocumentType.TXT
        raise ValueError("Unsupported file type")
