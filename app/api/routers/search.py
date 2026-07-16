"""Search endpoints (content-based fallback implementation)."""

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_file_repository
from app.core.logger import get_logger
from app.models.requests import SearchRequest
from app.models.responses import SearchResponse
from app.repositories.file_repository import FileRepository
from app.services.search_service import SearchService

logger = get_logger()

router = APIRouter(prefix="/search", tags=["search"])


def get_search_service(file_repo: FileRepository = Depends(get_file_repository)) -> SearchService:
    return SearchService(file_repository=file_repo)


@router.post("/", response_model=SearchResponse)
async def semantic_search(
    req: SearchRequest, search_service: SearchService = Depends(get_search_service)
) -> SearchResponse:
    """Perform a simple content-based search across uploaded documents."""
    try:
        results = search_service.search(query=req.query, document_ids=req.document_ids, top_k=req.top_k)
    except Exception as exc:
        logger.exception("Search failed")
        raise HTTPException(status_code=500, detail="Search failed.") from exc

    return SearchResponse(results=results)
