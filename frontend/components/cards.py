"""Reusable metric/info card components for Streamlit pages."""

import streamlit as st


def render_metric_card(label: str, value: str, delta: str | None = None) -> None:
    """Render a single metric card.

    Args:
        label: The metric's label.
        value: The metric's current value.
        delta: Optional delta value to display.
    """
    st.metric(label=label, value=value, delta=delta)


def render_info_card(title: str, description: str) -> None:
    """Render a simple bordered info card.

    Args:
        title: Card title text.
        description: Card body text.

    TODO: Style with custom CSS from assets/styles.css.
    """
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.caption(description)
