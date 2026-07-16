"""Reusable top navigation bar component for Streamlit pages."""

import streamlit as st


def render_navbar(title: str = "MindDock AI") -> None:
    """Render a simple top navigation bar.

    Args:
        title: Title text to display in the navbar.

    TODO: Add breadcrumbs / active-page highlighting.
    """
    st.markdown(f"### 🧠 {title}")
    st.divider()
