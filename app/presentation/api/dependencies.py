from app.application.use_cases.handle_guardrials_information import (
    HandleGuardrialsUseCase
)
from app.application.use_cases.handle_analyze_text import (
    HandleAnalyzeTextUseCase
)
from app.infrastructure.container import get_container

def get_handle_guardials_use_case() -> HandleGuardrialsUseCase:
    return get_container().get_handle_guardials_use_case()

def get_handle_analyze_text_use_case() -> HandleAnalyzeTextUseCase:
    return get_container().get_handle_analyze_text_use_case()
