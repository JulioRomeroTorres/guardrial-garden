from typing import Any, List
from app.domain.filter.paged_information import CommonFilterParams
from app.domain.guardrails.core_information import (
    CoreGuardrialInformation, GuardrailInformation
) 
from app.domain.repository.item_sql_repository import IItemSqlRepository

class GuardrailInformationManager:

    def __init__(self, db_repository: IItemSqlRepository):
        self.db_repository = db_repository

    async def get_guardrails(self, filters: CommonFilterParams) -> List[CoreGuardrialInformation]:

        guardrials_list = await self.db_repository.get_paged_items(
            filters.page,
            filters.limit,
            "metadata.created_at"
        )

        return [ CoreGuardrialInformation(**guardrial_information) for guardrial_information in guardrials_list ]
    
    async def get_specific_guardrail(self, guardial_id: str) -> GuardrailInformation:
        guardrial_information = await self.db_repository.get_items_by_filter({"guardrail_id": guardial_id}, length=1)
        return GuardrailInformation(**guardrial_information[0])