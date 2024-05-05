import streamlit_antd_components as sac
import streamlit as st

st.title("Therhappy App")

st.subheader("How to best use our app:")

if "demo_messages" not in st.session_state:
    st.session_state.demo_messages = [{
        "role": "system",
        "content": ""
        },

        {
            'role': "assistant",
            'content': "Hi! How are you doing today?"
        },
        {
            'role': "user",
            'content': "I lost my job. I feel worthless."
        },
        {
            'role': "assistant",
            'content': "I'm sorry to hear that you're going through a tough time. Losing a job can be really challenging, but it doesn't define your worth as a person. Remember that your value goes beyond your work status. Take some time to process your feelings and reach out to loved ones for support. It's okay to not be okay right now. How are you feeling about everything?"
        },
]
if "demo_messages2" not in st.session_state:
    st.session_state.demo_messages2 = [{
        "role": "system",
        "content": ""
        },

        {
            'role': "assistant",
            'content': "Hi! How are you doing today?"
        },
        {
            'role': "user",
            'content': "I lost my job. I feel worthless."
        },
        {
            'role': "assistant",
            'content': "I'm sorry to hear that you're going through a tough time. Losing a job can be really challenging, but it doesn't define your worth as a person. Remember that your value goes beyond your work status. Take some time to process your feelings and reach out to loved ones for support. It's okay to not be okay right now. How are you feeling about everything?"
        },
        {
            'role': "user",
            'content': "I feel like I have nobody. I am so sad."
        },
        {
            'role': "assistant",
            'content': "I'm so sorry to hear that you're feeling this way. It sounds like you're going through a really tough time right now. Remember that your feelings are valid, and it's okay to not be okay. It's important to take care of yourself during moments of distress. If you're feeling overwhelmed, it may be helpful to reach out to a mental health professional for support. Remember, you are not alone in this, and there are people who care about you."
        },
        {
            'role': "user",
            'content': "I hate this. I feel terrible"
        },    
        {
            'role': "assistant",
            'content': "I understand that you've been feeling sad throughout our chat session, and I'm sorry that our conversation hasn't been very helpful. It's important to prioritize your well-being, and talking to a mental health professional might offer you the support you need. Consider scheduling a call with a real therapist for a more personalized and effective guidance. You can use this link to connect with a therapist: http://localhost:8501/Talk_to_a_Therapist. Take care."
        },    

    ]

if "demo_messages3" not in st.session_state:
    st.session_state.demo_messages3 = [{
        "role": "system",
        "content": ""
        },

        {
            'role': "assistant",
            'content': "Hi! How are you doing today?"
        },
        {
            'role': "user",
            'content': "I lost my job. I feel worthless."
        },
        {
            'role': "assistant",
            'content': "I'm sorry to hear that you're going through a tough time. Losing a job can be really challenging, but it doesn't define your worth as a person. Remember that your value goes beyond your work status. Take some time to process your feelings and reach out to loved ones for support. It's okay to not be okay right now. How are you feeling about everything?"
        },
        {
            'role': "user",
            'content': "I feel like I have nobody. I am so sad."
        },
        {
            'role': "assistant",
            'content': "I'm so sorry to hear that you're feeling this way. It sounds like you're going through a really tough time right now. Remember that your feelings are valid, and it's okay to not be okay. It's important to take care of yourself during moments of distress. If you're feeling overwhelmed, it may be helpful to reach out to a mental health professional for support. Remember, you are not alone in this, and there are people who care about you."
        },
        {
            'role': "user",
            'content': "I hate this. I feel terrible"
        },    
        {
            'role': "assistant",
            'content': "I understand that you've been feeling sad throughout our chat session, and I'm sorry that our conversation hasn't been very helpful. It's important to prioritize your well-being, and talking to a mental health professional might offer you the support you need. Consider scheduling a call with a real therapist for a more personalized and effective guidance. You can use this link to connect with a therapist: http://localhost:8501/Talk_to_a_Therapist. Take care."
        },    
        {
            'role': "user",
            'content': "Thank you! I feel much better now. I so light!"
        },
    ]

step = sac.steps(

    items=[

        sac.StepsItem(title='step 1'),

        sac.StepsItem(title='step 2'),

        sac.StepsItem(title='step 3'),
    ], 

)


if step == "step 1":
    st.subheader("Open up about how you are feeling to the chatbot.")
    st.caption("Our AI tries to understand your emotions and helps you navigate them.")
    st.divider()
    for message in st.session_state.demo_messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    st.divider()
elif step== "step 2":
    st.subheader("Talk to a therapist")
    st.caption("If you we notice that our chatbot isn't working, we schedule a meeting with a licensed therapist and prompt you to join it.")
    st.divider()
    for message in st.session_state.demo_messages2:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    st.divider()
elif step== "step 3":
    st.balloons()
    st.subheader("Feel better!")
    st.caption("When we see you feeling better we'll celebrate with some awesome animations!")
    st.divider()
    for message in st.session_state.demo_messages3:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    st.divider()

