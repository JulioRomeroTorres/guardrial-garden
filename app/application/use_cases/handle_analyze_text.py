from typing import (
    Tuple, Any, Dict
)
from app.application.services.guardrial_information_manager import GuardrialInforamationManager
from app.application.services.content_analyzer_manager import ContentAnalyzerManager

class HandleAnalyzeTextUseCase:
    def __init__(self, 
                 guardrial_information_manager: GuardrialInforamationManager,
                 content_analyzer_manager: ContentAnalyzerManager):
        
        self.guardrial_information_manager = guardrial_information_manager
        self.content_analyzer_manager = content_analyzer_manager
    
    async def analyze_content_by_parameters(self, message: str, parameters: Dict[str, Any]) -> Tuple[Any, Any]:
        decision, results = await self.content_analyzer_manager.analyze_content(
            message,
            parameters
            )
        return decision, results

    async def analyze_content_by_guardial(self, message: str, guardial_id: str) -> Tuple[Any, Any]:
        guardrial_information = await self.guardrial_information_manager.get_specific_guardrial(guardial_id)
        decision, results = await self.analyze_content_by_parameters(message, guardrial_information.settings.tuning_parameters)
        return decision, results