"""Shared FastAPI dependency providers."""

from app.core.config import get_settings
from app.repositories.chroma_repository import ChromaRepository
from app.repositories.file_repository import FileRepository
from app.repositories.history_repository import HistoryRepository
from app.repositories.sqlite_repository import SQLiteRepository


def get_sqlite_repository() -> SQLiteRepository:
    """Provide a SQLiteRepository instance."""
    settings = get_settings()
    return SQLiteRepository(db_path=settings.sqlite_db_path)


def get_chroma_repository() -> ChromaRepository:
    """Provide a ChromaRepository instance."""
    settings = get_settings()
    return ChromaRepository(persist_dir=settings.chroma_persist_dir)


def get_file_repository() -> FileRepository:
    """Provide a FileRepository instance."""
    settings = get_settings()
    return FileRepository(base_dir=settings.upload_dir)


def get_history_repository() -> HistoryRepository:
    """Provide a HistoryRepository instance."""
    settings = get_settings()
    return HistoryRepository(db_path=settings.sqlite_db_path)
