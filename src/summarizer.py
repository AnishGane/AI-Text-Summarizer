# contains business logics

from src.prompts import PROMPTS
from src.llm import generate_response
from src.models import (
    SummaryRequest,
    SummaryResponse
)
from src.exceptions import PromptError

def summarize_text(request: SummaryRequest) -> SummaryResponse:
   try:
       prompt = PROMPTS[request.summary_type].format(text=request.text)
   except Exception as e:
       raise PromptError(f"No prompt found for summary type: {request.summary_type}") from e
   
   response = generate_response(prompt)
   
   return SummaryResponse(summary=response)