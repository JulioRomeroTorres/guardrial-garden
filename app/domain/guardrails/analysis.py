from typing import Optional, Dict, Any, List
from pydantic import BaseModel
from app.domain.contants import DecisionAction

class GuardrailAnalysisResult(BaseModel):
    name: str
    decision: DecisionAction
    results: Optional[List[Dict[str, Any]]] = None
    severity_scale: Optional[int] = 4