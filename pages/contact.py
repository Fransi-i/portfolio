import streamlit as st
import my_lib.send_email as se

st.header("Contact")
with st.form(key="email_form"):
    contact_email = st.text_input("Your email address")
    message = st.text_area("Your message")

    button = st.form_submit_button("Send")
    if button:
        se.send_mail(contact_email, message)
        st.write("Email on its way")
        