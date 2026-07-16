"""Repository for SQLite-backed persistence of core entities."""

from app.core.logger import get_logger

logger = get_logger()


class SQLiteRepository:
    """Handles CRUD operations against the SQLite database.

    This repository is responsible for documents, conversations,
    summaries, and quiz metadata persistence.
    """

    def __init__(self, db_path: str) -> None:
        """Initialize the repository with a database path.

        Args:
            db_path: Filesystem path to the SQLite database file.
        """
        self.db_path = db_path
        # TODO: initialize connection pool / engine

    def create_document(self, document: dict) -> None:
        """Persist a new document record.

        Args:
            document: Document data to persist.

        TODO: Implement insert logic.
        """
        raise NotImplementedError

    def get_document(self, document_id: str) -> dict | None:
        """Fetch a document by id.

        Args:
            document_id: Identifier of the document to fetch.

        Returns:
            dict | None: The document record, or None if not found.

        TODO: Implement select logic.
        """
        raise NotImplementedError

    def list_documents(self) -> list[dict]:
        """List all stored documents.

        Returns:
            list[dict]: All document records.

        TODO: Implement pagination and filtering.
        """
        raise NotImplementedError

    def delete_document(self, document_id: str) -> None:
        """Delete a document record.

        Args:
            document_id: Identifier of the document to delete.

        TODO: Implement delete logic (cascade to chunks/history).
        """
        raise NotImplementedError
