from typing import List, Optional
from ..models.module import Module
from uuid import uuid4
from datetime import datetime


class ModuleService:
    """
    Service class to handle business logic for textbook modules
    """

    def __init__(self):
        # In a real implementation, this would connect to a database
        self.modules: List[Module] = []

    async def create_module(self, module_data: dict) -> Module:
        """
        Create a new textbook module
        """
        module = Module(
            id=str(uuid4()),
            title=module_data.get("title"),
            slug=module_data.get("slug"),
            description=module_data.get("description"),
            week_number=module_data.get("week_number"),
            learning_goals=module_data.get("learning_goals", []),
            prerequisites=module_data.get("prerequisites", []),
            estimated_duration=module_data.get("estimated_duration", 0),
            is_active=module_data.get("is_active", True),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.modules.append(module)
        return module

    async def get_module_by_id(self, module_id: str) -> Optional[Module]:
        """
        Retrieve a module by its ID
        """
        for module in self.modules:
            if module.id == module_id:
                return module
        return None

    async def get_all_modules(self) -> List[Module]:
        """
        Retrieve all modules
        """
        return self.modules

    async def update_module(self, module_id: str, update_data: dict) -> Optional[Module]:
        """
        Update a module's information
        """
        for i, module in enumerate(self.modules):
            if module.id == module_id:
                # Create updated module with new data
                updated_data = module.dict()
                updated_data.update(update_data)
                updated_data["updated_at"] = datetime.utcnow()

                updated_module = Module(**updated_data)
                self.modules[i] = updated_module
                return updated_module
        return None

    async def delete_module(self, module_id: str) -> bool:
        """
        Delete a module by its ID
        """
        for i, module in enumerate(self.modules):
            if module.id == module_id:
                del self.modules[i]
                return True
        return False