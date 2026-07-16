"""Handles generation and retrieval of document-based quizzes."""

import json

from app.core.logger import get_logger
from app.llm.ollama_client import OllamaClient
from app.llm.prompt_manager import PromptManager
from app.models.quiz import Quiz, QuizQuestion
from app.repositories.file_repository import FileRepository
from app.services.document_service import DocumentService

logger = get_logger()


class QuizService:
    """Handles generation and retrieval of document-based quizzes."""

    def __init__(self, file_repository: FileRepository) -> None:
        """Initialize the service with document and LLM dependencies."""
        self.document_service = DocumentService(file_repository)
        self.ollama_client = OllamaClient()
        self.prompt_manager = PromptManager()

    def generate_quiz(self, document_id: str, num_questions: int = 5, difficulty: str = "medium") -> Quiz:
        """Generate a quiz from an uploaded document using the local Ollama model."""
        doc_type = self.document_service._detect_document_type(document_id)
        file_path = self.document_service.file_repository.base_dir / document_id
        if not file_path.exists():
            raise ValueError("Document not found.")

        try:
            text = self.document_service._extract_text(document_id, doc_type)
            if not text or not text.strip():
                raise ValueError("No extractable text found in the document.")
        except Exception as exc:
            logger.exception("Failed to parse document %s for quiz generation", document_id)
            raise ValueError("Unable to parse document for quiz generation.") from exc

        prompt = self.prompt_manager.get_quiz_prompt(text, num_questions, difficulty)
        response_text = self.ollama_client.generate(prompt)

        if response_text.startswith("```"):
            response_text = response_text.strip().strip("`")
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()

        start = response_text.find("[")
        end = response_text.rfind("]")
        if start != -1 and end != -1 and end > start:
            response_text = response_text[start : end + 1]

        try:
            payload = json.loads(response_text)
        except json.JSONDecodeError:
            payload = []

        if not isinstance(payload, list):
            payload = []

        questions = []
        for item in payload[:num_questions]:
            if not isinstance(item, dict):
                continue
            options = item.get("options") or []
            if not isinstance(options, list):
                options = []
            questions.append(
                QuizQuestion(
                    question=item.get("question", ""),
                    options=[str(option) for option in options],
                    correct_answer=str(item.get("correct_answer", "")),
                    explanation=item.get("explanation"),
                )
            )

        return Quiz(
            id=f"quiz-{document_id}",
            document_id=document_id,
            questions=questions,
            difficulty=difficulty,
        )
