from enum import Enum
from typing import Dict, Literal

DEFAULT_K_NEAREST_NEIGHBORS = 50
DEFAULT_TOP_ITEMS = 5

class DecisionAction(Enum):
    ACCEPT = "Accept"
    REJECT = "Reject"

MEDIA_FILE_MAPPER = {
    'pdf': 'application/pdf',
    'jpg': 'image/jpeg',
    'png': 'image/png',
    'jpeg': 'image/jpeg',
    'pptx': 'application/octet-stream',
    'docx': 'application/octet-stream',
    'txt': 'application/octet-stream'
}

class LlmProviderEnum(Enum):
    OPEN_AI = "Open Ai"
    ANTHROPIC = "Anthropic"
    DEEP_SEEK = "Deep Seek"

DEFAULT_MODEL_NAME = "gpt-4o-mini"

class SummarizeModelAvailable(Enum):
    GPT_4O_MINI= "gpt-4o-mini"
    GPT_4O= "gpt-4o"
    GPT_4_1_MINI= "gpt-4.1-mini"
    GPT_4_1= "gpt-4.1"
    
MODEL_SUMMARIZE_VERSION: Dict[SummarizeModelAvailable, str] = {
    SummarizeModelAvailable.GPT_4O_MINI: "2025-01-01-preview",
    SummarizeModelAvailable.GPT_4O: "2025-01-01-preview",
    SummarizeModelAvailable.GPT_4_1_MINI: "2025-01-01-preview",
    SummarizeModelAvailable.GPT_4_1: "2025-01-01-preview"
}

class OrderEnum(Enum):
    ASC = 1
    DESC = -1

MAPPER_SEVERITY_SCALE: Dict[int, Literal["FourSeverityLevels","EightSeverityLevels"]] = {
    4: "FourSeverityLevels",
    8: "EightSeverityLevels"
}