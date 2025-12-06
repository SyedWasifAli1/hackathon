from fastapi import APIRouter, HTTPException
from typing import List
from ..models.chapter import TextbookChapter
from ..services.chapter_service import ChapterService

router = APIRouter()
chapter_service = ChapterService()

@router.get("/chapters", response_model=List[TextbookChapter])
async def get_all_chapters():
    """
    Retrieve all textbook chapters
    """
    chapters = await chapter_service.get_all_chapters()
    return chapters

@router.get("/chapters/{chapter_id}", response_model=TextbookChapter)
async def get_chapter_by_id(chapter_id: str):
    """
    Retrieve a specific textbook chapter by ID
    """
    chapter = await chapter_service.get_chapter_by_id(chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter

@router.get("/chapters/module/{module_id}", response_model=List[TextbookChapter])
async def get_chapters_by_module(module_id: str):
    """
    Retrieve all chapters for a specific module
    """
    chapters = await chapter_service.get_chapters_by_module(module_id)
    return chapters