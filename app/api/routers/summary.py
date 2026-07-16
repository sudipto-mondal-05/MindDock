"""Document summarization endpoints."""

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_file_repository
from app.core.logger import get_logger
from app.models.requests import SummaryRequest
from app.models.responses import SummaryResponse
from app.repositories.file_repository import FileRepository
from app.services.summary_service import SummaryService

logger = get_logger()

router = APIRouter(prefix="/summary", tags=["summary"])


def get_summary_service(file_repo: FileRepository = Depends(get_file_repository)) -> SummaryService:
    return SummaryService(file_repository=file_repo)


@router.post("/", response_model=SummaryResponse)
async def generate_summary(
    summary_request: SummaryRequest,
    summary_service: SummaryService = Depends(get_summary_service),
) -> SummaryResponse:
    """Generate a summary for an uploaded document."""
    try:
        summary = summary_service.generate_summary(
            document_id=summary_request.document_id,
            length=summary_request.length,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        logger.exception("Summary generation failed")
        raise HTTPException(status_code=500, detail="Summary generation failed.") from exc

    return SummaryResponse(summary=summary)
