import streamlit as st
import pandas as pd
st.set_page_config(page_title='School Invoice',page_icon='🏫')
csvfile=pd.read_csv('schoolinvoice.csv')
studentID='Student'+ str(len(csvfile)+ 1)


# first page (REGISTER STUDENT)
# -ask to register student
# name, class, parentname, email, phone, address

menu=st.sidebar.selectbox("Menu",['Register Student','Add Payment','Download Receipts','Admin Panel'])

if menu == 'Register Student':
    title1,title2,title3=st.columns([25,50,25])
    with title2: 
        st.header(":blue[*Student Registration*]")
    st.write ("")

    with st.form("Student Registration",clear_on_submit=True):
        right,left=st.columns(2)
        with right:
            st.write("**Enter Student's Name**")
            name=st.text_input('w',placeholder='Student Name',label_visibility= 'collapsed')
            st.divider()
            st.write("**Enter Guardian's Name**")
            guardian=st.text_input('w',placeholder='Guardian Name',label_visibility= 'collapsed')
            st.divider()
            st.write("**Enter Guardian's Phone Number**")
            phone=st.text_input('w',placeholder='Guardian #',label_visibility= 'collapsed')

        with left:
            st.write("**Enter Student's Year**")
            year=st.selectbox('w',['Year 1','Year 2','Year 3','Year 4','Year 5','Year 6','Year 7','Year 8','Year 9','Year 10','Year 11','Year 12'],placeholder='Select Students Year',label_visibility= 'collapsed')
            st.divider()
            st.write("**Enter Guardian's Email**")
            email=st.text_input('w',placeholder='Guardian Email',label_visibility= 'collapsed')
            st.divider()
            st.write("**Enter Home Adress**")
            adress=st.text_input('w',placeholder='Home Address',label_visibility= 'collapsed')

        if st.form_submit_button('Complete Registration'):
            schooldict={'StudentID':[studentID],'First Name':[name],'Guardian':[guardian],'Phone':[phone],'Year':[year],'Email':[email],'Adress':[adress],'Guardian Email':[email]}
            dataDF=pd.DataFrame(schooldict)
            combinedata=pd.concat([csvfile,dataDF],ignore_index=True)
            combinedata.to_csv('schoolinvoice.csv',index=False)
            st.success("Student Registered")
if menu == 'Add Payment':

    
    cola,colb,colc=st.columns([1,3,1])
    with colc:
        searchbox=st.text_input("Enter Student ID")
        savebutton=st.button("Search For Student's ID")

    if savebutton:
        if searchbox:
            searchresult=csvfile[csvfile['StudentID'].str.lower()==searchbox.lower()]
            st.table(searchresult)
            getname=searchresult['First Name'].iloc[0]
            getgrade=searchresult['Year'].iloc[0]

            st.subheader(f':blue[**{getname}**]')
            st.write(f"{getgrade}")

if menu=='Admin Panel':
    adminpass=st.sidebar.text_input("Enter Admin Password",type='password')
    if adminpass:
        if adminpass=='admin':
            st.sidebar.success("Welcome Admin!")
        else:
            st.sidebar.error("Incorrect Password, Try Again")



    