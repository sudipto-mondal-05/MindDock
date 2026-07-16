"""Domain models representing chat conversations and messages."""

from datetime import datetime

from pydantic import BaseModel, Field

from app.core.constants import MessageRole


class ChatMessage(BaseModel):
    """A single message within a chat conversation.

    Attributes:
        id: Unique identifier for the message.
        conversation_id: Identifier of the parent conversation.
        role: Role of the message sender.
        content: Text content of the message.
        created_at: Timestamp when the message was created.
    """

    id: str
    conversation_id: str
    role: MessageRole
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ChatConversation(BaseModel):
    """A conversation thread tied to one or more documents.

    Attributes:
        id: Unique identifier for the conversation.
        document_ids: Documents this conversation is scoped to.
        title: Human-friendly conversation title.
        created_at: Timestamp when the conversation was created.
    """

    id: str
    document_ids: list[str] = Field(default_factory=list)
    title: str = "New Conversation"
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # TODO: add message history reference once repository layer is implemented
