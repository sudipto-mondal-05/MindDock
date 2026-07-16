"""MindDock AI - Search page. Perform semantic search across documents."""

import streamlit as st

from frontend.shared import load_css

st.set_page_config(page_title="Search - MindDock AI", page_icon="🔍", layout="wide")

load_css()

st.title("🔍 Semantic Search")

query = st.text_input("Search your documents", placeholder="What are you looking for?")
st.multiselect("Restrict to documents:", options=[], placeholder="No documents uploaded yet")
st.slider("Number of results", min_value=1, max_value=20, value=5)

if st.button("Search", type="primary") and query:
    st.info("Semantic search is not yet implemented.")

st.divider()
st.markdown("#### Results")
st.write("No results yet.")

# TODO: wire up to search_service via the API
