from datetime import datetime
from typing import List
from pydantic import BaseModel
from enum import Enum


class Module(BaseModel):
    """
    Represents an organized collection of chapters and exercises that form
    a cohesive learning unit over the 13-week course
    """
    id: str  # UUID
    title: str
    slug: str  # URL-friendly
    description: str
    week_number: int  # 1-13
    learning_goals: List[str]
    prerequisites: List[str]  # UUIDs of other modules required
    estimated_duration: int  # Hours
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

    class Config:
        # Enable ORM mode for database integration
        from_attributes = True