import streamlit as st 
import pandas as pd
import plotly.express as px
datafile=pd.read_csv('ClassAttendance.csv')
st.set_page_config(page_title='Class Attendance',page_icon=':school:')
menu=st.sidebar.selectbox('Choose Menu',["Input Info","Info Display"])
st.sidebar.link_button(url='https://stemhackathon.com/question-1-data-apps-hard/',label='Question')
if menu=="Input Info":
    st.title("Attendance Tracker")
    col1,col2=st.columns(2)
    with col1:
        name=st.text_input("Enter the Name of the Student")
        roll=st.number_input("Enter Roll Number",0)
    with col2:
        present=st.number_input("Enter Number of Present Days",0)
        absent=st.number_input("Enter Number of Absent Days",0)
        date=st.date_input("Select Today's Date")
    if st.button("Sumbit"):

        attendancedict={"Name":[name],"Roll":[roll],"Present":[present],"Absent":[absent]}
        dataframe=pd.DataFrame(attendancedict)
        combine=pd.concat([dataframe,datafile],ignore_index=True)
        combine.to_csv("ClassAttendance.csv",index=False)

if menu=="Info Display":
    st.table(datafile)
    '----'
    barchart=px.bar(datafile, x='Name', y=['Present','Absent'],barmode='group')
    st.plotly_chart(barchart)
