from typing import Optional
from pydantic import BaseModel, Field
from app.domain.contants import OrderEnum

class CommonFilterParams(BaseModel):
    page: Optional[int] = Field(1, ge=1, description="Page number (minimum: 1)")
    limit: Optional[int] = Field(10, ge=1, le=100, description="Items per page (minimum: 1, maximum: 100)")
    order: Optional[int] = OrderEnum.DESC.value