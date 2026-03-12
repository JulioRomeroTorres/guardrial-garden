from app.domain.contants import DecisionAction
from typing import Dict, Any, List, Optional, Tuple
from azure.ai.contentsafety.models import TextCategory
from app.domain.repository.content_safety_repository import IContentSafetyRepository

class ContentAnalyzerManager:
    def __init__(self, content_safety_repository: IContentSafetyRepository):
        self.content_safety_repository = content_safety_repository
        pass
    
    async def analyze_content(self, 
                              message: str, reject_thresholds: Dict[str, Any], 
                              block_list: Optional[List[str]] = []) -> Tuple[DecisionAction, List[TextCategory]]:
        
        analisis_result = await self.content_safety_repository.analyze_text(message, block_list)
        return await self.content_safety_repository.make_decision(analisis_result, reject_thresholds)