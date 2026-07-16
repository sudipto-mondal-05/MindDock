"""SQLite database connection management."""

import sqlite3
from contextlib import contextmanager

from app.core.config import get_settings
from app.core.logger import get_logger

logger = get_logger()
settings = get_settings()


@contextmanager
def get_connection():
    """Yield a SQLite database connection as a context manager.

    Yields:
        sqlite3.Connection: An open database connection.

    TODO: Consider connection pooling for concurrent request handling.
    """
    conn = sqlite3.connect(settings.sqlite_db_path)
    try:
        yield conn
    finally:
        conn.close()


def init_db() -> None:
    """Initialize the database, creating tables if they do not exist.

    TODO: Call schema creation statements from schema.py.
    """
    logger.info("Initializing database at {}", settings.sqlite_db_path)
    # TODO: execute CREATE TABLE statements
