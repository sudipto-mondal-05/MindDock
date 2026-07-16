"""Handles chat conversation orchestration between the user, retrieved context, and the LLM."""

from app.core.logger import get_logger
from app.llm.ollama_client import OllamaClient
from app.llm.prompt_manager import PromptManager

logger = get_logger()


class ChatService:
    """Handles chat conversation orchestration between the user, retrieved context, and the LLM."""

    def __init__(self) -> None:
        """Initialize the service and its LLM and prompt dependencies."""
        self.ollama_client = OllamaClient()
        self.prompt_manager = PromptManager()

    def chat(self, question: str, document_ids: list[str] | None = None, conversation_id: str | None = None) -> str:
        """Run a chat exchange for the given user question."""
        logger.info(
            "ChatService received question=%s conversation_id=%s document_ids=%s",
            question,
            conversation_id,
            document_ids,
        )

        # TODO: Use document_ids to retrieve context from the vector store.
        prompt = self.prompt_manager.get_chat_prompt("", question)
        return self.ollama_client.generate(prompt)
