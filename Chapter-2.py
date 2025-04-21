import streamlit as st

st.title("Workout Maker App")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}, welcome to the workout maker app!")


add = st.checkbox("I want to add a warm-up")
if add:
    st.success("Warm-up added!")



Workout_types = st.radio("Select a workout type", ["Cardio", "Strength", "Flexibility"])
st.write(f"You selected {Workout_types}")


workout_location =  st.selectbox("Select a workout location", ["Gym", "Home", "Outdoor"])
st.write(f"You selected {workout_location}")

experiance_level = st.select_slider("Select your experience level", ["Beginner", "Intermediate", "Advanced"])
st.write(f"You selected {experiance_level}")


info = st.number_input("Enter your age", min_value=0, max_value=100, value=25, step=1)
info1 = st.number_input("Enter your weight", min_value=0, max_value=500, value=70, step=1)


if st.button("Make a Workout"):
    st.success("Workout Created!")

