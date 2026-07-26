import streamlit as st
from src.models import SummaryType, SummaryRequest
from src.services.summarizer import summarize_text
from pydantic import ValidationError
from src.exceptions import PromptError, GeminiAPIError
# from src.services.pdf_service import extract_text_from_pdf
from src.components.sidebar import render_sidebar
from src.components.input import render_input
from src.components.output import render_output
from src.utils import load_css
import time

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📃",
    layout="centered"
)

load_css()

if "summary" not in st.session_state:
    st.session_state.summary = ""
    
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "summary_type" not in st.session_state:
    st.session_state.summary_type = SummaryType.SHORT
    
if "last_summarized_text" not in st.session_state:
            st.session_state.last_summarized_text = ""
    
st.title("AI Text Summarizer")

render_sidebar()

text, uploaded_pdf, summary_type, summarize = render_input()

if summarize:
    try:
        request = SummaryRequest(
            text=text,
            summary_type=summary_type,
        )

        with st.spinner("Generating summary..."):
            start = time.time()
            response = summarize_text(request)
            elapsed_time = time.time() - start
            
            st.info(f"Summary generated in {elapsed_time:.2f} seconds")

        st.session_state.last_summarized_text = text
        st.session_state.summary = response.summary
        st.session_state.summary_type = summary_type

    except ValidationError as e:
        st.error(str(e))

    except PromptError as e:
        st.error(str(e))

    except GeminiAPIError as e:
        st.error(str(e))

render_output()