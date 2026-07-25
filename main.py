from src.models import (
    SummaryRequest,
    SummaryType,
)
from src.summarizer import summarize_text

request = SummaryRequest(
    text="""
Artificial Intelligence is changing healthcare
through better diagnosis,
drug discovery,
and personalized medicine.
""",
    summary_type=SummaryType.BULLETS,
)

response = summarize_text(request)

print(response.summary)