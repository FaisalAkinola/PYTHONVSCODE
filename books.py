import streamlit as st
import pandas as pd
import plotly.express as px
csvfile=pd.read_csv("books.csv")

menu=st.sidebar.selectbox('Menu',['Input Info','Bookclub Statistics'])

if menu=="Input Info":
    left,right=st.columns(2)
    with left:
        name=st.text_input("Enter Your Name")
        books=st.number_input("How Many Books Have You Read This Semester",0)

    with right:
        genre=st.text_input("Enter Your Favourate Genre")
        pages=st.number_input("How Many Pages Have You Read This Semester",0)

    col1,col2,col3=st.columns(3)
    with col2:
        if st.button("Save Info"):
            st.success("Info Saved")
            booksdict={'Name':[name],'Genre':[genre],'Books':[books],'Pages':[pages]}
            dataDF=pd.DataFrame(booksdict)
            combinedata=pd.concat([csvfile,dataDF],ignore_index=True)
            combinedata.to_csv('books.csv',index=False)
if menu=="Bookclub Statistics":
    st.table(csvfile)

    choice=st.radio('Choose Chart to View',['Pages','Books'])

    if choice=='Books':
        barchart=px.bar(csvfile, x='Name', y='Books')
    if choice=='Pages':
        barchart=px.bar(csvfile, x='Name', y='Pages')
    
    st.plotly_chart(barchart)




