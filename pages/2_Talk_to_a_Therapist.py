import streamlit as st
import time
# import smtplib
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# import os
import base64
from requests import HTTPError

load_dotenv()


zoom_url = "https://meet.google.com/hrc-petk-oyo"
placeholder = st.empty()
with placeholder.container():
    with st.spinner('Finding an available therapist.'):
        SCOPES = [
            "https://www.googleapis.com/auth/gmail.send"
            ]
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(f"""
                           Please click this link to join the therapy session:
                           
                            {zoom_url}
                           """)
        message['to'] = 'rijal.suprabhat@gmail.com'
        message['subject'] = 'A user has requested a therapist session'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (service.users().messages().send(userId="me", body=create_message).execute())
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None

with placeholder.container():
    st.link_button('Talk to a therapist', zoom_url)
    

