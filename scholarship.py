import streamlit as st
import pandas as pd
datafile=pd.read_csv('scholarship.csv')

menu=st.sidebar.selectbox('Select Menu',['Scholarship Eligibility','Scholarship Database'])
if menu == 'Scholarship Eligibility':
    st.write("Enter Your Name:")
    name=st.text_input("s",placeholder='Input Name',label_visibility='collapsed')
    st.write("Enter Mathematics GPA:")
    maths=st.number_input("r",0,4,label_visibility='collapsed')
    st.write('Enter Science GPA:')
    science=st.number_input("f",0,4,label_visibility='collapsed')
    st.write("Enter English GPA:")
    english=st.number_input("g",0,4,label_visibility='collapsed')
    st.write("Enter Humanities GPA:")
    humanities=st.number_input("h",0,4,label_visibility='collapsed')
    st.write("Enter Foreign Languages GPA")
    languages=st.number_input("j",0,4,label_visibility='collapsed')
    total=maths+science+english+humanities+languages
    average=total/5
    eligibility=("")
    if average<2.5:
        eligibility=("Not Eligible For A Scholarship")
    elif average<=3:
        eligibility=("Eligible For Partial Scholarship")
    elif average<=3.5:
        eligibility=("Eligible For Half Scholarship")
    elif average>3.5:
        eligibility=("Eligible For Full Scholarship")
    if st.button('Save Data'):
        st.write(f'Your Average GPA Is {average} And You Are',eligibility)
        dict ={'Name':[name],'Maths GPA':[maths],'Science GPA':[science],'English GPA':[english],'Humanities GPA':[humanities],'Languages GPA':[languages],'Average GPA':[average],'Scholarship Eligibility':[eligibility]}
        dataframe=pd.DataFrame(dict)
        combinedata=pd.concat([datafile,dataframe],ignore_index=True)
        combinedata.to_csv('scholarship.csv',index=False)
if menu==('Scholarship Database'):
    st.table(datafile)
        
        
