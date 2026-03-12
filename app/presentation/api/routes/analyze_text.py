import logging
from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Form

from starlette.responses import JSONResponse

from app.presentation.api.dependencies import (
    get_handle_analyze_text_use_case
)
from app.presentation.api.dto import (
    CustomGuardrialRequest,
    GuardrialAnalysisResponse
)

logger = logging.getLogger(__name__)

BASE_PATH = "/api/v1/analyze-text"

router = APIRouter(
    prefix=BASE_PATH
)

@router.post("/{guardial_id}/")
async def analyze_text_by_catalog_guardial(guardial_id: str):

    handle_analyze_text = get_handle_analyze_text_use_case()
    decision, analysis_result = await handle_analyze_text.analyze_content_by_guardial(guardial_id)
    
    guardial_analysis_result = GuardrialAnalysisResponse(
        is_approved=decision == "1",
        result=analysis_result
    )
    
    return JSONResponse(guardial_analysis_result.model_dump(), headers={"status_code": "200"})

@router.get("/custom-guardial/")
async def analyze_text_by_custom_guardial(tunning_parameters: CustomGuardrialRequest):

    handle_analyze_text = get_handle_analyze_text_use_case()
    decision, analysis_result = await handle_analyze_text.analyze_content_by_parameters(tunning_parameters)

    guardial_analysis_result = GuardrialAnalysisResponse(
        is_approved= (decision == 1),
        result=analysis_result
    )
    
    return JSONResponse(guardial_analysis_result.model_dump(), headers={"status_code": "200"})