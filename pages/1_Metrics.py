import streamlit as st
from analysis.data_loader import load_data
from analysis.insights import detect_frustration, detect_failures, recommendation_quality

st.title("📊 Metrics Overview")

conversations, messages = load_data()

messages = detect_frustration(messages)
messages = detect_failures(messages)

frustration_rate = messages["frustrated"].mean()
failure_rate = messages["failure"].mean()
_, _, conversion_rate = recommendation_quality(messages)

col1, col2, col3 = st.columns(3)

col1.metric("😤 Frustration Rate", f"{frustration_rate:.2f}")
col2.metric("⚠️ Failure Rate", f"{failure_rate:.2f}")
col3.metric("🛍️ Conversion Rate", f"{conversion_rate:.2f}")

st.markdown("---")

st.info("These metrics summarize overall assistant performance.")