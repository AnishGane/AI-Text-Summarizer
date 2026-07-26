import streamlit as st
from src.models import SummaryType

def render_input():
    with st.container(border=True):
        
        text = st.text_area(
            "Enter the text here",
            value = st.session_state.input_text if st.session_state.input_text else "",
            placeholder="Paste text here",
            height=200,
            label_visibility="collapsed",
            key="input_text"
        )
        
        if(st.session_state.summary and text != st.session_state.last_summarized_text):
            st.session_state.summary = ""
            
        col1, col2, col3 = st.columns([2,2,1])
        
        with col1:
            uploaded_pdf = st.session_state.get("uploaded_pdf")

            if uploaded_pdf is None:
                with st.popover(":material/file_upload:", use_container_width=True):
                    st.file_uploader(
                        "Upload PDF",
                        type=["pdf"],
                        key="uploaded_pdf",
                        label_visibility="collapsed",
                    )

            else:
                left, right = st.columns([5,1])

                with left:
                    st.markdown(
                            f"""
                                <div class="file-chip">
                                <span class="file-name">📄 {uploaded_pdf.name}</span>
                                </div>
                                """,
                            unsafe_allow_html=True,
                        )

                with right:
                    if st.button(
                        ":material/close:",
                        key="remove_pdf",
                        help="Remove PDF",
                    ):
                        del st.session_state["uploaded_pdf"]
                        st.rerun()
            
        with col2:
            summary_type = st.selectbox(
                "Summary Type",
                options=list(SummaryType),
                index=list(SummaryType).index(
                    st.session_state.summary_type
                ),
                format_func=lambda x: x.replace("_", " ").title(),
                label_visibility="collapsed",
            )
        
        with col3:
            summarize = st.button(
                ":material/auto_awesome: Summarize",
                use_container_width=True,
                disabled=not text.strip() and uploaded_pdf is None,
            )
            
    return text, uploaded_pdf, summary_type, summarize