"""MindDock AI - Upload page. Allows users to upload PDF, DOCX, and TXT files."""

import requests
import streamlit as st

from frontend.shared import load_css

API_URL = "http://localhost:8000"
REQUEST_TIMEOUT = 60

st.set_page_config(page_title="Upload - MindDock AI", page_icon="📤", layout="wide")

load_css()

st.title("📤 Upload Documents")
st.caption("Add PDF, DOCX, or TXT files to your MindDock AI knowledge base")

if "uploaded_documents" not in st.session_state:
    st.session_state.uploaded_documents = []

uploaded_files = st.file_uploader(
    "Drag and drop files here",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
)

if uploaded_files:
        uploaded_count = 0
        for uploaded_file in uploaded_files:
            try:
                response = requests.post(
                    f"{API_URL}/documents/",
                    files={"file": (uploaded_file.name, uploaded_file.read(), uploaded_file.type)},
                    timeout=REQUEST_TIMEOUT,
                )
                response.raise_for_status()
                payload = response.json()
                st.session_state.uploaded_documents.append(payload["document"])
                uploaded_count += 1
            except requests.RequestException as exc:
                st.error(f"Failed to upload {uploaded_file.name}: {exc}")

        if uploaded_count:
            st.success(f"Uploaded {uploaded_count} file(s) successfully.")
if st.button("Refresh uploaded documents"):
    try:
        response = requests.get(f"{API_URL}/documents/", timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        payload = response.json()
        st.session_state.uploaded_documents = payload.get("documents", [])
    except requests.RequestException as exc:
        st.error(f"Unable to refresh document list: {exc}")

if st.session_state.uploaded_documents:
    st.divider()
    st.markdown("#### Uploaded Documents")
    st.dataframe(
        [
            {
                "Filename": doc.get("filename", ""),
                "Type": doc.get("doc_type", ""),
                "Status": doc.get("status", ""),
                "Size": f"{doc.get('size_bytes', 0)} bytes",
                "Uploaded At": doc.get("created_at", ""),
            }
            for doc in st.session_state.uploaded_documents
        ],
        use_container_width=True,
    )
else:
    st.divider()
    st.markdown("#### Uploaded Documents")
    st.info("No documents uploaded yet. Use the uploader above and press Refresh.")
