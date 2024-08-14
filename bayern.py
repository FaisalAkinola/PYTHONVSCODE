import streamlit as st
import pandas as pd 
import plotly.express as px 
csvfile=pd.read_csv('bayern.csv')

# st.table(csvfile)
st.table(csvfile.head(10))
WinLoss=['Win Loss']
WinLossTable=csvfile[WinLoss].value_counts().reset_index()
st.table(WinLossTable)
renamed=WinLossTable.rename(columns={'Win Loss':'Match Results','count': 'Number Of Matches'})
st.table(renamed)

barchart=px.bar(renamed, x='Match Results',y='Number Of Matches')
st.plotly_chart(barchart)