import streamlit as st
import requests

FLASK_API_URL = "http://127.0.0.1:5000"


# Function to display the chat
def ui():
    # Title
    st.title("I am your onboarding buddy")

    with st.form("post_data_form"):
        input_data = st.text_input('Question', key='question')
        submit_button = st.form_submit_button("Ask!")
        
        if submit_button:
            response = requests.post(f"{FLASK_API_URL}/ask", json={"question": input_data})
            if response.status_code == 201:
                response_data = response.json()
                st.success(response_data)
            else:
                st.error("Failed to send data to Flask API")

ui()