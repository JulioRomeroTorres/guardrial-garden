from typing import Any, List
from app.domain.guardrials.core_information import (
    CoreGuardrialInformation, GuardrialInformation
) 
from app.domain.repository.item_sql_repository import IItemSqlRepository

class GuardrialInforamationManager:

    def __init__(self, db_repository: IItemSqlRepository):
        self.db_repository = db_repository

    async def get_guardrials(self, filters: Any) -> List[CoreGuardrialInformation]:
        guardrials_list = await self.db_repository.get_paged_items(filters)
        return [ CoreGuardrialInformation(**guardrial_information) for guardrial_information in guardrials_list ]
    
    async def get_specific_guardrial(self, guardial_id: str) -> GuardrialInformation:
        guardrial_information = await self.db_repository.get_item_by_id(guardial_id)
        return GuardrialInformation(**guardrial_information)