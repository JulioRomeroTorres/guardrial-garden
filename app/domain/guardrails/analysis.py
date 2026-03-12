from typing import Optional, Dict, Any
from pydantic import BaseModel
from app.domain.contants import DecisionAction
from azure.ai.contentsafety.models import TextCategory

class GuardrailAnalysisResult(BaseModel):
    name: str
    decision: DecisionAction
    results: Optional[Dict[Any, str]] = None