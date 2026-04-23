import streamlit as st
from analysis.data_loader import load_data
from analysis.insights import brand_analysis

st.title("🏷️ Brand Analysis")

conversations, messages = load_data()
brand_stats = brand_analysis(conversations, messages)

st.subheader("📈 Message Distribution")

st.bar_chart(brand_stats.set_index("widgetId"))

st.subheader("📋 Data Table")

st.dataframe(brand_stats)