"""Custom application exception hierarchy."""


class MindDockError(Exception):
    """Base exception for all MindDock AI application errors."""


class DocumentNotFoundError(MindDockError):
    """Raised when a requested document cannot be located."""


class UnsupportedFileTypeError(MindDockError):
    """Raised when an uploaded file type is not supported."""


class ParsingError(MindDockError):
    """Raised when a document fails to parse."""


class LLMConnectionError(MindDockError):
    """Raised when the Ollama LLM backend cannot be reached."""


class VectorStoreError(MindDockError):
    """Raised when a ChromaDB vector store operation fails."""

    # TODO: attach richer error context (collection name, operation, etc.)
