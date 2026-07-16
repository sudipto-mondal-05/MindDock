"""Reusable file uploader component for Streamlit pages."""

import streamlit as st


def render_uploader(label: str = "Upload a document"):
    """Render a file uploader widget restricted to supported document types.

    Args:
        label: Label displayed above the uploader.

    Returns:
        The uploaded file(s) from Streamlit, or None.

    TODO: Add client-side size validation feedback.
    """
    return st.file_uploader(label, type=["pdf", "docx", "txt"], accept_multiple_files=True)
