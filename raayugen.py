#gfh
# import streamlit as st
# import google
# from google import genai

# # Function to query Gemini model
# def query(user_query):
#     # Load API key securely (better to use st.secrets)
#     api_key ="AIzaSyCrTm6b4G-QT23LSZuejjbJny24dOyfVqQ"

#     # Initialize client
#     my_ai = genai.Client(api_key=api_key)

#     # Generate response
#     response = my_ai.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=user_query
#     )

#     # Convert into text format
#     return response.text

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["msg"])

# # App title
# st.title("🧠 RAYYU-GEN 💻")

# # User input
# user_input = st.chat_input("Ask me anything...")

# if user_input:
#     # Add user message to history
#     st.session_state.messages.append({"role": "user", "msg": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Get AI response
#     ai_response = query(user_input)

#     # Add AI response to history
#     st.session_state.messages.append({"role": "assistant", "msg": ai_response})
#     with st.chat_message("assistant"):
#         st.markdown(ai_response)


# import streamlit as st
# import google
# from google import genai

# # Function to query Gemini model
# def query(user_query):
#     # Load API key securely (better to use st.secrets)
#     api_key ="AIzaSyDEc_QOSuvaiocFivYGphrPDewgsfP_-yA"

#     # Initialize client
#     my_ai = genai.Client(api_key=api_key)

#     # Generate response
#     response = my_ai.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=user_query
#     )

#     # Convert into text format
#     return response.text

# # Initialize session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["msg"])

# # App title
# st.title("🧠 RAYYU-GEN 💻")

# # User input
# user_input = st.chat_input("Ask me anything...")

# if user_input:
#     # Add user message to history
#     st.session_state.messages.append({"role": "user", "msg": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Get AI response
#     ai_response = query(user_input)

    # Add AI response to history
    # st.session_state.messages.append({"role": "assistant", "msg": ai_response})
    # with st.chat_message("assistant"):

    #     st.markdown(ai_response)
# import streamlit as st
# import google.generativeai as genai
# from cryptography.fernet import Fernet

# -------------------------------
# 🔐 Encryption Setup
# -------------------------------
# Generate a Fernet key once (outside the app):
# from cryptography.fernet import Fernet
# print(Fernet.generate_key())
# Save that key in .streamlit/secrets.toml as ENCRYPTION_KEY

# Encrypt your Gemini API key once locally:
# fernet = Fernet("your-generated-fernet-key")
# encrypted_key = fernet.encrypt(b"YOUR_GEMINI_API_KEY")
# print(encrypted_key.decode())
# Save that encrypted string in secrets.toml as GEMINI_API_KEY_ENCRYPTED
import os
import streamlit as st
import google
from google import genrativeai as genai

# Function to query Gemini model
def query(user_query):
    # Load API key securely (better to use st.secrets)
    api_key ="AIzaSyA25q4gkO3T5tliPA4BS8uxVycnke3p6OU"

    # Initialize client
    my_ai = genai.Client(api_key=api_key)

    # Generate response
    response = my_ai.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_query
    )

    # Convert into text format
    return responce.txt

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["msg"])

# App title
st.title("🧠RAYYU-GEN 💻")

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "msg": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    ai_response = query(user_input)

    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "msg": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)



