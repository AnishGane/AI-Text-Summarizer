import streamlit as st
from src.models import SummaryType, SummaryRequest
from src.summarizer import summarize_text
from pydantic import ValidationError
from src.exceptions import PromptError, GeminiAPIError

st.markdown(
    """
    <style>
    textarea {
        resize: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📃",
    layout="centered"
)

st.title("AI Text Summarizer")

st.write(
    "Summarize long text into concise summaries using Google's Gemini."
)

st.subheader("Enter your text to summarize")
text = st.text_area("", 
                        height=300,
                        placeholder="Paste your article here..."
                )

col1, col2 = st.columns(2)

with col1:
    summary_type = st.selectbox(
        "Summary Type",
        options=list(SummaryType),
        format_func=lambda x: x.replace("_", " ").title(),
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
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
            "",
            value=response.summary,
            height=200         
        )
        
    except ValidationError as e:
        st.error(str(e))

    except PromptError as e:
        st.error(str(e))

    except GeminiAPIError as e:
        st.error(str(e))