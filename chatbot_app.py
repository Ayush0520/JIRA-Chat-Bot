import streamlit as st
import requests

# Title and description
st.title("JIRA AI Agent")
st.write("Interact with your chatbot through this interface!")

# User input
user_query = st.text_input("Enter your query:", placeholder="Type something...")

# Button to submit query
if st.button("Submit"):
    if user_query.strip():
        # API endpoint
        api_url = "https://c812-20-193-157-81.ngrok-free.app/api/query"
        payload = {"query": user_query}

        try:
            # Send POST request to the backend
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Summary: {result.get('summary')}")
                st.write(f"Message: {result.get('message')}")
            else:
                st.error(f"Error: {response.status_code} - {response.json().get('error')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query!")

# Display usage instructions
st.info("This chatbot processes user queries and provides a summary or response based on JIRA Historical Data.")
