from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class DifficultyLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class TextbookChapter(BaseModel):
    """
    Represents a textbook chapter with educational content organized by topic
    with learning objectives and exercises
    """
    id: str  # UUID
    title: str
    slug: str  # URL-friendly
    content: str  # Markdown format
    module_id: str  # UUID reference to Module
    chapter_number: int  # For ordering within module
    learning_objectives: List[str]
    prerequisites: List[str]  # UUIDs of other chapters required
    estimated_reading_time: int  # Minutes
    word_count: int
    difficulty_level: DifficultyLevel
    created_at: datetime
    updated_at: datetime
    is_published: bool = False

    class Config:
        # Enable ORM mode for database integration
        from_attributes = True