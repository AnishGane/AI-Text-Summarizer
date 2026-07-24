# contains business logics

from src.prompts import SUMMARY_PROMPT
from src.llm import generate_response

def summarize_text(text: str)->str:
    """Summarize the text provided by the user"""

    prompt = SUMMARY_PROMPT.format(text=text)

    return generate_response(prompt)