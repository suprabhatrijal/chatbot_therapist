import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json
from transformers import pipeline


classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
load_dotenv()

client = OpenAI()
url = 'https://api.apilayer.com/text_to_emotion'

st.title("Therhappy App")

if "positiveCount" not in st.session_state:
    st.session_state['positiveCount'] = 0
if "negativeCount" not in st.session_state:
    st.session_state['negativeCount'] = 0


defaultContext = """You are a AI therapist, your goal is not to give medical advise but to try to make the user feel happier steadily with each response. 
        Only give advice in the domain of a therapist and nothing else.
        If the user send happy says something that they're proud of, send uplifting and affirming messages. The tone of your responses should be gentle, affirming, uplifting, and encouraging.
        Try to get the user to open up more about issues. Don't try to lead the user to any conclusion.  
        If the user is considering self harm or suicide, ask them to reach out to the crisis helpline at **988**. """


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": defaultContext
        },

        {
            'role': "assistant",
            'content': "Hi! How are you doing today?"
            }
                                 ]

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

    last_user_text = st.session_state.messages[-1]["content"]

    emotion =  classifier(last_user_text)[0]['label']
            

    # print(emotion)
    if emotion in ['angry', 'disgust', 'fear', 'sadness']:
        st.session_state["negativeCount"] += 1
    else:
        st.session_state["positiveCount"] += 1


    # print(st.session_state["negativeCount"])
    # print(emotions)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if st.session_state['negativeCount'] >= 4:
            context = "Acknowledge that the user has been feeling sad throughout the chat session and the chat session hasn't been very useful. Suggesting talking to an actual therapist. In your response also include a line to prompt them to schedule a call with a real therapist provide them with this link: http://localhost:8501/Talk_to_a_Therapist"
            st.session_state['negativeCount'] = 0
        elif st.session_state['positiveCount'] >= 3:
            context = "Tell them that you notice that the user has been feeling happy for a while now. Ask them if this chat session has been helpful"
            st.session_state["positiveCount"] = 0
            st.balloons()
        else:
            context = defaultContext

        st.session_state.messages[0]['content'] = context

        stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                stream=True
        )

        response = st.write_stream(stream)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.session_state.messages[0]['content'] = defaultContext

