"""Analytics dashboard endpoints."""

from fastapi import APIRouter

from app.core.logger import get_logger

logger = get_logger()

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/")
async def list_dashboard_placeholder():
    """Placeholder root endpoint for the dashboard router.

    Returns:
        dict: A placeholder response indicating the endpoint is not yet implemented.

    TODO: Replace with real dashboard endpoint logic.
    """
    return {"message": "dashboard endpoint placeholder - not yet implemented"}
