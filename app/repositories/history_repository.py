"""Repository for chat conversation and message history persistence."""

from app.core.logger import get_logger

logger = get_logger()


class HistoryRepository:
    """Handles persistence of chat conversations and messages."""

    def __init__(self, db_path: str) -> None:
        """Initialize the history repository.

        Args:
            db_path: Filesystem path to the SQLite database file.
        """
        self.db_path = db_path
        # TODO: reuse shared SQLite connection from SQLiteRepository

    def create_conversation(self, conversation: dict) -> None:
        """Persist a new conversation.

        Args:
            conversation: Conversation data to persist.

        TODO: Implement insert logic.
        """
        raise NotImplementedError

    def add_message(self, message: dict) -> None:
        """Persist a new chat message.

        Args:
            message: Message data to persist.

        TODO: Implement insert logic.
        """
        raise NotImplementedError

    def get_conversation_history(self, conversation_id: str) -> list[dict]:
        """Fetch all messages for a conversation.

        Args:
            conversation_id: Identifier of the conversation.

        Returns:
            list[dict]: Ordered list of messages.

        TODO: Implement select logic ordered by created_at.
        """
        raise NotImplementedError
