import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("⚙️ Settings")

        st.markdown("### About")
        
        st.info(
            """
             **AI Text Summarizer**

            Powered by Google Gemini.

            Upload a PDF or paste text to generate
            concise AI summaries.
            """
        )
        
        st.divider()

        st.caption("Made with ❤️ using Streamlit")