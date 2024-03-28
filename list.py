# classwork:
# create a list.py file
# -tell us what a list is in python
# -create an example of a list and display all the list items in python
# -give 3 examples of how to use a list in streamlit (radio, selectbox, sidebar)

# A list is a data collection in python that allows you to store multiple items in a variable and display them to users
import streamlit as st
Phone=['Apple','Samsung','Huawei']
menu=st.sidebar.selectbox('Select Phone Type',Phone)

#The items were 'Apple' 'Samsung' 'Huawei'

opinion=['Yes','No']
opinioncheck=st.radio("Do you like chocolate",opinion)

continentlist=['N.America','S.America','Africa','Europe','Asia','Oceania','Antartica']
continent=st.selectbox("What Continent are You In?",continentlist)

