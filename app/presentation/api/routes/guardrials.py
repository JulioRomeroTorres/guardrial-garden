import logging
from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.presentation.api.dependencies import (
    get_handle_guardials_use_case
)
from app.presentation.api.dto import (
    GuardrialsCatalogFilters,
    PagedGuardrialsResponse
)

logger = logging.getLogger(__name__)

BASE_PATH = "/api/v1/guardrials"

router = APIRouter(
    prefix=BASE_PATH
)

@router.post("/")
async def create_guardrial():
    return JSONResponse({}, headers={"status_code": "200"})

@router.get("/")
async def get_guardrials(filters: GuardrialsCatalogFilters):

    handle_document = get_handle_guardials_use_case()
    guardials = await handle_document.get_guardrials(filters)

    uploaded_document = PagedGuardrialsResponse(
        page=filters.page,
        limit=filters.limit,
        guardials=guardials    
    )
    
    return JSONResponse(uploaded_document.model_dump(), headers={"status_code": "200"})

@router.get("/{guardrial_id}/")
async def get_specific_guardrial_information(guardrial_id: str):

    handle_document = get_handle_guardials_use_case()
    guardial_information = await handle_document.get_specific_guardrial(guardrial_id)
    
    return JSONResponse(guardial_information.model_dump(), headers={"status_code": "200"})

@router.put("/{guardrial_id}/")
async def get_specific_guardrial_information(guardial_id: str):
    return JSONResponse({}, headers={"status_code": "200"})