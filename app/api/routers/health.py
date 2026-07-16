"""Service health check endpoint."""

from fastapi import APIRouter

from app.core.config import get_settings
from app.models.responses import HealthResponse

settings = get_settings()

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return the current health status of the API.

    Returns:
        HealthResponse: Basic status and environment information.
    """
    return HealthResponse(status="ok", app_name=settings.app_name, environment=settings.environment)
