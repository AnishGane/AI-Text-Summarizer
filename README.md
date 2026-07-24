## AI Text Summarizer

#### Work flow till now:

1. main.py -> contains sample_text for now and calls the summarize_text(text) and prints the generated summary response text
2. summarizer.py -> has summarize_text(text) that calls the generate_response(prompt)
3. prompts.py -> contains SUMMARY_PROMPT that has {text}
4. llm.py -> has generate_response(prompt), that call the gemini api for returning the response.text
