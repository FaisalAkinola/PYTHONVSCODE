import streamlit as st

st.title("Arithmetic Calculator")
col1,col2=st.columns(2)

with col1:
    num1=st.number_input("s",0,label_visibility='collapsed',placeholder="Enter Your First Number")
    num2=st.number_input("f",0,label_visibility='collapsed',placeholder="Enter Your Second Number")
    num3=0
with col2:
    cola1,cola2=st.columns(2)
    with cola1:
        add=st.button("_+_")
        if add:
            num3=num1+num2
        minus=st.button("_-_")
        if minus:
            num3=num1-num2
    with cola2:
        times=st.button("x")
        if times:
            num3=num1*num2
        divide=st.button("÷")
        if divide:
            num3=num1/num2
st.write(f"Answer = {num3}")
