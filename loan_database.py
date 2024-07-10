import streamlit as st
import pandas as pd

loan_datafile = pd.read_csv('loan_database.csv')

st.title('Loan Eligibility Checker')

menu = st.sidebar.selectbox('Select Menu', ['Check Loan Eligibility', 'Loan Database'])

if menu == 'Check Loan Eligibility':
    st.subheader('Loan Eligibility Checker')
    name = st.text_input("Enter Your Name")
    income = st.number_input("Enter Your Annual Income")
    credit_score = st.number_input("Enter Your Credit Score")

    if st.button("Check Eligibility"):
        eligibility_result = ""
        if income < 30000 or credit_score < 600:
            eligibility_result = "Not eligible for a loan"
        elif 30000 <= income <= 50000 and 600 <= credit_score <= 700:
            eligibility_result = "Eligible for a small loan"
        elif 50000 < income <= 100000 and 700 < credit_score <= 800:
            eligibility_result = "Eligible for a medium loan"
        elif income > 100000 and credit_score > 800:
            eligibility_result = "Eligible for a large loan"
        else:
            eligibility_result = "Not eligible for a loan"

        st.write(f'Hello {name}, {eligibility_result}')
        
        
        loan_dict = {'Name': [name], 'Income': [income], 'Credit Score': [credit_score], 'Eligibility': [eligibility_result]}
        loan_dataframe = pd.DataFrame(loan_dict)
        combined_loan_data = pd.concat([loan_datafile, loan_dataframe], ignore_index=True)
        combined_loan_data.to_csv('loan_database.csv', index=False)

if menu == 'Loan Database':
    st.subheader('Loan Database')
    st.table(loan_datafile)

