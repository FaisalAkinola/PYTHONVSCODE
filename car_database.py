import streamlit as st
import pandas as pd
datafile=pd.read_csv('car_database.csv')
menu=st.sidebar.selectbox('Select Menu',['Buy Car','Car Database'])
if menu==('Buy Car'):
    name=st.text_input("Enter Your Name")
    salary=st.number_input("Enter Your Salary")
    affordable_car=("")
    if salary < 30000:
        affordable_car=("Used Car")
    elif 60000 <= salary <= 100000:
        affordable_car=("Mid Range Car")
    elif 100000 < salary <= 200000:
        affordable_car("Luxury Car")
    else:
        affordable_car=("Supercar")
    if st.button("Save Data"):
        st.write(f'Hello {name}, You Can Afford A {affordable_car}')
        dict ={'Name':[name],'Car':[affordable_car]}
        dataframe=pd.DataFrame(dict)
        combinedata=pd.concat([datafile,dataframe],ignore_index=True)
        combinedata.to_csv('car_database.csv',index=False)
if menu==('Car Database'):
    st.table(datafile)




