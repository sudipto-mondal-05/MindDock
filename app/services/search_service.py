"""Simple content-based search service as a fallback for semantic search.

This service performs keyword-based matching over document chunks using
the existing `ParserFactory` and `Chunker`. It is intentionally simple
so it works without embeddings or an external vector DB.
"""

from typing import List

from app.repositories.file_repository import FileRepository
from app.parsers.parser_factory import ParserFactory
from app.retrieval.chunker import Chunker
from app.core.constants import DocumentType


class SearchService:
    """Performs keyword search over stored documents."""

    def __init__(self, file_repository: FileRepository) -> None:
        self.file_repository = file_repository
        self.chunker = Chunker()

    def _detect_document_type(self, filename: str) -> DocumentType:
        if filename.lower().endswith(".pdf"):
            return DocumentType.PDF
        if filename.lower().endswith(".docx"):
            return DocumentType.DOCX
        if filename.lower().endswith(".txt"):
            return DocumentType.TXT
        raise ValueError("Unsupported file type")

    def _score_chunk(self, query: str, chunk: str) -> float:
        """Simple scoring: count of query words present in the chunk.

        Returns a float score (higher is more relevant).
        """
        q_words = [w for w in query.lower().split() if w]
        if not q_words:
            return 0.0
        chunk_lower = chunk.lower()
        matches = sum(1 for w in q_words if w in chunk_lower)
        return matches / len(q_words)

    def search(self, query: str, document_ids: List[str] | None = None, top_k: int = 5) -> List[dict]:
        """Search across stored documents and return top_k results.

        Each result is a dict: {document_id, chunk_text, score}.
        """
        results: List[dict] = []

        filenames = self.file_repository.list_files()
        if document_ids:
            filenames = [fn for fn in filenames if fn in set(document_ids)]

        for filename in filenames:
            try:
                doc_type = self._detect_document_type(filename)
            except ValueError:
                continue

            parser = ParserFactory.get_parser(doc_type)
            file_path = str(self.file_repository.base_dir / filename)
            try:
                text = parser.parse(file_path)
            except Exception:
                # skip files that fail to parse
                continue

            chunks = self.chunker.split(text)
            for c in chunks:
                score = self._score_chunk(query, c)
                if score > 0:
                    results.append({"document_id": filename, "chunk_text": c, "score": score})

        # Sort and return top_k
        results.sort(key=lambda r: r["score"], reverse=True)
        return results[:top_k]

