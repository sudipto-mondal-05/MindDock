"""Reusable chat window component for Streamlit pages."""

import streamlit as st


def render_chat_window(history: list[dict]) -> None:
    """Render a chat message history.

    Args:
        history: List of message dicts with 'role' and 'content' keys.

    TODO: Support streaming message rendering.
    """
    for message in history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
