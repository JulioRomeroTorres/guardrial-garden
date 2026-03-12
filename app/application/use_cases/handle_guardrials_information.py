from typing import (
    Any, List, Any
)
from app.domain.guardrails.core_information import (
    GuardrailInformation, CoreGuardrialInformation
)
from app.application.services.guardrail_information_manager import GuardrailInformationManager

class HandleGuardrailsUseCase:
    def __init__(self, guardrail_information_manager: GuardrailInformationManager):
        self.guardrail_information_manager = guardrail_information_manager
        pass
    
    async def get_guardrails(self, filters: Any) -> List[CoreGuardrialInformation]:
        return await self.guardrail_information_manager.get_guardrails(filters)

    async def get_specific_guardrail(self, guardial_id: str) -> GuardrailInformation:
        return await self.guardrail_information_manager.get_specific_guardrail(guardial_id)