import streamlit as st
from analysis.data_loader import load_data
from analysis.insights import (
    detect_frustration,
    detect_failures,
    recommendation_quality,
    extract_key_patterns
)

st.set_page_config(page_title="ConvoAI", layout="wide")

# ---- TITLE ----
st.title("🚀 AI Conversation Analysis Dashboard")

# ---- LOAD DATA ----
conversations, messages = load_data()

messages = detect_frustration(messages)
messages = detect_failures(messages)

# ---- METRICS ----
total_conversations = conversations.shape[0]
total_messages = messages.shape[0]

frustration_count = messages["frustrated"].sum()
failure_count = messages["failure"].sum()

_, _, conversion_rate = recommendation_quality(messages)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Conversations", total_conversations)
col2.metric("Total Messages", total_messages)
col3.metric("Frustrated Messages", int(frustration_count))
col4.metric("Conversion Rate", f"{conversion_rate:.2f}")

st.markdown("---")

# ---- ISSUE BREAKDOWN ----
st.subheader("🚨 Issue Breakdown")

issue_count = {
    "Frustration": int(frustration_count),
    "Failures": int(failure_count)
}

for k, v in issue_count.items():
    st.write(f"🔹 {k}: {v}")

st.markdown("---")

# ---- INSIGHTS ----
st.subheader("💡 Key Insights")

patterns = extract_key_patterns(messages, conversion_rate)

for i, p in enumerate(patterns):
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #1c1f26, #2a2f3a);
                padding:18px;
                border-radius:12px;
                margin-bottom:12px;
                color:white'>
        <b>Insight {i+1}</b><br><br>
        {p}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---- SUMMARY ----
if issue_count:
    top_issue = max(issue_count, key=issue_count.get)
    st.success(f"Most common issue: {top_issue}")

st.info("Use the sidebar to explore detailed metrics, insights, and brand analysis.")