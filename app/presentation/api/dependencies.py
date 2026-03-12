from app.application.use_cases.handle_guardrials_information import (
    HandleGuardrailsUseCase
)
from app.application.use_cases.handle_analyze_text import (
    HandleAnalyzeTextUseCase
)
from app.infrastructure.container import get_container

def get_handle_guardrails_use_case() -> HandleGuardrailsUseCase:
    return get_container().get_handle_guardrails_use_case()

def get_handle_analyze_text_use_case() -> HandleAnalyzeTextUseCase:
    return get_container().get_handle_analyze_text_use_case()
