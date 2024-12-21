import streamlit as st
from email.message import EmailMessage 
import ssl
import smtplib

sender='aishafazyakinola9@gmail.com'
password='ughzxjmmvfbznndi'

col1,col2=st.columns(2)
with col1:
    receiver=st.text_input('Enter Email to Send To')
with col2:
    subject=st.text_input("Enter Subject")
body=st.text_area("Enter Email message here")
upload=st.file_uploader("Upload Image/Text Files to Attach to Mail",type=['jpg','pdf','png','txt','csv','txt'])

if st.button("Send Email"):

    try:
        email=EmailMessage()
        email['From']=sender
        email['To']=receiver
        email['Subject']=subject


        if upload and receiver and subject and body:
            filedata=upload.read()
            filename=upload.name

            email.add_attachment(filedata,maintype='application', subtype='octet stream',filename=filename)



            context=ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                smtp.login(sender,password)
                smtp.sendmail(sender,receiver,email.as_string())
            st.success("Email With Attachment Sent!")
        else:
            st.warning("One or More of The Boxes Has Not Been Filled")
    except:
        st.error("Sorry Something Went Wrong")