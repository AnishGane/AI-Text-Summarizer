from pathlib import Path
import streamlit as st
import re

def load_css():
    css_path = Path("assets/style.css")
    
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
def summary_stats():
    summary = st.session_state.summary
    
    words = len(summary.split())
    chars_num = len(summary)
    minutes = round(words / 200, 2)
    
    return words, chars_num, minutes

def user_input_stats():
    words = len(st.session_state.input_text.split())
    chars_num = len(st.session_state.input_text)
    
    return words, chars_num

def clear_session():
    
    keys = [
        "input_text",
        "summary",
        "uploaded_pdf",
        "summary_type",
        "last_summarized_text"
    ]
    
    for key in keys:
        st.session_state.pop(key, None)

    st.rerun()
    

def clean_summary(text: str) -> str:
    text = text.strip()
    
    patterns = [
        r"^\*\*Summary:?\*\*",
        r"^Summary:?",
        r"^\*\*Draft:?\*\*",
        r"^Draft:?",
    ]
    
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        
    return text.strip()