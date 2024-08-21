# Create an ATM machine using python streamlit.

# Check balance
# Withdraw
# Deposit

# Make use of button, success notifications and error validation.
import streamlit as st 
st.set_page_config(layout="centered")


pic1,pic2,pic3=st.columns([1,3,1])
filename='banklogo.png'
with pic1:
    st.image(filename)
with pic2:    
    st.title("Online ATM")
with pic3:
    st.image(filename)
deposit=0
withdrawal=0
balance=10000

col1,col2=st.columns(2)
with col1:
    deposit=st.number_input("Input Deposit Amount")
with col2:
    withdrawal=st.number_input("Input Withdrawal Amount")
st.divider()
cola1,cola2,cola3=st.columns(3)
balance2=(balance+deposit)-withdrawal

if withdrawal>balance2:
    st.error("Not Enough Money")
else:
    with cola1:
        st.write("Bank Balance")
        st.subheader(f'{balance2}')
    with cola2:
        st.write(f"+{deposit}")
        st.write(f"-{withdrawal}")