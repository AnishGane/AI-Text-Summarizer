from enum import Enum
from pydantic import BaseModel, Field, ConfigDict 

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
    )
    
    summary_type: SummaryType = SummaryType.MEDIUM
    
class SummaryResponse(BaseModel):
    summary: str