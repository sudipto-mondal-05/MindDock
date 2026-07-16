"""MindDock AI - Summary page. Generate summaries of uploaded documents."""

from pathlib import Path

import requests
import streamlit as st

from frontend.shared import load_css

API_URL = "http://localhost:8000"
REQUEST_TIMEOUT = 60

st.set_page_config(page_title="Summary - MindDock AI", page_icon="📝", layout="wide")

load_css()

st.title("📝 Document Summary")

summary_length = st.selectbox("Summary length", options=["short", "medium", "long"], index=1)

if "documents" not in st.session_state:
    st.session_state.documents = []


def get_upload_dir() -> Path:
    return (Path(__file__).resolve().parents[2] / "storage" / "uploads").resolve()


def load_documents() -> None:
    try:
        response = requests.get(f"{API_URL}/documents/", timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        payload = response.json()
        documents = payload.get("documents", [])
        if documents:
            st.session_state.documents = documents
            return
    except requests.RequestException as exc:
        st.caption(f"Falling back to local upload directory: {exc}")

    upload_dir = get_upload_dir()
    if upload_dir.exists():
        files = sorted(path.name for path in upload_dir.iterdir() if path.is_file())
        st.session_state.documents = [{"filename": filename, "id": filename} for filename in files]
    else:
        st.session_state.documents = []
        st.warning("Upload directory not found.")


if not st.session_state.documents:
    load_documents()

if st.button("Refresh documents"):
    load_documents()

options = [doc.get("filename", doc.get("id", str(doc))) for doc in st.session_state.documents]
selected_document = st.selectbox(
    "Select a document",
    options=options if options else ["No documents uploaded yet"],
    format_func=lambda x: x,
    key="selected_document",
    disabled=not bool(options),
)

summary_output = ""
if st.button("Generate Summary", type="primary"):
    if not options or not selected_document or selected_document == "No documents uploaded yet":
        st.error("Please refresh and select a document first.")
    else:
        try:
            body = {"document_id": selected_document, "length": summary_length}
            response = requests.post(
                f"{API_URL}/summary/",
                json=body,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            payload = response.json()
            summary_output = payload["summary"]["content"]
            st.success("Summary generated successfully.")
        except requests.RequestException as exc:
            st.error(f"Summary generation failed: {exc}")

st.divider()
st.markdown("#### Generated Summary")
st.text_area("Summary output", value=summary_output, height=250, disabled=True)

# TODO: wire up to summary_service via the API
