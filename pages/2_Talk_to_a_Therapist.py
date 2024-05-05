import streamlit as st
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import base64
from requests import HTTPError

load_dotenv()


zoom_url = "https://meet.google.com/hrc-petk-oyo"
google_cred = {"installed":st.secrets["installed"]}
sender = "goodguysman@gmail.com"
reciever = "rijal.suprabhat@gmail.com"

placeholder = st.empty()
with placeholder.container():
    with st.spinner('Finding an available therapist.'):
        message = MIMEText(f"""
                           Please click this link to join the therapy session:
                           
                            {zoom_url}
                           """)
        message['to'] = 'rijal.suprabhat@gmail.com'
        message['subject'] = 'A user has requested a therapist session'
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, st.secrets["APP_PASSWORD"])
            server.sendmail(sender, reciever, message.as_string())
            server.quit()
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None

with placeholder.container():
    st.link_button('Talk to a therapist', zoom_url)
    

