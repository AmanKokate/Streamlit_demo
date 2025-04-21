import streamlit as st

st.title("Hello World!")
st.subheader("This is a Subheader")
st.write("This is a simple Streamlit app to demonstrate the use of Streamlit.")
st.text("This is a text element.")

Demo = st.selectbox("Select a demo", ["Demo 1", "Demo 2", "Demo 3"])
st.write(f"you selected {Demo}")

st.success("The Option has been selected")



st.title("select a programing Language")

lang = st.selectbox("Select a programming language", ["Python", "java", "c++", "C#", "javascript"])
st.write(f"you selected {lang}")


st.success("The Programing language has been selected")



