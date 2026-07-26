import streamlit as st

def render_output():
    if not st.session_state.summary:
        return
    
    with st.container(border=True):
        st.subheader("✨ Summary")

        st.text_area(
            "summary",
            value=st.session_state.summary,
            height=220,
            disabled=True,
            label_visibility="collapsed",
        )
        
        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                ":material/download: Download",
                st.session_state.summary,
                file_name="summary.txt",
                mime="text/plain",
                use_container_width=True,
            )

        with col2:

            st.button(
                ":material/content_copy: Copy",
                use_container_width=True,
                disabled=True,
            )