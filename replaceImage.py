import streamlit as st

st.header("Upload and Replace Image")

uploadedfile=st.file_uploader("Upload an Image",type=['png','jpg','jpeg'])

if uploadedfile:
    filename='logo.jpg'

    
    with open(filename, 'wb') as writename:
        writename.write(uploadedfile.getbuffer())
    st.write("Image Changed")
else:
 st.write("Upload Image File")