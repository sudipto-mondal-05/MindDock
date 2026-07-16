"""Chat conversation endpoints."""

from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.core.constants import MessageRole
from app.core.logger import get_logger
from app.models.chat import ChatMessage
from app.models.requests import ChatRequest
from app.models.responses import ChatResponse
from app.services.chat_service import ChatService

logger = get_logger()

router = APIRouter(prefix="/chat", tags=["chat"])
chat_service: ChatService | None = None


def get_chat_service() -> ChatService:
    global chat_service
    if chat_service is None:
        chat_service = ChatService()
    return chat_service


@router.post("/", response_model=ChatResponse)
async def send_chat(chat_request: ChatRequest) -> ChatResponse:
    """Send a chat message and receive an assistant response."""
    try:
        service = get_chat_service()
        answer = service.chat(
            question=chat_request.message,
            document_ids=chat_request.document_ids,
            conversation_id=chat_request.conversation_id,
        )
    except Exception as exc:
        logger.exception("Chat service failed")
        raise HTTPException(status_code=500, detail="Chat service failed.") from exc

    conversation_id = chat_request.conversation_id or str(uuid4())
    message = ChatMessage(
        id=str(uuid4()),
        conversation_id=conversation_id,
        role=MessageRole.ASSISTANT,
        content=answer,
    )

    return ChatResponse(conversation_id=conversation_id, message=message)
