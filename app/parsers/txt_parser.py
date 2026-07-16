"""Parser for extracting text content from plain TXT files."""


class TxtParser:
    """Extracts text from plain text documents."""

    def parse(self, file_path: str) -> str:
        """Read text content from a TXT file."""
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
