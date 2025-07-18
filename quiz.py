import streamlit as st
import pandas as pd
import plotly.express as px



quiz=st.sidebar.selectbox("Menu",['General Knowledge','Personal Quiz'])
if quiz=='General Knowledge':
    st.header("General Knowledge Quiz")
    menu=st.sidebar.selectbox("Menu",['Take Quiz','Quiz Statistics'])
    quizlink="general.csv"

    try:
        quizscores=pd.read_csv(quizlink)
    except:
        quizscores=pd.DataFrame()

    if menu=='Take Quiz':
        name1,name2=st.columns(2)
        with name1:
            name=st.text_input("Enter Your Name")
        if st.pills("Start Quiz",['Start Quiz'],label_visibility='collapsed'):

            col1,col2=st.columns(2)
            with col1:
                q1=st.selectbox("What is the capital of Russia?",['Choose','Kiev','Moscow','Stockholm','Berlin'])
                q2=st.selectbox("What is the square root of 81?",['Choose','99','9','8','81'])
                q3=st.selectbox("How many kilometers does 1 mile equal?",['Choose','15','2.4','1.6','8.64'])
                q4=st.selectbox("What year did WW2 start?",['Choose','1941','1939','1936','1945'])
                q5=st.selectbox("Who discovered gravity?",['Choose','Albert Einstein','Da Vinci','Isaac Newton','Neil Armstrong'])
                q6=st.selectbox("What is waters chemical formula?",['Choose','H2O','CO2','2HO','WTR'])

            with col2:   
                q7=st.selectbox("What is the world's oldest flag?",['Choose','England','India','Denmark','Nepal'])
                q8=st.selectbox("What animal has 3 hearts?",['Choose','Blue Whale','Octopus','Elephant','Giant Squid'])
                q9=st.selectbox("How Tall is Mt. Everest?",['Choose','8172m','8849m','8849km','300m'])
                q10=st.selectbox("What is the world's smallest country?",['Choose','San Marino','Monaco','Vatican City','Liechtenstein'])
                q11=st.selectbox("What is the world's largest country?",['Choose','Canada','U.S','China','Russia'])
                q12=st.selectbox("What is the closes star to our sun",['Choose','Sirius','Pluto','Proxima Centauri','The Milky Way'])


            if st.button("Finish Quiz"):
                if name:
                    if q1 =="Choose" or q2=="Choose" or q3=="Choose" or q4=="Choose" or q5=="Choose" or q6=="Choose" or q7=="Choose" or q8=="Choose" or q9=="Choose" or q10=="Choose" or q11=="Choose" or q12=="Choose":
                        st.error("Some questions have not been answered")
                    else:
                        
                        quizscores.loc[0, name]=0
                        quizscores.to_csv(quizlink,index=False)

                        if q1=='Moscow':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q2=='9':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q3=='1.6':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q4=='1939':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q5=='Isaac Newton':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q6=='H2O':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q7=='Denmark':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q8=='Octopus':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q9=='8849m':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q10=='Vatican City':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q11=='Russia':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q12=='Proxima Centauri':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)

                        percentage=quizscores.loc[0, name]/12.0*100



                        st.success(f"Answers submitted you scored a {percentage}%")  
                else:
                    st.error("Please enter a name")

    if menu=='Quiz Statistics':
        # st.table(quizscores)
        melt_table=quizscores.melt(var_name='Name', value_name='Score')
        melt_table['Percentage'] = ((melt_table['Score']/12.0)*100).round(1)

        chart=st.sidebar.pills("",["Pie Chart","Bar Chart"])



        st.table(melt_table)

        piechart=px.pie(melt_table, names='Name', values='Score')
        barchart=px.bar(melt_table, x='Name', y='Score')

        if chart=="Pie Chart":
                st.plotly_chart(piechart)
        if chart=="Bar Chart":
            st.plotly_chart(barchart)

if quiz=='Personal Quiz':
    st.header("Personal Quiz")
    menu=st.sidebar.selectbox("Menu",['Take Quiz','Quiz Statistics'])
    quizlink="personal.csv"

    try:
        quizscores=pd.read_csv(quizlink)
    except:
        quizscores=pd.DataFrame()

    if menu=='Take Quiz':
        name1,name2=st.columns(2)
        with name1:
            name=st.text_input("Enter Your Name")
        if st.pills("Start Quiz",['Start Quiz'],label_visibility='collapsed'):

            col1,col2=st.columns(2)
            with col1:
                q1=st.selectbox("What is my favourite color?",['Choose','Red','Black','Orange','Blue'])
                q2=st.selectbox("What is my favourite subject?",['Choose','English','Math','Social Studies','Science'])
                q3=st.selectbox("What is my favourite sport?",['Choose','Football','Basketball','Track','Swimming'])
                q4=st.selectbox("What month was I born?",['Choose','September','December','October','August'])
                q5=st.selectbox("What is my favourite food?",['Choose','Chicken Tenders','Chips','Eba','Fried Meat'])
                q6=st.selectbox("What is my favourite drink?",['Choose','Water','Sprite','Ice Tea','Coca-Cola'])

            with col2:   
                q7=st.selectbox("What is my favourite way to travel?",['Choose','Car','Train','Plane','Tram'])
                q8=st.selectbox("What is my favourite device?",['Choose','Phone','Computer','Nintendo','Tablet'])
                q9=st.selectbox("What is my favourite animal",['Choose','Cats','Snakes','Dogs','Cockroaches'])
                q10=st.selectbox("What is my favourite season?",['Choose','Summer','Winter','Autumn','Spring'])
                q11=st.selectbox("How old am I?",['Choose','14','13','12','11'])
                q12=st.selectbox("Where have I lived?",['Choose','France','Germany','Swizerland','Greece'])


            if st.button("Finish Quiz"):
                if name:
                    if q1 =="Choose" or q2=="Choose" or q3=="Choose" or q4=="Choose" or q5=="Choose" or q6=="Choose" or q7=="Choose" or q8=="Choose" or q9=="Choose" or q10=="Choose" or q11=="Choose" or q12=="Choose":
                        st.error("Some questions have not been answered")
                    else:
                        
                        quizscores.loc[0, name]=0
                        quizscores.to_csv(quizlink,index=False)

                        if q1=='Blue':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q2=='Math':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q3=='Football':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q4=='October':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q5=='Chips':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q6=='Ice Tea':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q7=='Plane':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q8=='Computer':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q9=='Dogs':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q10=='Spring':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q11=='13':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)
                        if q12=='Swizerland':
                            quizscores.loc[0, name]+=1
                            quizscores.to_csv(quizlink,index=False)

                        percentage=quizscores.loc[0, name]/12.0*100



                        st.success(f"Answers submitted you scored a {percentage}%")
   
                else:
                    st.error("Please enter a name")

    if menu=='Quiz Statistics':
        # st.table(quizscores)
        melt_table=quizscores.melt(var_name='Name', value_name='Score')
        melt_table['Percentage'] = ((melt_table['Score']/12.0)*100).round(1)

        chart=st.sidebar.pills("",["Pie Chart","Bar Chart"])



        st.table(melt_table)

        piechart=px.pie(melt_table, names='Name', values='Score')
        barchart=px.bar(melt_table, x='Name', y='Score')

        if chart=="Pie Chart":
                st.plotly_chart(piechart)
        if chart=="Bar Chart":
            st.plotly_chart(barchart)