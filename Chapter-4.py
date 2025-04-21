import streamlit as st
import pandas as pd


st.title("Protein Sales Dashboard")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Sales Summary")

    st.write(df.describe()) 


if file:
    brands = df['Brand'].unique()
    select_brand = st.selectbox("Filter Brand", brands)
    filtered_data = df[df["Brand"] == select_brand]
    st.dataframe(filtered_data)