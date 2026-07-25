import streamlit as st
from src.models import SummaryType, SummaryRequest
from src.summarizer import summarize_text
from pydantic import ValidationError
from src.exceptions import PromptError, GeminiAPIError

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📃",
    layout="centered"
)

st.title("AI Text Summarizer")

st.write(
    "Summarize long text into concise summaries using Google's Gemini."
)

text = st.text_area("Enter your text to summarize:", 
                        height=300,
                        placeholder="Paste your article here..."
                )

summary_type = st.selectbox(
    "Summary Type",
    options=list(SummaryType),
    format_func=lambda x: x.replace("_", " ").title(),
)

summarize_button = st.button(
    "Generate Summary",
    use_container_width=True,
    disabled= not text.strip(),
)

if summarize_button:
    try:
        request = SummaryRequest(text = text, summary_type = summary_type)

        with st.spinner("Wait a moment, Generating summary..."):
            response = summarize_text(request)

        st.success("Summary generated successfully!")

        st.subheader("Summary")
        st.text_area(
            value=response.summary,
            height=200         
        )
        
    except ValidationError as e:
        st.error(str(e))

    except PromptError as e:
        st.error(str(e))

    except GeminiAPIError as e:
        st.error(str(e))