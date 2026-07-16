"""FastAPI application entrypoint for MindDock AI.

Wires together CORS, middleware, routers, and startup/shutdown events.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.middleware import log_requests_middleware
from app.api.routers import chat, dashboard, documents, health, quiz, search, summary
from app.core.config import get_settings
from app.core.logger import get_logger
from app.database.migrations import run_migrations

settings = get_settings()
logger = get_logger()

app = FastAPI(
    title=settings.app_name,
    description="Local AI-powered document assistant - MindDock AI",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(log_requests_middleware)

app.include_router(health.router)
app.include_router(documents.router)
app.include_router(chat.router)
app.include_router(summary.router)
app.include_router(quiz.router)
app.include_router(search.router)
app.include_router(dashboard.router)


@app.on_event("startup")
async def on_startup() -> None:
    """Run startup tasks: ensure directories exist and database is migrated.

    TODO: Add Ollama connectivity check and ChromaDB warm-up.
    """
    logger.info("Starting {}...", settings.app_name)
    run_migrations()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    """Run graceful shutdown tasks.

    TODO: Close any open connections/clients (Ollama, Chroma, DB pools).
    """
    logger.info("Shutting down {}...", settings.app_name)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=settings.api_host, port=settings.api_port, reload=settings.debug)
