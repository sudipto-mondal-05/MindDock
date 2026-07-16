"""MindDock AI - Dashboard page. Displays analytics and usage metrics."""

import streamlit as st

from frontend.shared import load_css

st.set_page_config(page_title="Dashboard - MindDock AI", page_icon="📊", layout="wide")

load_css()

st.title("📊 Dashboard")
st.caption("Overview of your MindDock AI workspace")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Documents", "0")
col2.metric("Total Conversations", "0")
col3.metric("Summaries Generated", "0")
col4.metric("Quizzes Generated", "0")

st.divider()

st.markdown("#### Recent Activity")
st.dataframe({"Date": [], "Action": [], "Document": []}, use_container_width=True)

st.markdown("#### Document Types Breakdown")
st.bar_chart({"PDF": [0], "DOCX": [0], "TXT": [0]})

# TODO: replace placeholders with live calls to dashboard_service via the API
