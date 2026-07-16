"""Simple migration runner for applying schema changes over time."""

from app.core.logger import get_logger
from app.database.database import get_connection
from app.database.schema import ALL_SCHEMAS

logger = get_logger()


def run_migrations() -> None:
    """Apply all pending schema migrations.

    TODO: Replace with a versioned migration system (e.g. alembic) if the
    project grows beyond simple CREATE TABLE IF NOT EXISTS statements.
    """
    with get_connection() as conn:
        for statement in ALL_SCHEMAS:
            conn.execute(statement)
        conn.commit()
    logger.info("Migrations applied successfully.")
