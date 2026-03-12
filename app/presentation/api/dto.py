from pydantic import BaseModel
from app.domain.contants import DecisionAction
from typing import (
    Any, Optional, List, Literal, Dict
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

MAPPER_CATEGORY_NAME = {
    "Hate": "hate",
    "SelfHarm": "self_harm",
    "Sexual": "sexual",
    "Violence": "violence"
}

class GuardrailAnalysisResponse(BaseModel):
    decision: DecisionAction
    results: Dict[Any, str]
    guardrail_name: Optional[str] = None
    guardrail_id: Optional[str] = None

    def format_json(self):
        return {
            "result": { f"{MAPPER_CATEGORY_NAME[key]}": value for key, value in self.results.items() } ,
            "guardrail_information": {
                "id": self.guardrail_id,
                "name": self.guardrail_name
            }, 
            "is_approved": ( self.decision.value == DecisionAction.ACCEPT.value ),
            "is_by_pass": (( self.decision.value == DecisionAction.BY_PASS.value ))
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
    mode: Optional[str] = "user_input"