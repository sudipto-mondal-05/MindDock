"""MindDock AI - Streamlit Home page.

Entry point for the Streamlit multi-page application.
"""

import sys
from pathlib import Path

# Ensure the project root is on sys.path so `from frontend.shared` works
# when Streamlit runs this file as a script.
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st

from frontend.shared import load_css

st.set_page_config(
    page_title="MindDock AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

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

st.title("🧠 MindDock AI")
st.subheader("Your local, private AI-powered document assistant")

st.markdown(
    """
Welcome to **MindDock AI** — upload your documents and chat with them,
generate summaries, build quizzes, and search across your knowledge base,
all running locally on your machine.
"""
)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Documents", "0")
with col2:
    st.metric("Conversations", "0")
with col3:
    st.metric("Summaries", "0")
with col4:
    st.metric("Quizzes", "0")

st.divider()

st.markdown("#### Get started")
gcol1, gcol2, gcol3 = st.columns(3)
with gcol1:
    st.markdown("**1. Upload**  \nAdd PDF, DOCX, or TXT documents.")
with gcol2:
    st.markdown("**2. Process**  \nMindDock indexes your content locally.")
with gcol3:
    st.markdown("**3. Interact**  \nChat, summarize, quiz, and search.")

# TODO: replace static metrics with live calls to the dashboard API
