from src.models import SummaryType
from src.prompts.summary_prompt import PROMPTS
from src.prompts.system_prompt import SYSTEM_PROMPT

def build_prompt(summary_type: SummaryType, text: str) -> str:
    
    task_prompt = PROMPTS[summary_type].format(text=text)
    
    return f"{SYSTEM_PROMPT}\n\n{task_prompt}"