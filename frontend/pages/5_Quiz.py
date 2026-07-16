"""MindDock AI - Quiz page. Generate quizzes from uploaded documents."""

from pathlib import Path

import requests
import streamlit as st

from frontend.shared import load_css

API_URL = "http://localhost:8000"
REQUEST_TIMEOUT = 60

st.set_page_config(page_title="Quiz - MindDock AI", page_icon="❓", layout="wide")

load_css()

st.title("❓ Quiz Generator")

if "quiz_documents" not in st.session_state:
    st.session_state.quiz_documents = []


def get_upload_dir() -> Path:
    return (Path(__file__).resolve().parents[2] / "storage" / "uploads").resolve()


def load_documents() -> None:
    upload_dir = get_upload_dir()
    if upload_dir.exists():
        files = sorted(path.name for path in upload_dir.iterdir() if path.is_file())
        st.session_state.quiz_documents = files
    else:
        st.session_state.quiz_documents = []


load_documents()

col1, col2 = st.columns(2)
with col1:
    selected_document = st.selectbox(
        "Select a document",
        options=st.session_state.quiz_documents if st.session_state.quiz_documents else ["No documents uploaded yet"],
        placeholder="No documents uploaded yet",
    )
    num_questions = st.number_input("Number of questions", min_value=1, max_value=20, value=5)
with col2:
    difficulty = st.select_slider("Difficulty", options=["easy", "medium", "hard"], value="medium")

quiz_output = []
if st.button("Generate Quiz", type="primary"):
    if not st.session_state.quiz_documents or selected_document == "No documents uploaded yet":
        st.error("Please add a supported document to the upload folder first.")
    else:
        try:
            response = requests.post(
                f"{API_URL}/quiz/",
                json={
                    "document_id": selected_document,
                    "num_questions": int(num_questions),
                    "difficulty": difficulty,
                },
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            payload = response.json()
            quiz_output = payload.get("quiz", {}).get("questions", [])
            st.success("Quiz generated successfully.")
        except requests.RequestException as exc:
            st.error(f"Quiz generation failed: {exc}")

st.divider()
st.markdown("#### Quiz Preview")
if quiz_output:
    for idx, question in enumerate(quiz_output, start=1):
        st.markdown(f"**{idx}. {question.get('question', '')}**")
        for option in question.get("options", []):
            st.write(f"- {option}")
        if question.get("correct_answer"):
            st.caption(f"Correct answer: {question['correct_answer']}")
        if question.get("explanation"):
            st.caption(f"Explanation: {question['explanation']}")
        st.write("")
else:
    st.write("No quiz generated yet.")
