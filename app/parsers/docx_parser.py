"""Parser for extracting text content from DOCX files using python-docx."""

from docx import Document as DocxDocument


class DocxParser:
    """Extracts text from Word (.docx) documents."""

    def parse(self, file_path: str) -> str:
        """Extract text content from a DOCX file."""
        doc = DocxDocument(file_path)
        paragraphs = [paragraph.text for paragraph in doc.paragraphs if paragraph.text]
        return "\n".join(paragraphs)
