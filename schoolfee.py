

#create a simple page for a school. Show on the page the Elementary fee is 5000 dollars and the college fee is 15000 dollars
#Ask how many kids the parent have for elementary and ask if they have for college
#create a dictionary and convert all information to a dataframe after clicking a submit button


import streamlit as st
import pandas as pd
st.header("School Fees")
elementary=st.number_input("How Many Children Do You Want To Enroll In Elementary School?",0,100)
college=st.number_input("How Many Children Do You Want To Enroll In College?",0,100)
elementaryfee=elementary*5000
collegefee=college*15000
totalfee=collegefee+elementaryfee
if st.button("Submit"):
    feedict={'Elementary Children':[elementary],'College Children':[college],'Elementary Fee':[elementaryfee],'College Fee':[collegefee],'Total Fee':[totalfee]}
    feetable=pd.DataFrame(feedict)
    st.table(feetable)

