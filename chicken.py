import streamlit as st
st.title("Chicken Cost")
st.subheader("Chickens cost 5 dollars") #header subheader, write, success,info, error, warning
chickens=st.number_input("How many chickens do you want?",0)
cost=chickens*5
checkcost=st.button("Check the cost")
if checkcost:
    st.write('The cost is',cost,'dollars')
    #anpther change made