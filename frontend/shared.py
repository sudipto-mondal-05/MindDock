"""Shared frontend utilities for MindDock AI Streamlit pages."""

from pathlib import Path

import streamlit as st


def load_css() -> None:
    """Load the shared Streamlit stylesheet for the app."""
    style_path = Path(__file__).resolve().parent / "assets" / "styles.css"
    if not style_path.exists():
        return

    css = style_path.read_text(encoding="utf-8")

    # Streamlit's generated class names can change between versions.
    # Use stable data-testid selectors where possible and add an
    # explicit override to ensure the background applies.
    override_css = (
        "\n/* Overrides to target Streamlit stable selectors */\n"
        "div[data-testid=\"stAppViewContainer\"] { background-color: var(--minddock-bg) !important; }\n"
    )

    # Replace legacy `.stApp` selector with a stable selector for newer Streamlit
    css = css.replace(".stApp", "div[data-testid=\"stAppViewContainer\"]")

    st.markdown(f"<style>{css}\n{override_css}</style>", unsafe_allow_html=True)
