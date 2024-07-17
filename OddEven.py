import streamlit as st

st.title("Even or Odd Checker")

name = st.text_input("Enter your name:")
number = st.number_input("Enter a number:",0)

if number % 2 == 0:
    result = "even"
else:
    result = "odd"

st.write(f"Hello {name}, the number {number} is {result}.")
