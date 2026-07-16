"""Quiz generation endpoints."""

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_file_repository
from app.core.logger import get_logger
from app.models.requests import QuizRequest
from app.models.responses import QuizResponse
from app.repositories.file_repository import FileRepository
from app.services.quiz_service import QuizService

logger = get_logger()

router = APIRouter(prefix="/quiz", tags=["quiz"])


def get_quiz_service(file_repo: FileRepository = Depends(get_file_repository)) -> QuizService:
    return QuizService(file_repository=file_repo)


@router.post("/", response_model=QuizResponse)
async def generate_quiz(
    quiz_request: QuizRequest,
    quiz_service: QuizService = Depends(get_quiz_service),
) -> QuizResponse:
    """Generate a quiz from an uploaded document."""
    try:
        quiz = quiz_service.generate_quiz(
            document_id=quiz_request.document_id,
            num_questions=quiz_request.num_questions,
            difficulty=quiz_request.difficulty,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Quiz generation failed")
        raise HTTPException(status_code=500, detail="Quiz generation failed.") from exc

    return QuizResponse(quiz=quiz)
