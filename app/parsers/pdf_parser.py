"""Parser for extracting text content from PDF files using PyMuPDF.

This module performs imports lazily and raises a clear `ParsingError`
when PyMuPDF is not available or when parsing fails. This gives the
API clearer error messages instead of failing at import time.
"""

from typing import List

from app.core.logger import get_logger
from app.core.exceptions import ParsingError

logger = get_logger()


class PDFParser:
    """Extracts text from PDF documents."""

    def parse(self, file_path: str) -> str:
        """Extract text content from a PDF file.

        Attempts to import PyMuPDF (`fitz`) at call time so the application
        can start even if the optional dependency is missing; a clear
        `ParsingError` is raised with actionable text when parsing fails.
        """
        try:
            import fitz  # PyMuPDF
        except Exception as exc:  # noqa: BLE001 - raising domain error
            raise ParsingError(f"PyMuPDF (fitz) is not available: {exc}") from exc

        doc = None
        try:
            doc = fitz.open(file_path)
            text_parts: List[str] = []
            for page in doc:
                # Use the default text extraction API; gracefully skip empty pages
                try:
                    page_text = page.get_text()
                except Exception:
                    logger.debug("Skipping page with extraction error in %s", file_path)
                    continue
                if page_text:
                    text_parts.append(page_text)

            if text_parts:
                return "\n".join(text_parts)

            # If PyMuPDF extracted nothing, attempt a fallback using pypdf
            try:
                from pypdf import PdfReader
            except Exception as exc:  # pragma: no cover - optional dependency
                logger.debug("pypdf not available for fallback: %s", exc)
            else:
                try:
                    reader = PdfReader(file_path)
                    alt_parts: List[str] = []
                    for p in reader.pages:
                        try:
                            t = p.extract_text()
                        except Exception:
                            continue
                        if t:
                            alt_parts.append(t)
                    if alt_parts:
                        return "\n".join(alt_parts)
                except Exception as exc:
                    logger.debug("pypdf fallback parsing failed for %s: %s", file_path, exc)
        except Exception as exc:
            logger.exception("PDF parsing failed for %s", file_path)
            raise ParsingError(f"Failed to parse PDF {file_path}: {exc}") from exc
        finally:
            if doc is not None:
                try:
                    doc.close()
                except Exception:
                    logger.debug("Error closing PDF document %s", file_path)
        # No extractable text found
        return ""
