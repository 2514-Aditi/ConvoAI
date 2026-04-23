import streamlit as st
from analysis.data_loader import load_data
from analysis.insights import extract_key_patterns, recommendation_quality

st.title("💡 Insights")

conversations, messages = load_data()
_, _, conversion_rate = recommendation_quality(messages)

patterns = extract_key_patterns(messages, conversion_rate)

for i, p in enumerate(patterns):
    st.markdown(f"""
    <div style='
        background-color:#1f2937;
        padding:18px;
        border-radius:12px;
        margin-bottom:12px;
        border-left:5px solid #6366F1;
        color:#E5E7EB;
        font-size:15px;
        line-height:1.6;
    '>
        <b style='color:#A5B4FC; font-size:16px;'>Insight {i+1}</b><br><br>
        {p}
    </div>
    """, unsafe_allow_html=True)