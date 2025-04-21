import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter amount in INR:", min_value=1)

currency = st.selectbox("Select currency to convert to:", ["USD", "EUR", "GBP", "AUD", "CAD"])

if st.button("Convert"):
    # API endpoint for currency conversion
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    
    # Make a request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][currency]
        converted_amount = amount * rate
        st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
    else:
        st.error("Error fetching data from the API.")