from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum


class QuerySource(str, Enum):
    TEXTBOOK_CHAPTER = "textbook_chapter"
    TEXTBOOK_MODULE = "textbook_module"
    USER_INPUT = "user_input"


class RAGQuery(BaseModel):
    """
    Model representing a RAG (Retrieval-Augmented Generation) query
    """
    id: Optional[str] = None
    query_text: str
    context_text: Optional[str] = None
    source_id: Optional[str] = None
    source_type: Optional[QuerySource] = None
    response_text: Optional[str] = None
    confidence_score: Optional[float] = None
    retrieved_chunks: Optional[List[str]] = None
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    feedback_score: Optional[int] = None  # For feedback functionality later