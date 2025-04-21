import streamlit as st


st.title("Workout Plan Feedback")

col1, col2 = st.columns(2)

with col1:
    st.header("Workout Plan")
    st.write("1. Warm-up: 10 minutes of light cardio")
    st.write("2. Strength Training: 30 minutes of weight lifting")
    st.write("3. Cool Down: 10 minutes of stretching")
    st.image("https://img.etimg.com/thumb/msid-96657736,width-650,height-488,imgsize-26966,,resizemode-75/workout.jpg", width=300)
    vote1 = st.button("Rate the workout plan")

with col2:
    st.header("Nutrition Plan")
    st.write("1. Breakfast: Oatmeal with fruits")
    st.write("2. Lunch: Grilled chicken with vegetables")
    st.write("3. Dinner: Salmon with quinoa")
    st.image("https://www.saludprimal.com/wp-content/uploads/2020/09/nutricion-03.jpg",width=400)
    vote2 = st.button("Rate the nutrition plan")


if vote1:
    st.success("Thank you for your feedback on the workout plan!")
    
elif vote2:
    st.success("Thank you for your feedback on the nutrition plan!")


name = st.sidebar.text_input("Enter your name")
plan = st.sidebar.selectbox("Select a plan", ["Workout Plan", "Nutrition Plan"])

st.write(f"Hello {name}, you selected the {plan}.") 


with st.expander("Nutrition Details"):
    st.write("1. Add more protein to your diet")
    st.write("2. Include more vegetables in your meals")
    st.write("3. Stay hydrated")


st.markdown(
        """
        ### Nutrition Tips
        - Drink plenty of water
        - Eat a balanced diet
        - Avoid processed foods
        """
    )

    

