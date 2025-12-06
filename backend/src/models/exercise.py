from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class ExerciseType(str, Enum):
    multiple_choice = "multiple_choice"
    coding = "coding"
    simulation = "simulation"
    essay = "essay"


class DifficultyLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class Exercise(BaseModel):
    """
    Represents interactive problems and activities associated with chapters and modules
    """
    id: str  # UUID
    title: str
    description: str
    chapter_id: str  # UUID reference to Chapter
    module_id: str  # UUID reference to Module
    exercise_type: ExerciseType
    difficulty_level: DifficultyLevel
    estimated_completion_time: int  # Minutes
    content: str  # Exercise content in Markdown
    solution: Optional[str]  # Hidden solution
    scoring_criteria: dict  # How to grade the exercise
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

    class Config:
        # Enable ORM mode for database integration
        from_attributes = True