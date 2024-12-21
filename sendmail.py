import streamlit as st 
from email.message import EmailMessage
import ssl
import smtplib


sender='aishafazyakinola9@gmail.com'
password='ughzxjmmvfbznndi'

receiver=st.text_input("Enter Email To Send To")
subject=st.text_input("Enter Email Subject Here")

body=st.text_area("Enter Email Content Here",height=200)

if st.button("Send Mail"):

    email=EmailMessage()
    email['From']=sender
    email['To']=receiver
    email['subject']=subject
    email.set_content(body)
    securecontents=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',456,context=securecontents) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,email.as_string())
        st.success("Email Sent")



