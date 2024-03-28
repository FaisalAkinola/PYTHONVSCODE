# Savings App
# Create a python program to ask how much a user wants to save on Monday, Tuesday, up to sunday  
# Add up all his savings
# Show him the total savings for the week
import streamlit as st
monday=st.number_input('Savings for Monday:',0) 
tuesday=st.number_input("Savings for Tuesday:",0)
wednesday=st.number_input("Savings for Wednesday",0)
thursday=st.number_input("Savings for Thursday",0)
friday=st.number_input("Savings for Friday",0)
saturday=st.number_input("Savings for Saturday",0)
sunday=st.number_input("Savings for Sunday",0)

total=st.button("Total Savings")
savings=monday+tuesday+wednesday+thursday+friday+saturday+sunday
if total:
    st.write("You have saved",savings,"Dollars this week.")