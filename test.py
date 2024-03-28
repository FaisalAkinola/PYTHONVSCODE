import streamlit as st
import pandas as pd
name='Iphone 15 Pro Max'
price=1199
phonebrand={'Brand':[name],'Price':[price],'Release Date':[2021]}
table=pd.DataFrame(phonebrand)
st.table(table)
st.write(phonebrand)