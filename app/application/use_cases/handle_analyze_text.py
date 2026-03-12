from typing import (
    Any, Dict, Optional, Literal
)
from app.domain.contants import MAPPER_SEVERITY_SCALE
from app.application.services.guardrail_information_manager import GuardrailInformationManager
from app.application.services.content_analyzer_manager import ContentAnalyzerManager, AnalysisResultType

class HandleAnalyzeTextUseCase:
    def __init__(self, 
                 guardrail_information_manager: GuardrailInformationManager,
                 content_analyzer_manager: ContentAnalyzerManager):
        
        self.guardrail_information_manager = guardrail_information_manager
        self.content_analyzer_manager = content_analyzer_manager
    
    async def analyze_content_by_parameters(self, message: str, parameters: Dict[str, Any], severity_scale: Optional[Literal[4,8]] = 4) -> AnalysisResultType:
        decision, results = await self.content_analyzer_manager.analyze_content(
            message,
            parameters,
            severity_scale=MAPPER_SEVERITY_SCALE[severity_scale]
            )
        return decision, results

    async def analyze_content_by_guardial(self, message: str, guardial_id: str) -> AnalysisResultType:
        guardrial_information = await self.guardrail_information_manager.get_specific_guardrail(guardial_id)
        tunnig_parameters_information = guardrial_information.settings

        decision, results = await self.analyze_content_by_parameters(message, tunnig_parameters_information.tuning_parameters, tunnig_parameters_information.severity_scale)
        return decision, results