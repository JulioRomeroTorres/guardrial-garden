import logging
from typing import Optional
from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.presentation.api.dependencies import (
    get_handle_guardrails_use_case
)
from app.presentation.api.dto import (
    GuardrailsCatalogFilters,
    PagedGuardrailsResponse
)

logger = logging.getLogger(__name__)

BASE_PATH = "/api/v1/guardrails"

router = APIRouter(
    prefix=BASE_PATH
)

@router.post("/")
async def create_guardrial():
    return JSONResponse({}, headers={"status_code": "200"})

@router.get("/")
async def get_guardrails(page: Optional[int] = 1, page_size: Optional[int] = 10, order: Optional[int] = -1):
    filters = GuardrailsCatalogFilters(page=page, limit=page_size, order=order)

    handle_document = get_handle_guardrails_use_case()
    guardials = await handle_document.get_guardrails(filters)

    paged_documents = PagedGuardrailsResponse(
        page=filters.page,
        limit=filters.limit,
        guardials=guardials    
    )
    
    return JSONResponse(paged_documents.model_dump(), headers={"status_code": "200"})

@router.get("/{guardrial_id}/")
async def get_specific_guardrial_information(guardrial_id: str):

    handle_document = get_handle_guardrails_use_case()
    guardial_information = await handle_document.get_specific_guardrail(guardrial_id)
    
    return JSONResponse(guardial_information.format_json(), headers={"status_code": "200"})

@router.put("/{guardrial_id}/")
async def get_specific_guardrial_information(guardial_id: str):
    return JSONResponse({}, headers={"status_code": "200"})