from src.models import SummaryType

PROMPTS = {
    SummaryType.SHORT: """
You are an expert summarizer.

Summarize the following text in 2–3 concise sentences.

Text:
{text}
""",
    SummaryType.MEDIUM: """
You are an expert summarizer.

Summarize the following text in one concise paragraph.

Text:
{text}
""",
    SummaryType.LONG: """
You are an expert summarizer.

Create a detailed summary while preserving all important information.

Text:
{text}
""",
    SummaryType.BULLETS: """
You are an expert summarizer.

Summarize the following text into bullet points.

Text:
{text}
""",
    SummaryType.EXECUTIVE: """
You are writing for business executives.

Create an executive summary highlighting only the most important information.

Text:
{text}
""",
    SummaryType.KEY_TAKEAWAYS: """
Extract the key takeaways from the following text.

Return them as numbered points.

Text:
{text}
""",
}