import streamlit as st
st.set_page_config(layout='wide')
import pandas as pd
import plotly.express as px

csvlink=pd.read_csv('scores.csv')

menu=st.sidebar.selectbox('Select Menu',['Scores Input','Database|Chart'])
colu1,colu2,colu3=st.columns([1,2,1])
if menu == 'Scores Input':
    with colu2:
        st.header("Enter Students Scores")
    name=st.text_input("Enter The Pupil's Name")
    colu4,colu5=st.columns(2)
    with colu4:
        mathscore=st.number_input("Pupil's Maths Score: ",0,100,value=70)
        englishscore=st.number_input("Pupil's English Score: ",0,100,value=70)
        geoscore=st.number_input("Pupil's Geography Score: ",0,100,value=70)
    with colu5:
        histscore=st.number_input("Pupil's History Score: ",0,100,value=70)
        sciscore=st.number_input("Pupil's Science Score: ",0,100,value=70)
        arabscore=st.number_input("Pupil's Arabic Score: ",0,100,value=70)
        



    combinescore=mathscore+englishscore+geoscore+histscore+sciscore+arabscore
    averagescore=combinescore / 6
    if averagescore >= 90: 
        grade="A+"
    elif averagescore >= 80: 
        grade="A"
    elif averagescore >= 70: 
        grade="B"
    elif averagescore >= 60: 
        grade="C"
    elif averagescore >= 50: 
        grade="D"
    elif averagescore <  50: 

        grade="F"

    averageround=str(round(averagescore, 2))

    # Name,Mathematics,English,Geography,History,Science,Arabic,Total,Average,Grade
    if st.button("Submit Scores"):
            col1, col2, col3 =st.columns(3)
            with col1:
                st.success ('Scores Submitted')
            studentsdict = {'Name':[name],'Mathematics':[mathscore],'English':[englishscore],
                            'Geography':[geoscore],'History':[histscore],'Science':[sciscore],
                            'Arabic':[arabscore],'Total':[combinescore],'Average':[averageround],
                            'Grade':[grade]}
            students_table = pd.DataFrame(studentsdict)
            new_table = pd.concat([csvlink,students_table],ignore_index=True) #this will merge the two dataframes together
            new_table.to_csv("scores.csv",index=False)#both should ignore index positions in the table

if menu == 'Database|Chart':
    cola1,cola2,cola3=st.columns([1,2,1])
    with cola2:
        st.header("Students Database")   
    st.table(csvlink)
    
    subjects=['Mathematics','English','Geography','History','Science','Arabic']
    subjectstable=csvlink[subjects].mean().reset_index()
    renamedcolumns=subjectstable.rename(columns={'index':'Subject',0:'Average'})
   # st.table(renamedcolumns)
    

    chart1,chart2,chart3=st.columns(3)
    with chart1:
        choosechart=st.radio("Choose Chart to Plot",['Barchart','Piechart'],horizontal=True)
        choosesubject=st.multiselect("Choose Subject")


    barchart=px.bar(renamedcolumns, x='Subject', y='Average')
    piechart=px.pie(renamedcolumns, names='Subject', values='Average' )
    colb1,colb2,colb3=st.columns(3)
    # with colb2:
        # chart=st.selectbox('Select Chart',['Pie Chart','Bar Chart'])
    if choosechart == 'Bar Chart':
        st.plotly_chart(barchart)

    if choosechart=='Pie Chart':
        st.plotly_chart(piechart)

