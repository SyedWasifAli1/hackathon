from typing import List, Optional
from ..models.chapter import TextbookChapter
from uuid import uuid4
from datetime import datetime


class ChapterService:
    """
    Service class to handle business logic for textbook chapters
    """

    def __init__(self):
        # In a real implementation, this would connect to a database
        self.chapters: List[TextbookChapter] = []

    async def create_chapter(self, chapter_data: dict) -> TextbookChapter:
        """
        Create a new textbook chapter
        """
        chapter = TextbookChapter(
            id=str(uuid4()),
            title=chapter_data.get("title"),
            slug=chapter_data.get("slug"),
            content=chapter_data.get("content", ""),
            module_id=chapter_data.get("module_id"),
            chapter_number=chapter_data.get("chapter_number"),
            learning_objectives=chapter_data.get("learning_objectives", []),
            prerequisites=chapter_data.get("prerequisites", []),
            estimated_reading_time=chapter_data.get("estimated_reading_time", 0),
            word_count=chapter_data.get("word_count", 0),
            difficulty_level=chapter_data.get("difficulty_level"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            is_published=chapter_data.get("is_published", False)
        )
        self.chapters.append(chapter)
        return chapter

    async def get_chapter_by_id(self, chapter_id: str) -> Optional[TextbookChapter]:
        """
        Retrieve a chapter by its ID
        """
        for chapter in self.chapters:
            if chapter.id == chapter_id:
                return chapter
        return None

    async def get_chapters_by_module(self, module_id: str) -> List[TextbookChapter]:
        """
        Retrieve all chapters belonging to a specific module
        """
        return [chapter for chapter in self.chapters if chapter.module_id == module_id]

    async def get_all_chapters(self) -> List[TextbookChapter]:
        """
        Retrieve all chapters
        """
        return self.chapters

    async def update_chapter(self, chapter_id: str, update_data: dict) -> Optional[TextbookChapter]:
        """
        Update a chapter's information
        """
        for i, chapter in enumerate(self.chapters):
            if chapter.id == chapter_id:
                # Create updated chapter with new data
                updated_data = chapter.dict()
                updated_data.update(update_data)
                updated_data["updated_at"] = datetime.utcnow()

                updated_chapter = TextbookChapter(**updated_data)
                self.chapters[i] = updated_chapter
                return updated_chapter
        return None

    async def delete_chapter(self, chapter_id: str) -> bool:
        """
        Delete a chapter by its ID
        """
        for i, chapter in enumerate(self.chapters):
            if chapter.id == chapter_id:
                del self.chapters[i]
                return True
        return False