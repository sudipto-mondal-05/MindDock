"""Repository for filesystem-based storage of raw and processed files."""

from pathlib import Path

from app.core.logger import get_logger

logger = get_logger()


class FileRepository:
    """Handles reading/writing files to the local storage directories."""

    def __init__(self, base_dir: str) -> None:
        """Initialize the file repository.

        Args:
            base_dir: Root directory for file storage.
        """
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_file(self, filename: str, content: bytes) -> str:
        """Save raw file content to disk.

        Args:
            filename: Target filename.
            content: Raw bytes to write.

        Returns:
            str: The full path where the file was saved.
        """
        target_path = self.base_dir / filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(content)
        logger.info("Saved uploaded file to %s", target_path)
        return str(target_path)

    def read_file(self, filename: str) -> bytes:
        """Read raw file content from disk."""
        target_path = self.base_dir / filename
        return target_path.read_bytes()

    def delete_file(self, filename: str) -> None:
        """Delete a file from disk."""
        target_path = self.base_dir / filename
        if target_path.exists():
            target_path.unlink()
            logger.info("Deleted file %s", target_path)

    def list_files(self) -> list[str]:
        """Return all filenames stored in the base directory."""
        return [p.name for p in self.base_dir.iterdir() if p.is_file()]
