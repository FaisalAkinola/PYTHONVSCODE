import streamlit as st

initial_savings = 400

concert_cost = st.number_input("Enter amount spent on concert tickets:")
dinner_cost = st.number_input("Enter amount spent on dinner:")
shopping_cost = st.number_input("Enter amount spent on shopping:")
transportation_cost = st.number_input("Enter amount spent on transportation:")
movie_cost = st.number_input("Enter amount spent on movies:")

total_expenses = concert_cost + dinner_cost + shopping_cost + transportation_cost + movie_cost

amount_left = initial_savings - total_expenses

st.title("John's Financial Planner")
st.write(f"John's total expenses: ${total_expenses}")
st.write(f"Amount left after expenses: ${amount_left}")

if amount_left > 0:
    each_investment = amount_left / 4
    st.write(f"Each investment option will receive: ${each_investment}")
elif amount_left == 0:
    st.write("You have no money left to invest.")
else:
    st.write("You spent more than your initial savings. Cannot invest.")
