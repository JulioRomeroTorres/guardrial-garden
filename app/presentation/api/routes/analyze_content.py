import logging
from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form

from starlette.responses import JSONResponse

from app.presentation.api.dependencies import (
    get_handle_analyze_text_use_case
)
from app.presentation.api.dto import (
    CustomGuardrailRequest,
    AnalyzeContentRequest,
    GuardrailAnalysisResponse
)

logger = logging.getLogger(__name__)

BASE_PATH = "/api/v1/analyze-content"

router = APIRouter(
    prefix=BASE_PATH
)

@router.post("/{guardial_id}/")
async def analyze_text_by_catalog_guardial(guardial_id: str, analzy_content_request: AnalyzeContentRequest):

    handle_analyze_text = get_handle_analyze_text_use_case()
    guardrail_result = await handle_analyze_text.analyze_content_by_guardial(analzy_content_request.message, guardial_id, analzy_content_request.mode)
    
    guardial_analysis_result = GuardrailAnalysisResponse(
        decision=guardrail_result.decision,
        analysis=guardrail_result.results,
        guardrail_name=guardrail_result.name,
        guardrail_id=guardial_id,
        severity_scale=guardrail_result.severity_scale
    )
    
    return JSONResponse(guardial_analysis_result.format_json(), headers={"status_code": "200"})

@router.get("/custom-validation/")
async def analyze_text_by_custom_guardial(custom_guardrial_request: CustomGuardrailRequest):

    handle_analyze_text = get_handle_analyze_text_use_case()
    decision, analysis_result = await handle_analyze_text.analyze_content_by_parameters(custom_guardrial_request.tunning_parameters.format_json(), custom_guardrial_request.severity_scale)

    guardial_analysis_result = GuardrailAnalysisResponse(
        decision=decision,
        analysis=analysis_result,
        severity_scale=custom_guardrial_request.severity_scale
    )
    
    return JSONResponse(guardial_analysis_result.format_json(), headers={"status_code": "200"})