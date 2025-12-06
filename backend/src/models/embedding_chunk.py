from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum


class ChunkType(str, Enum):
    CHAPTER_CONTENT = "chapter_content"
    MODULE_CONTENT = "module_content"
    EXERCISE_CONTENT = "exercise_content"
    SUPPLEMENTARY = "supplementary"


class EmbeddingChunk(BaseModel):
    """
    Model representing a text chunk with its embedding for RAG system
    """
    id: Optional[str] = None
    content: str
    embedding: Optional[List[float]] = None  # Vector embedding
    source_id: str  # ID of the source document (chapter, module, etc.)
    source_type: ChunkType
    chunk_index: Optional[int] = None  # Position of this chunk in the source
    metadata: Optional[dict] = None  # Additional metadata about the chunk
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    similarity_score: Optional[float] = None  # For retrieval results