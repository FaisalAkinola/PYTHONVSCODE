import streamlit as st
st.title("welcome to my age calculator")
name=st.text_input("Enter your name")
currentyear=st.number_input("enter your current year",2023)
yob=st.number_input("Enter year of birth",1950,2023)
age=currentyear-yob 
checkage=st.button("Check my age")
if checkage:
    st.write(name,"you will be",age,"in",currentyear)