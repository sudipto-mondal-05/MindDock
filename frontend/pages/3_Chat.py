"""MindDock AI - Chat page. Chat interface for interacting with documents."""

import requests
import streamlit as st

from frontend.shared import load_css

API_URL = "http://localhost:8000"
REQUEST_TIMEOUT = 60

st.set_page_config(page_title="Chat - MindDock AI", page_icon="💬", layout="wide")

load_css()

st.title("💬 Chat with your Documents")

with st.sidebar:
    st.markdown("#### Select Documents")
    st.multiselect("Scope this chat to:", options=[], placeholder="No documents uploaded yet")
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.conversation_id = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask something about your documents...")
if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = requests.post(
            f"{API_URL}/chat/",
            json={
                "conversation_id": st.session_state.conversation_id,
                "document_ids": [],
                "message": prompt,
            },
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        payload = response.json()
        assistant_text = payload["message"]["content"]
        st.session_state.conversation_id = payload["conversation_id"]
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_text})

        with st.chat_message("assistant"):
            st.write(assistant_text)
    except requests.RequestException as exc:
        error_message = str(exc)
        st.session_state.chat_history.append({"role": "assistant", "content": "Failed to reach the chat backend."})
        with st.chat_message("assistant"):
            st.error(error_message)
