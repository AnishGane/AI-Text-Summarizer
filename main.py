from pydantic import ValidationError
from src.models import SummaryRequest
from src.summarizer import summarize_text
from src.exceptions import (
    PromptError,
    GeminiAPIError
)

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
    print("\nInput validation failed:")
    print(e)

except PromptError as e:
    print("Prompt Error")
    print(e)

except GeminiAPIError as e:
    print("Gemini Error")
    print(e)