from typing import Any
from functools import lru_cache
from app.config import get_settings

from app.application.use_cases.handle_guardrials_information import (
    HandleGuardrailsUseCase
)

from app.application.use_cases.handle_analyze_text import (
    HandleAnalyzeTextUseCase
)

from app.application.services.content_analyzer_manager import ContentAnalyzerManager
from app.application.services.guardrail_information_manager import GuardrailInformationManager

from app.infrastructure.repository.mongo_db import MongoDbRepository
from app.infrastructure.repository.content_safety import ContentSafetyGuardilRepository

from pymongo import AsyncMongoClient
from app.infrastructure.managers.http_manager import HttpRepositoryManager
from azure.ai.contentsafety.aio import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential

class DependencyContainer:
    def __init__(self):
        self._instances = {}
        self._factories = {}
        self._initialized = False
        self._db_client = None
        self._storage_client = None
        self._content_safety_client = None

    def _ensure_initialized(self):
        if self._initialized:
            return

        settings = get_settings()
        
        self._factories["db_repository"] = lambda: MongoDbRepository(self._get_db_client(), settings.mongo_db_name, "guardrail_information")        
        self._factories["content_safety_repository"] = lambda: ContentSafetyGuardilRepository(self._get_content_safety_client())
        
        self._factories["guardrail_information_manager"] = lambda: GuardrailInformationManager(
            self.get('db_repository')
        )

        self._factories["content_analyzer_manager"] = lambda: ContentAnalyzerManager(
                self.get('content_safety_repository')
            )

        self._initialized = True

    def get(self, service_name: str) -> Any:
        self._ensure_initialized()

        if service_name not in self._instances:
            if service_name not in self._factories:
                raise ValueError(f"Unknown service: {service_name}")
            self._instances[service_name] = self._factories[service_name]()

        return self._instances[service_name]

    def get_handle_guardrails_use_case(self) -> HandleGuardrailsUseCase:
        return HandleGuardrailsUseCase(
            guardrail_information_manager=self.get("guardrail_information_manager")
        )

    def get_handle_analyze_text_use_case(self) -> HandleAnalyzeTextUseCase:
          return HandleAnalyzeTextUseCase(
            guardrail_information_manager=self.get("guardrail_information_manager"),
            content_analyzer_manager=self.get("content_analyzer_manager"),
        )

    def clear(self):
        self._instances.clear()
        self._initialized = False
    
    def _get_db_client(self) -> AsyncMongoClient:
        if self._db_client is None:
            settings = get_settings()
            self._db_client = AsyncMongoClient(settings.mongo_db_connection_string)
        return self._db_client

    def _get_content_safety_client(self) -> AsyncMongoClient:
        if self._content_safety_client is None:
            settings = get_settings()
            self._content_safety_client = ContentSafetyClient(
                settings.content_safety_endpoint,
                AzureKeyCredential(settings.content_safety_api_key)
            )
            
        return self._content_safety_client

    async def close_all(self):
        
        print("Closing all connection...")
        if self._db_client:
            await self._db_client.close()
        
        if self._content_safety_client:
            await self._content_safety_client.close()

        await HttpRepositoryManager.close_all_sessions()

        self.clear()
        print("All connection are closed")

@lru_cache
def get_container() -> DependencyContainer:
    return DependencyContainer()
