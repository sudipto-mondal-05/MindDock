"""Domain models representing generated quizzes."""

from datetime import datetime

from pydantic import BaseModel, Field


class QuizQuestion(BaseModel):
    """A single quiz question with options and the correct answer.

    Attributes:
        question: The question text.
        options: List of candidate answers.
        correct_answer: The correct answer (must be one of options).
        explanation: Optional explanation for the correct answer.
    """

    question: str
    options: list[str] = Field(default_factory=list)
    correct_answer: str = ""
    explanation: str | None = None


class Quiz(BaseModel):
    """Represents a full quiz generated from a document.

    Attributes:
        id: Unique identifier for the quiz.
        document_id: Identifier of the source document.
        questions: List of quiz questions.
        difficulty: Difficulty level of the quiz.
        created_at: Timestamp when the quiz was generated.
    """

    id: str
    document_id: str
    questions: list[QuizQuestion] = Field(default_factory=list)
    difficulty: str = "medium"
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # TODO: add scoring / attempt tracking models
