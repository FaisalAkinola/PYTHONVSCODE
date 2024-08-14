import streamlit as st
import pandas as pd
import plotly.express as px
csvfile=pd.read_csv('players.csv')
menu=st.sidebar.selectbox('Select Menu',['Stat Inputs','Stat Charts'])

if menu=='Stat Inputs':
    name=st.text_input("Input a Player's Full Name")
    right,rightmid,leftmid,left=st.columns(4)
    with right:
        goals=st.number_input("Input a Player's Goals Scored")
    with rightmid:
        assists=st.number_input("Input a Player's Assists Made")
    with leftmid:
        tackles=st.number_input("Input a Player's Tackles Made")
    with left:
        passes=st.number_input("Input a Player's Passes Completed") 
    if st.button("Save Info"):
        st.success("Info Saved")
        playersdict={'Name':[name],'Goals':[goals],'Assists':[assists],'Tackles':[tackles],'Passes':[passes]}
        dataDF=pd.DataFrame(playersdict)
        combinedata=pd.concat([csvfile,dataDF],ignore_index=True)
        combinedata.to_csv('players.csv',index=False)

if menu=='Stat Charts':
    st.table(csvfile)
    #  stats=['Name','Goals','Assists','Tackles','Passes']
    #  statstable=csvfile[stats].value_counts().reset_index()
    # st.table (statstable)

    # orderedgoals=['0-10','11-20','21-30','>30']
    # orderedassists=['0-10','11-20','21-30','>30']
    # orderedtackles=['0-30','21-50','41-70','>70']
    # orderedpasses=['0-800','801-1600','1601-2400','>2400']

    choosechart=st.radio("Choose Stat to Plot",['Goals','Assists','Tackles','Passes'],horizontal=True)
    if choosechart == 'Goals':
        barchart=px.bar(csvfile, x='Name',y='Goals')
        st.plotly_chart(barchart)

    if choosechart == 'Assists':
        barchart=px.bar(csvfile, x='Name',y='Assists')
        st.plotly_chart(barchart)

    if choosechart == 'Tackles':
        barchart=px.bar(csvfile, x='Name',y='Tackles')
        st.plotly_chart(barchart)

    if choosechart == 'Passes':
        barchart=px.bar(csvfile, x='Name',y='Passes')
        st.plotly_chart(barchart)
