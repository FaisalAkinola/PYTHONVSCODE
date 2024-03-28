import streamlit as st
import pandas as pd
datafile=pd.read_csv('nameage.csv')
menu=st.sidebar.selectbox("Menu",['Insert Data','Data Storage'])
if menu == 'Insert Data':
    name=st.text_input("Enter Name")
    age=st.number_input("Enter Age",3,18)
    if st.button('Enter Data'):
        dict ={'Name':[name],'Age':[age]}
        dataframe=pd.DataFrame(dict)
        combinedata=pd.concat([datafile,dataframe],ignore_index=True)
        combinedata.to_csv('nameage.csv',index=False)
        st.success('Data Submitted')
if menu == 'Data Storage':
    st.table(datafile)