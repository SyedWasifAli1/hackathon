from fastapi import APIRouter, HTTPException
from typing import List
from ..models.module import Module
from ..services.module_service import ModuleService

router = APIRouter()
module_service = ModuleService()

@router.get("/modules", response_model=List[Module])
async def get_all_modules():
    """
    Retrieve all textbook modules
    """
    modules = await module_service.get_all_modules()
    return modules

@router.get("/modules/{module_id}", response_model=Module)
async def get_module_by_id(module_id: str):
    """
    Retrieve a specific textbook module by ID
    """
    module = await module_service.get_module_by_id(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return module