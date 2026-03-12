import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Optional

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from app.domain.message_store.cosmos_db_credentials import CosmosDbCredentials

class Settings(BaseSettings):
    app_name: str = "Draft Agent"
    api_version: str = os.getenv("API_VERSION") 
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    cors_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://20.14.210.156:3001"
    ]
    
    mongo_db_connection_string: Optional[str] = os.getenv("MONGO_DB_CONNECTION_STRING")
    mongo_db_name: Optional[str] = os.getenv("MONGO_DB_NAME")

    content_safety_endpoint: Optional[str] = os.getenv("CONTENT_SAFETY_ENDPOINT")
    content_safety_api_key: Optional[str] = os.getenv("CONTENT_SAFETY_API_KEY")


    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
