# -Add title==
#Add a restaurant picture==
# -shows them the food selections
# -After they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill

#meals, drinks, fruits, snacks

import streamlit as st
st.set_page_config(layout="wide")
st.title("Pay N Eat Restaurant")
st.image("https://cdn.pixabay.com/photo/2017/07/07/22/19/someone-2482972_1280.jpg")


menu=['Meals','Drinks','Dessert']
selectmenu=st.sidebar.selectbox('Select a Menu Category',menu)
bill=0
if selectmenu == 'Meals':
    st.subheader("Meals")
    meal1, meal2, meal3, meal4 = st.columns(4)
    with meal1:
        if st.checkbox("Rice And Chicken: $12"):
            st.success("Added to Menu")
            bill +=12
    with meal2:
        if st.checkbox("Spag And Sauce: $10"):
            st.success("Added to Menu")
            bill +=10
    with meal3:
        if st.checkbox('Ofada Rice And Sauce: $10'):
            st.success("Added to Menu")
            bill +=10
    with meal4:
        if st.checkbox("Chips And Chicken: $14"):
            st.success("Added to Menu")
            bill +=14
elif selectmenu == 'Drinks':
    st.subheader("Drinks")
    drink1 ,drink2 ,drink3 ,drink4 = st.columns(4)
    with drink1:
     if st.checkbox("Water: $2"):
        st.success("Added to Menu")
        bill +=2
    with drink2:
        if st.checkbox("Coca-Cola: $5"):
            st.success("Added to Menu")
            bill +=5
    with drink3:
        if st.checkbox("Iced Tea: $4"):
            st.success("Added to Menu")
            bill +=4
    with drink4:
        if st.checkbox("Orange Juice: $3"):
            st.success("Added to Menu")
            bill +=3
elif selectmenu=='Dessert':
        st.subheader("Desserts")
        dessert1 ,dessert2 ,dessert3 ,dessert4 =st.columns(4)
        with dessert1:
            if st.checkbox('Spongecake: $6'):
                    st.success("Added to Menu")
                    bill +=6
        with dessert2:
            if st.checkbox("Ice Cream: $4"):
                    st.success("Added to Menu")
                    bill +=4
        with dessert3:
            if st.checkbox("Red Velvet Cake: $6"):
                    st.success("Added to Menu")
                    bill +=6
        with dessert4:
            if st.checkbox("Chocolate Fondue: $6"):
                    st.success("Added to Menu")
                    bill +=6
if st.button("Check Bill"):
 st.write("The Bill is:",bill,"Dollars")
bill1,bill2,bill3=st.columns(3)
with bill1:
 if st.checkbox("Would you like to share the bill?:"):
            people= st.slider("How many: ",2,50)
            perbill=bill/people
            st.write("Bill per person:",perbill,"Dollars")