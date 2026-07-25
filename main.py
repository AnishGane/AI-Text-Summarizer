from pydantic import ValidationError
from src.models import SummaryRequest
from src.summarizer import summarize_text
from src.exceptions import (
    PromptError,
    GeminiAPIError
)
from src.logger import logger
import logging

logger = logging.getLogger(__name__)

try:
    request = SummaryRequest(
        text="""
            Artificial Intelligence is changing healthcare
            through better diagnosis,
            drug discovery,
            and personalized medicine.
            """
    )

    response = summarize_text(request)

    print(response.summary)

except ValidationError as e:
    logger.warning("Input validation failed.")
    print(e)

except PromptError as e:
    logger.warning("Prompt generation failed.")
    print(e)

except GeminiAPIError as e:
    logger.error("Communication with Gemini API failed.")
    print(e)