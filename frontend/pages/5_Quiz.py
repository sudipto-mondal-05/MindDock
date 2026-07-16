"""MindDock AI - Quiz page. Generate quizzes from uploaded documents."""

import streamlit as st

from frontend.shared import load_css

st.set_page_config(page_title="Quiz - MindDock AI", page_icon="❓", layout="wide")

load_css()

st.title("❓ Quiz Generator")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Select a document", options=[], placeholder="No documents uploaded yet")
    st.number_input("Number of questions", min_value=1, max_value=20, value=5)
with col2:
    st.select_slider("Difficulty", options=["easy", "medium", "hard"], value="medium")

if st.button("Generate Quiz", type="primary"):
    st.info("Quiz generation is not yet implemented.")

st.divider()
st.markdown("#### Quiz Preview")
st.write("No quiz generated yet.")

# TODO: wire up to quiz_service via the API and render interactive questions
