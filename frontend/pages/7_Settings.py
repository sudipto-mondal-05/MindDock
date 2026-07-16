"""MindDock AI - Settings page. Configure application and model settings."""

import streamlit as st

from frontend.shared import load_css

st.set_page_config(page_title="Settings - MindDock AI", page_icon="⚙️", layout="wide")

load_css()

st.title("⚙️ Settings")

st.markdown("#### Model Configuration")
st.selectbox("Ollama Model", options=["llama3.2"], index=0)
st.text_input("Ollama Base URL", value="http://localhost:11434")

st.markdown("#### Storage")
st.text_input("Upload Directory", value="storage/uploads", disabled=True)
st.text_input("Vector DB Directory", value="vector_db", disabled=True)

st.markdown("#### Danger Zone")
st.button("🗑️ Clear All Documents", type="secondary")
st.button("🧹 Reset Vector Database", type="secondary")

st.divider()
st.caption("MindDock AI v0.1.0 — local, private, and yours.")

# TODO: persist settings changes and wire up danger-zone actions to the API
