
import streamlit as st
import requests

API_URL = "https://flowisetest-1.onrender.com/api/v1/prediction/318e37be-4ab4-4d78-9c3f-791f977fe11b"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    st.title("Chatbot Web App")
    
    st.write("Welcome to the chatbot! Type a question below:")
    
    user_input = st.text_input("You:", value="")
    
    if st.button("Ask"):
        if user_input.strip() != "":
            response = query({"question": user_input})
            
            bot_response = response.get("text")
            
            st.text_area("Bot:", bot_response)
    
if __name__ == "__main__":
    main()