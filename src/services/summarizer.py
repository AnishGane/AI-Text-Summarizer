# contains business logics
from src.llm import generate_response
from src.models import (
    SummaryRequest,
    SummaryResponse
)
from src.exceptions import PromptError
from src.logger import logger
import logging
from src.utils import clean_summary
from src.prompts.prompt_builder import build_prompt

logger = logging.getLogger(__name__)

def summarize_text(request: SummaryRequest) -> SummaryResponse:
    logger.info(
        "Generating %s summary",
        request.summary_type.value
    )
    try:
        prompt = build_prompt(request.summary_type, request.text)
    except KeyError as e:
        logger.error("Invalid summary type: %s", request.summary_type)
        raise PromptError(f"No prompt found for summary type: {request.summary_type}") from e
    
    response = generate_response(prompt)
    
    response = clean_summary(response)
    
    logger.info("Summary generated successfully.")
    
    return SummaryResponse(summary=response)