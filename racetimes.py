import streamlit as st
import pandas as pd
csvfile=pd.read_csv('racetimes.csv')
menu=st.sidebar.selectbox('Menu',['Event Inputs','Event Database'])
if menu=='Event Inputs':
    st.title("Input Race Times")
    col1,col2=st.columns(2)
    with col1:
        name=st.text_input("Enter The Racer's Name")
    with col2:
        time=st.number_input("Enter The Racer's Time")
    category=st.selectbox('Select The Event Category',['Sprints','Middle Run','Long Run'])
    if category=='Sprints':
        distance=st.selectbox('Select The Event Distance',['100M','200M','400M'])
    if category=='Middle Run': 
        distance=st.selectbox('Select The Event Distance',['800M','1500M'])
    if category=='Long Run':
        distance=st.selectbox('Select The Event Distance',['3000M','5000M','10000M'])
    if st.button("Save Info"):
        racedict={'Runner Name':[name],'Race Time':[time],'Race Category':[category],'Race Distance':[distance]}
        raceDF=pd.DataFrame(racedict)
        combinedata=pd.concat([csvfile,raceDF],ignore_index=True)
        combinedata.to_csv('racetimes.csv',index=False)
        
if menu=='Event Database':
    st.table(csvfile)