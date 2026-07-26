import streamlit as st
from src.models import SummaryType
from src.utils import user_input_stats, clear_session

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
        
        if text:
            words, char_num = user_input_stats()
        
            st.markdown(f"###### Above text contains {words} words ({char_num} characters)")
        
        if(st.session_state.summary and text != st.session_state.last_summarized_text):
            st.session_state.summary = ""
            
        uploaded_pdf = st.session_state.get("uploaded_pdf")
            
        show_clear = bool(text.strip()) or uploaded_pdf is not None
        
        if show_clear:
            col1, col2, col3, col4 = st.columns([2,1,1,0.8])
        else:
            col1, col2, col3 = st.columns([2,1,1])
            col4 = None
        
        with col1:
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
                        type="secondary",
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
            
        if show_clear:
            with col4:
                if st.button(":material/clear: Clear", use_container_width=True):
                    clear_session()
                
    return text, uploaded_pdf, summary_type, summarize