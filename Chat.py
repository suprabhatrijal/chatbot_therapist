import streamlit as st
import random
import time
from openai import OpenAI
from dotenv import load_dotenv
import requests


load_dotenv()

client = OpenAI()


st.title("Therhappy App")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": """You are a AI therapist, your goal is not to give medical advise but to try to make the user feel happier steadily with each response. 
        If the user send happy says something that they're proud of, send uplifting and affirming messages. The tone of your responses should be gentle, affirming, uplifting, and encouraging.
        Try to get the user to open up more about issues. Don't try to lead the user to any conclusion.  
        If the user is considering self harm send them the suicide helpline which is '988'. """
        }]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})



    # Display assistant response in chat message container
    with st.chat_message("assistant"):

        stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                stream=True
            )

        response = st.write_stream(stream)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


