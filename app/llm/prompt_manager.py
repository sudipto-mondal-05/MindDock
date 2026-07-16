"""Centralized management of prompt templates for all AI features."""


class PromptManager:
    """Loads and renders prompt templates used across services."""

    def __init__(self, prompts_dir: str = "prompts") -> None:
        """Initialize the prompt manager.

        Args:
            prompts_dir: Directory containing prompt template files.
        """
        self.prompts_dir = prompts_dir
        # TODO: load templates from disk (jinja2 or plain string templates)

    def get_chat_prompt(self, context: str, question: str) -> str:
        """Build a chat prompt from retrieved context and a user question."""
        system_prompt = (
            "You are a helpful assistant. Answer the user's question concisely "
            "and accurately using the provided context."
        )

        if context:
            return (
                f"{system_prompt}\n\nContext:\n{context}\n\n"
                f"User: {question}\nAssistant:"
            )

        return f"{system_prompt}\n\nUser: {question}\nAssistant:"

    def get_summary_prompt(self, text: str, length: str) -> str:
        """Build a summarization prompt."""
        length_map = {
            "short": "a brief paragraph",
            "medium": "a clear summary",
            "long": "a detailed summary",
        }
        summary_style = length_map.get(length, "a clear summary")

        return (
            f"Summarize the following document text into {summary_style}. "
            "Keep the summary focused on the main points and avoid adding extra details.\n\n"
            f"Document text:\n{text}\n\nSummary:"
        )

    def get_quiz_prompt(self, text: str, num_questions: int, difficulty: str) -> str:
        """Build a quiz-generation prompt."""
        difficulty_map = {
            "easy": "simple and beginner-friendly",
            "medium": "balanced and moderately challenging",
            "hard": "challenging and detailed",
        }
        difficulty_style = difficulty_map.get(difficulty, "balanced and moderately challenging")

        return (
            f"Create {num_questions} multiple-choice questions from the following document text. "
            f"Make the questions {difficulty_style}. "
            "Return ONLY valid JSON in this exact format: "
            "[{\"question\": \"...\", \"options\": [\"...\", \"...\", \"...\", \"...\"], \"correct_answer\": \"...\", \"explanation\": \"...\"}] "
            "Do not include Markdown, commentary, or surrounding text. "
            "Each question must have exactly four options. "
            "Keep the content grounded in the provided text and avoid invented facts.\n\n"
            f"Document text:\n{text}\n\nQuiz JSON:"
        )
