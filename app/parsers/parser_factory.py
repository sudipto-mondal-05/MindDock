"""Factory for selecting the appropriate parser based on document type."""

from app.core.constants import DocumentType
from app.core.exceptions import UnsupportedFileTypeError
from app.parsers.docx_parser import DocxParser
from app.parsers.pdf_parser import PDFParser
from app.parsers.txt_parser import TxtParser


class ParserFactory:
    """Selects and instantiates the correct parser for a document type."""

    @staticmethod
    def get_parser(doc_type: DocumentType):
        """Return a parser instance for the given document type.

        Args:
            doc_type: The type of document to parse.

        Returns:
            object: An instance of the appropriate parser class.

        Raises:
            UnsupportedFileTypeError: If no parser exists for the type.

        TODO: Consider caching parser instances if they become stateful.
        """
        if doc_type == DocumentType.PDF:
            return PDFParser()
        if doc_type == DocumentType.DOCX:
            return DocxParser()
        if doc_type == DocumentType.TXT:
            return TxtParser()
        raise UnsupportedFileTypeError(f"No parser available for type: {doc_type}")
