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
Create a comprehensive summary of the provided text.

Requirements:
- Preserve every important concept.
- Explain relationships between ideas.
- Maintain the original logical flow.
- Do not omit important examples.
- Use 2–5 paragraphs depending on the length of the input.
- Do not add headings.
- Do not start with "Summary".
- Do not include introductory phrases.
- Return only the final summary.

Text:
{text}
""",

    SummaryType.BULLETS: """
You are an expert AI assistant specializing in text summarization.

Task:
Summarize the provided text into bullet points.

Requirements:

- Return 5–8 bullets.
- Each bullet must be one sentence.
- Begin every bullet with "-".
- No nested bullets.
- No introduction.
- No conclusion.

Text:
{text}
""",

    SummaryType.EXECUTIVE: """
You are an AI assistant preparing a briefing for senior business executives.

Task:
Create an executive summary of the provided text. Write for senior business executives.

Instructions:
- Focus on the most important insights.
- Highlight objectives, findings, decisions, risks, and outcomes when applicable.
- Keep the summary concise and professional.
- Avoid unnecessary background information.
- Return only the executive summary.

Include:
- Purpose
- Main findings
- Important outcomes
- Recommendations (if present)

Maximum 200 words.

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

Return exactly in this numbered list format:

1.
2.
3.
4.
5.

No heading.
No explanations.
No markdown.

Text:
{text}
""",
}