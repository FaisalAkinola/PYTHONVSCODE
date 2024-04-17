import streamlit as st
import pandas as pd
datafile=pd.read_csv('employee.csv')
st.set_page_config(layout='wide')
menu=st.sidebar.selectbox('Select Menu',['Register Staff','Staff Database','Staff Search'])
user_id='USER_'+str(len(datafile)+1)

if menu=='Register Staff':
    st.header(":orange[REGISTER STAFF]")
    colu1, colu2 =st.columns(2)
    with colu1:
        name=st.text_input('Name: ')
        email=st.text_input('Email Adress: ')
    with colu2:
        lastname=st.text_input('Last Name:')
        gender=st.selectbox('Gender:',['Male','Female'])
    department=st.selectbox('Department:',['Management','Accounting','Engineering','Human Resources','Security','Medical','Transportation'])
    JT=st.selectbox('Job Title:',['Board of Directors','Supervisor','Senior Staff','Junior Staff','Paid Intern','Unpaid Intern'])
    colh1,colh2 = st.columns(2)
    with colh1:
        contract=st.selectbox('Contract Status:',['Full Time','Part Time'])
    with colh2:
        pay=st.number_input ("Monthly Salary:",0,10000000,value=80000)
    education=st.selectbox('Educational Degree',['None','Associate Degree','Bachelor Degree','Graduate Degree','Professional Degree','Doctorate Degree'])
    date=st.date_input('Employment Date:')
    colg1,colg2=st.columns(2)
    if st.button('Save Employee Data'):
        with colg1:
            st.success('Data Saved')
        employeedict={'First Name':[name],'Last Name':[lastname],'Gender':[gender],'Department':[department],'Job Title':[JT],'Contract Status':[contract],'Monthly Salary':[pay],'Education Degree':[education],'Employment Date':[date],'User ID':[user_id],'Email Adress':[email]}
        dataDF=pd.DataFrame(employeedict)
        combinedata=pd.concat([datafile,dataDF],ignore_index=True)
        combinedata.to_csv('employee.csv',index=False)
        
if menu=='Staff Database':
    st.header(":orange[DATABASE]")
    st.table(datafile)

if menu =='Staff Search':
    side1,side2,side3=st.columns(3)
    with side3:
        st.subheader("Search For Employee Details")
        search= st.text_input("Find Employee Id")
        find = st.button("Find Employee")
    if find:
        if search:
            try:
                search_result=datafile[datafile['User ID'].str.lower()==search.lower()]
                
               
                newID = search_result['User ID'].iloc[0]
                newFN = search_result['First Name'].iloc[0]
                newLN = search_result['Last Name'].iloc[0]
                newGEN = search_result['Gender'].iloc[0]
                newDEP = search_result['Department'].iloc[0]
                newJT = search_result['Job Title'].iloc[0]
                newMS = search_result['Monthly Salary'].iloc[0]
                newEDU = search_result['Education Degree'].iloc[0]
                newED = search_result['Employment Date'].iloc[0]
                newCS = search_result['Contract Status'].iloc[0]
                newEA = search_result['Email Adress'].iloc[0]

                space=' '
                st.title(f'Welcome :blue[{newFN} {space} {newLN}]')
                st.subheader(":blue[Personal Information]")
                st.divider()
                cols1,cols2,cols3= st.columns(3)
            
                with cols1:
                    st.write('Email:')
                    st.write(newEA)
                with cols2:
                    st.write('Gender:')
                    st.write(newGEN)
                with cols3:
                    st.write('Education Degree:')
                    st.write(newEDU)
                st.divider()
                st.subheader(":blue[Job Information]")
                st.divider()
                colf1,colf2,colf3=st.columns(3)
                with colf1:
                    st.write('Employee ID:')
                    st.write(f':violet[{newID}]')
                with colf2:
                    st.write("Department:")
                    st.write(newDEP)
                with colf3:
                    st.write("Date of Employment:")
                    st.write(newED)
                st.divider()
                coli1,coli2,coli3=st.columns(3)
                with coli1:
                    st.write("Job Title:")
                    st.write(newJT)
                with coli2:
                    st.write('Contract Status:')
                    st.write(newCS)
                with coli3:
                    st.write('Salary:')
                    gg=str(newMS)
                    st.write(f"${gg}")
        






            except IndexError:
                   st.error('Input Valid ID')
        else:
            st.error("Please Enter A User ID")
            #change made