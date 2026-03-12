from pydantic import BaseModel
from app.domain.contants import DecisionAction
from typing import (
    Any, Optional, List, Literal
) 
from app.domain.filter.paged_information import CommonFilterParams
from app.domain.guardrails.core_information import GuardrailInformation
from azure.ai.contentsafety.models import TextCategory

class GuardrailsCatalogFilters(CommonFilterParams):
    pass

class PagedGuardrailsResponse(CommonFilterParams):
    guardials: List[Any]

class GuardrailInformationResponse(GuardrailInformation):
    pass

class GuardrailAnalysisResponse(BaseModel):
    is_approved: DecisionAction
    result: Any

    def format_json(self):
        return {
            **self.model_dump(),
            "is_approved": ( self.is_approved.value == DecisionAction.ACCEPT.value ),
        } 

class TunningGuardrailsParameters(BaseModel):
    hate: int
    self_harm: int
    sexual: int
    violence: int
    prompt: Optional[str] = None

    def format_json(self):
        return {
            "Hate": self.hate,
            "SelfHarm": self.self_harm,
            "Violence": self.violence,
            "Sexual": self.sexual
        }

class CustomGuardrailRequest(BaseModel):
    message: str
    tunning_parameters: TunningGuardrailsParameters
    severity_scale: Optional[Literal[4, 8]] = 4

class AnalyzeContentRequest(BaseModel):
    message: str