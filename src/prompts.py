from src.models import SummaryType

PROMPTS = {
    SummaryType.SHORT: """
You are an expert AI assistant specializing in text summarization.

Task:
Generate a short, concise summary of the provided text.

Instructions:
- Keep the summary between 2 and 3 sentences.
- Preserve the main idea and key facts.
- Use clear and natural language.
- Do not add information that is not present in the original text.
- Do not include headings, labels, introductions, or conclusions.
- Return only the summary.

Text:
{text}
""",

    SummaryType.MEDIUM: """
You are an expert AI assistant specializing in text summarization.

Task:
Generate a medium-length summary of the provided text.

Instructions:
- Write a single well-structured paragraph.
- Preserve the important information while removing unnecessary details.
- Keep the language professional and easy to read.
- Do not add new information.
- Do not include headings or explanatory text.
- Return only the summary.

Text:
{text}
""",

    SummaryType.LONG: """
You are an expert AI assistant specializing in text summarization.

Task:
Generate a detailed summary of the provided text.

Instructions:
- Preserve all major ideas and supporting details.
- Organize the information logically.
- Keep the writing clear and coherent.
- Do not repeat information unnecessarily.
- Do not invent or infer facts.
- Do not include titles or commentary.
- Return only the summary.

Text:
{text}
""",

    SummaryType.BULLETS: """
You are an expert AI assistant specializing in text summarization.

Task:
Summarize the provided text into bullet points.

Instructions:
- Use Markdown bullet points.
- Write between 5 and 8 bullets.
- Each bullet should contain one key idea.
- Keep bullets concise and informative.
- Do not include introductory or closing sentences.
- Return only the bullet list.

Text:
{text}
""",

    SummaryType.EXECUTIVE: """
You are an AI assistant preparing a briefing for senior business executives.

Task:
Create an executive summary of the provided text.

Instructions:
- Focus on the most important insights.
- Highlight objectives, findings, decisions, risks, and outcomes when applicable.
- Keep the summary concise and professional.
- Avoid unnecessary background information.
- Return only the executive summary.

Text:
{text}
""",

    SummaryType.KEY_TAKEAWAYS: """
You are an expert AI assistant specializing in extracting insights.

Task:
Identify the key takeaways from the provided text.

Instructions:
- Return between 5 and 10 numbered points.
- Each point should represent one important insight.
- Keep each point concise.
- Do not repeat information.
- Do not include introductory text.
- Return only the numbered list.

Text:
{text}
""",
}