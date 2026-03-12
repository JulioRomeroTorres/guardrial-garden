from typing import (
    Tuple, Any, Dict
)
from app.application.services.guardrail_information_manager import GuardrailInformationManager
from app.application.services.content_analyzer_manager import ContentAnalyzerManager, AnalysisResultType

class HandleAnalyzeTextUseCase:
    def __init__(self, 
                 guardrail_information_manager: GuardrailInformationManager,
                 content_analyzer_manager: ContentAnalyzerManager):
        
        self.guardrail_information_manager = guardrail_information_manager
        self.content_analyzer_manager = content_analyzer_manager
    
    async def analyze_content_by_parameters(self, message: str, parameters: Dict[str, Any]) -> AnalysisResultType:
        decision, results = await self.content_analyzer_manager.analyze_content(
            message,
            parameters
            )
        return decision, results

    async def analyze_content_by_guardial(self, message: str, guardial_id: str) -> AnalysisResultType:
        guardrial_information = await self.guardrail_information_manager.get_specific_guardrail(guardial_id)
        decision, results = await self.analyze_content_by_parameters(message, guardrial_information.settings.tuning_parameters)
        return decision, results