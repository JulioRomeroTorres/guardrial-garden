from pydantic import BaseModel
from typing import Any, Optional, List, Any
from app.domain.filter.paged_information import CommonFilterParams
from app.domain.guardrials.core_information import GuardrialInformation

class GuardrialsCatalogFilters(CommonFilterParams):
    pass

class PagedGuardrialsResponse(CommonFilterParams):
    guardials: List[Any]

class GuardrialInformationResponse(GuardrialInformation):
    pass

class GuardrialAnalysisResponse(BaseModel):
    is_approved: bool
    result: Any

class TunningGuardrialsParameters:
    hate: int
    self_harm: int
    sexual: int
    violence: int
    prompt: Optional[str] = None

class CustomGuardrialRequest(BaseModel):
    message: str
    tunning_parameters: TunningGuardrialsParameters
    