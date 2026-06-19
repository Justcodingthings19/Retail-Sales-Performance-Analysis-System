import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Retail Dashboard",
    layout="wide"
)

st.title(
    "Retail Sales Performance Dashboard"
)

data = pd.read_csv(
    "dataset/retail_sales.csv"
)

st.subheader("Dataset")

st.dataframe(data)

st.subheader("Summary")

st.write(data.describe())

st.subheader("Sales Chart")

st.bar_chart(data["Sales"])
