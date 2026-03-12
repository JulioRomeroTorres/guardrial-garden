
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class GuardialMetadata(BaseModel):
    created_by: str
    created_at: datetime
    updated_at: datetime
    tags: Optional[List[str]] = None

    def format_json(self):
        return {
            "created_by": self.created_by,
            "created_at": self.created_at.strftime('%m/%d/%Y, %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%m/%d/%Y, %H:%M:%S'),
            "tags": self.tags
        }

class GuardialSettings(BaseModel):
    tuning_parameters: Dict[str, int]

class CoreGuardrialInformation(BaseModel):
    guardrail_id: str
    name: str
    version: str
    description: str
    is_active: bool

class GuardrailInformation(CoreGuardrialInformation):
    category: str
    settings: GuardialSettings
    metadata: GuardialMetadata

    def format_json(self):
        return {
            "guardrail_id": self.guardrail_id,
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "is_active": self.is_active,
            "category": self.category,
            "settings": self.settings.model_dump(),
            "metadata": self.metadata.format_json()
        }
