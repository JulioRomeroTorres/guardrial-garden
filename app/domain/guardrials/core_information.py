
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class GuardialMetadata(BaseModel):
    created_by: str
    created_at: str
    updated_at: str
    tags: Optional[List[str]]

class GuardialSettings(BaseModel):
    tuning_parameters: Dict[str, int]

class CoreGuardrialInformation(BaseModel):
    guardial_id: str
    name: str
    version: str
    description: str
    is_active: bool

class GuardrialInformation(CoreGuardrialInformation):
    category: str
    settings: GuardialSettings
    metadata: GuardialMetadata

