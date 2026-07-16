"""Document upload, listing, retrieval, and deletion endpoints."""

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.api.dependencies import get_file_repository
from app.core.logger import get_logger
from app.models.document import Document
from app.models.responses import DocumentListResponse, DocumentResponse
from app.services.document_service import DocumentService
from app.repositories.file_repository import FileRepository

logger = get_logger()

router = APIRouter(prefix="/documents", tags=["documents"])


def get_document_service(file_repo: FileRepository = Depends(get_file_repository)) -> DocumentService:
    return DocumentService(file_repository=file_repo)


@router.post("/", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    document_service: DocumentService = Depends(get_document_service),
) -> DocumentResponse:
    """Upload a new document and save it to storage."""
    content = await file.read()
    try:
        document = document_service.upload_document(file.filename, content)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return DocumentResponse(document=document)


@router.get("/", response_model=DocumentListResponse)
async def list_documents(document_service: DocumentService = Depends(get_document_service)) -> DocumentListResponse:
    """Return a list of uploaded documents."""
    documents = document_service.list_documents()
    return DocumentListResponse(documents=documents, total=len(documents))
