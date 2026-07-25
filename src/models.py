from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, field_validator
from src.config import MIN_INPUT_LENGTH, MAX_INPUT_LENGTH

class SummaryType(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"
    BULLETS = "bullets"
    EXECUTIVE = "executive"
    KEY_TAKEAWAYS = "key_takeaways"

class SummaryRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
    )
    
    text: str = Field(
        ...,
        description="Text to summarize",
        min_length=MIN_INPUT_LENGTH,
        max_length=MAX_INPUT_LENGTH,
    )
    
    summary_type: SummaryType = SummaryType.BULLETS
    
    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        if not value:
            raise ValueError("Text cannot be empty")
        
        return value
    
class SummaryResponse(BaseModel):
    summary: str