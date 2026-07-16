"""Centralized logging configuration using Loguru."""

import sys

from loguru import logger

from app.core.config import get_settings

_settings = get_settings()

logger.remove()
logger.add(
    sys.stdout,
    level="DEBUG" if _settings.debug else "INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
)
logger.add(
    "storage/temp/minddock.log",
    rotation="10 MB",
    retention="7 days",
    level="DEBUG",
)


def get_logger():
    """Return the configured application logger.

    Returns:
        loguru.Logger: The shared Loguru logger instance.
    """
    return logger
