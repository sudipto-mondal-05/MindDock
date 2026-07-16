"""Custom middleware for request logging and timing."""

import time

from fastapi import Request

from app.core.logger import get_logger

logger = get_logger()


async def log_requests_middleware(request: Request, call_next):
    """Log incoming requests and their processing time.

    Args:
        request: The incoming HTTP request.
        call_next: The next handler in the middleware chain.

    Returns:
        Response: The HTTP response, with an added X-Process-Time header.
    """
    start_time = time.perf_counter()
    response = await call_next(request)
    duration_ms = (time.perf_counter() - start_time) * 1000
    logger.info(
        "{method} {path} -> {status} ({duration:.2f} ms)",
        method=request.method,
        path=request.url.path,
        status=response.status_code,
        duration=duration_ms,
    )
    response.headers["X-Process-Time"] = f"{duration_ms:.2f}ms"
    return response
