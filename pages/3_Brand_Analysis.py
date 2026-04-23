import streamlit as st
from analysis.data_loader import load_data
from analysis.insights import brand_analysis

st.title("🏷️ Brand Analysis")

conversations, messages = load_data()
brand_stats = brand_analysis(conversations, messages)

# ---- FILTER ----
st.subheader("Filter by Brand")

brands = brand_stats["widgetId"].astype(str).tolist()
selected_brand = st.selectbox("Select Brand", ["All"] + brands)

if selected_brand != "All":
    filtered = brand_stats[brand_stats["widgetId"].astype(str) == selected_brand]
else:
    filtered = brand_stats

# ---- CHART ----
st.subheader("📈 Message Distribution")

st.bar_chart(filtered.set_index("widgetId"))

# ---- TABLE ----
st.subheader("📋 Data Table")

st.dataframe(filtered)