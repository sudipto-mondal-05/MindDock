"""Application configuration management using Pydantic settings.

Centralizes all environment-driven configuration for MindDock AI.
"""

from functools import lru_cache
from pathlib import Path

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _resolve_storage_path(path_value: str) -> str:
    """Resolve relative storage paths against the project root."""
    path = Path(path_value)
    if path.is_absolute():
        return str(path.resolve())
    return str((PROJECT_ROOT / path).resolve())


class Settings(BaseSettings):
    """Application-wide settings loaded from environment variables.

    Attributes:
        app_name: Human readable application name.
        environment: Deployment environment (dev/staging/prod).
        debug: Toggles debug mode / verbose logging.
        api_host: Host address for the FastAPI server.
        api_port: Port for the FastAPI server.
        cors_origins: Allowed CORS origins for the frontend.
        sqlite_db_path: Path to the SQLite database file.
        chroma_persist_dir: Path to the ChromaDB persistence directory.
        ollama_base_url: Base URL for the local Ollama server.
        ollama_model: Default Ollama model name to use.
        upload_dir: Directory where raw uploaded documents are stored.
        processed_dir: Directory where processed documents are stored.
        export_dir: Directory where exported artifacts are stored.
        temp_dir: Directory used for temporary/scratch files.
        max_upload_size_mb: Maximum allowed upload size in megabytes.
    """

    app_name: str = "MindDock AI"
    environment: str = "development"
    debug: bool = True

    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: list[str] = ["*"]

    sqlite_db_path: str = "data/minddock.db"
    chroma_persist_dir: str = "vector_db"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:3b"

    upload_dir: str = "storage/uploads"
    processed_dir: str = "storage/processed"
    export_dir: str = "storage/exports"
    temp_dir: str = "storage/temp"

    max_upload_size_mb: int = 50

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @model_validator(mode="after")
    def resolve_storage_directories(self) -> "Settings":
        self.upload_dir = _resolve_storage_path(self.upload_dir)
        self.processed_dir = _resolve_storage_path(self.processed_dir)
        self.export_dir = _resolve_storage_path(self.export_dir)
        self.temp_dir = _resolve_storage_path(self.temp_dir)
        return self


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance.

    Using lru_cache ensures the .env file is parsed only once per process.

    Returns:
        Settings: The application settings singleton.
    """
    return Settings()
