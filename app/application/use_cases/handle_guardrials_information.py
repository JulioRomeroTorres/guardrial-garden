from typing import (
    Any, List, Any
)
from app.domain.guardrials.core_information import (
    GuardrialInformation, CoreGuardrialInformation
)
from app.application.services.guardrial_information_manager import GuardrialInforamationManager

class HandleGuardrialsUseCase:
    def __init__(self, guardrial_information_manager: GuardrialInforamationManager):
        self.guardrial_information_manager = guardrial_information_manager
        pass
    
    async def get_guardrials(self, filters: Any) -> List[CoreGuardrialInformation]:
        return await self.guardrial_information_manager.get_guardrials(filters)

    async def get_specific_guardrial(self, guardial_id: str) -> GuardrialInformation:
        return await self.guardrial_information_manager.get_specific_guardrial(guardial_id)