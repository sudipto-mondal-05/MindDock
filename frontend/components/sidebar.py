"""Reusable sidebar navigation component for Streamlit pages."""

import streamlit as st


def render_sidebar() -> None:
    """Render the standard MindDock AI sidebar navigation.

    TODO: Highlight the currently active page.
    """
    with st.sidebar:
        st.markdown("### 🧠 MindDock AI")
        st.caption("Your local AI document assistant")
        st.divider()
        st.page_link("Home.py", label="Home", icon="🏠")
        st.page_link("pages/1_Dashboard.py", label="Dashboard", icon="📊")
        st.page_link("pages/2_Upload.py", label="Upload", icon="📤")
        st.page_link("pages/3_Chat.py", label="Chat", icon="💬")
        st.page_link("pages/4_Summary.py", label="Summary", icon="📝")
        st.page_link("pages/5_Quiz.py", label="Quiz", icon="❓")
        st.page_link("pages/6_Search.py", label="Search", icon="🔍")
        st.page_link("pages/7_Settings.py", label="Settings", icon="⚙️")
