"""Quiz generation endpoints."""

from fastapi import APIRouter

from app.core.logger import get_logger

logger = get_logger()

router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.get("/")
async def list_quiz_placeholder():
    """Placeholder root endpoint for the quiz router.

    Returns:
        dict: A placeholder response indicating the endpoint is not yet implemented.

    TODO: Replace with real quiz endpoint logic.
    """
    return {"message": "quiz endpoint placeholder - not yet implemented"}
