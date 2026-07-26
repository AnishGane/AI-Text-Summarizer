import streamlit as st
from src.utils import summary_stats

def render_output():
    if not st.session_state.summary:
        return
    
    with st.container(border=True):
        col1, col2 = st.columns([2, 1.5])

        with col1:
            st.subheader("✨ Summary")
        
        with col2:
            st.markdown("\n", unsafe_allow_html=True)
            words, chars_num, minutes = summary_stats()
        
            st.write(f"{words} words ({chars_num} characters) in {minutes} minutes")
        
        st.code(
            st.session_state.summary,
            language=None,
            line_numbers=False,
            wrap_lines=True
        )
        
        col1, col2 = st.columns(2)

        with col1:
            download_options = ["TXT", "MD"]
            download_type = st.segmented_control(
                "Download as",
                options=download_options,
                default="TXT"
            )
            
            if download_type == "TXT":
                file_name = "summary.txt"
                mime="text/plain"

            else:
                file_name = "summary.md"
                mime="text/markdown"

        with col2:
            st.markdown("\n", unsafe_allow_html=True)
            st.download_button(
                ":material/download: Download",
                st.session_state.summary,
                file_name=file_name,
                mime=mime,
                use_container_width=True,
            )