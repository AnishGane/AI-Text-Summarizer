# contains business logics

from src.prompts import PROMPTS
from src.llm import generate_response
from src.models import (
    SummaryRequest,
    SummaryResponse
)

def summarize_text(request: SummaryRequest) -> SummaryResponse:
    """Summarize the text provided by the user"""

    prompt = PROMPTS[request.summary_type].format(text=request.text)

    summary = generate_response(prompt)

    return SummaryResponse(summary=summary)