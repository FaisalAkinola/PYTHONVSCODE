#Enable users to upload and view a CSV file
#Enable users to upload and view an image file
#Enable users to upload and play an audio file
#Enable users to upload and play an video file

      #classwork: 
        # put a button to click to play
        # check to handle errors 
#ability test on uploadCSV
# use a multiselect to choose columns to plot: create a variable called columnslist = 'read your pandas file'.to_list()
# use a radio to choose statistical operators (sum,average,count) #check your previous work

import streamlit as st 
import pandas as pd 
import plotly.express as px
menu=st.sidebar.selectbox("Choose an Option",['Upload CSV','Upload Image','Upload Audio','Upload Video'])


if menu=='Upload CSV':
    st.subheader("Upload CSV & View Data")
    uploadcsv=st.file_uploader("Upload Your CSV File",type='csv')
    if uploadcsv:
        readcsv=pd.read_csv(uploadcsv)

        with st.expander('View CSV Table'):
            st.table(readcsv)

            readcsvcolumn=readcsv.columns

            col1,col2,col3=st.columns(3)
            with col1:
                selectcolumns=st.multiselect("Choose Columns to Plot",readcsvcolumn)
            with col2:
                operator=st.selectbox("Choose Stats Operator",['Average','Sum','Count'])
            with col3:
                selectchart=st.selectbox("Choose Chart to Plot,",['Bar Chart','Pie Chart'])

            if selectcolumns:
                if operator=='Average':
                    ave_op=readcsv[selectcolumns].mean().reset_index()
                    # st.table(ave_op)
                    if selectchart=='Bar Chart':
                        barchart=px.bar(ave_op, x='index',y=0,labels={'index':'Subject','0':'Average'})
                        st.plotly_chart(barchart)
                    elif selectchart=='Pie Chart':
                        piechart=px.pie(ave_op, names='index',values=0,labels={'index':'Subject','0':'Average'})
                        st.plotly_chart(piechart)



if menu==('Upload Image'):
    st.subheader("Upload Image & View Image")
    uploadimage=st.file_uploader("Upload Your Image File",type=['jpeg','jpg','png','webp'])
    if uploadimage:
        with st.expander('View Image'):
            st.image(uploadimage)

if menu==('Upload Audio'):
    st.subheader("Upload Audio & Play Audio")
    uploadaudio=st.file_uploader("Upload Your Audio File",type=['mp3','wav'])

    if uploadaudio:
        st.audio(uploadaudio,format='audio/mp3')

if menu==('Upload Video'):
    st.subheader("Upload Video & Play Video")
    youtubelink=st.text_input("Upload Your Youtube Link")

    try:
        if youtubelink:
            if st.button("Play Video"):        
                st.video(youtubelink)
    except:
        st.error("Can't Play This Video Link")






