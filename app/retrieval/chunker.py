"""Splits parsed document text into retrievable chunks."""

from app.core.constants import DEFAULT_CHUNK_OVERLAP, DEFAULT_CHUNK_SIZE


class Chunker:
    """Splits raw text into overlapping chunks suitable for embedding."""

    def __init__(self, chunk_size: int = DEFAULT_CHUNK_SIZE, overlap: int = DEFAULT_CHUNK_OVERLAP) -> None:
        """Initialize the chunker.

        Args:
            chunk_size: Target number of characters per chunk.
            overlap: Number of overlapping characters between chunks.
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str) -> list[str]:
        """Split text into overlapping character chunks.

        Args:
            text: The full document text.

        Returns:
            list[str]: The resulting text chunks.
        """
        normalized = " ".join(text.split())
        if not normalized:
            return []

        chunks: list[str] = []
        start = 0
        text_length = len(normalized)

        while start < text_length:
            end = min(text_length, start + self.chunk_size)
            if end < text_length:
                boundary = normalized.rfind(" ", start, end)
                if boundary > start:
                    end = boundary
            chunk = normalized[start:end].strip()
            if chunk:
                chunks.append(chunk)
            start = end - self.overlap
            if start <= 0:
                start = end
            if start >= text_length:
                break

        return chunks
