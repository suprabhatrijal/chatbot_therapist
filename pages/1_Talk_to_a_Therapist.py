import streamlit as st
import time


placeholder = st.empty()
with placeholder.container():
    with st.spinner('Finding an available therapist.'):
        time.sleep(5)

with placeholder.container():
    st.link_button('Talk to a therapist', 'https://howard.zoom.us/j/87155741484?pwd%3DMDRYSnJEMnNndnIxS29JTW5FS2hIZz09%23success&sa=D&source=calendar&usd=2&usg=AOvVaw29TfU4lluMtqI4N0_LWKo-#success')
    

