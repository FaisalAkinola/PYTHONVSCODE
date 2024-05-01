import streamlit as st
# st.set_page_config(layout='wide')
Image1,Image2,Image3=st.columns(3)
with Image1:
    st.image("Logo.png",width=50)
col1,col2=st.columns(2)
with Image3:
    st.title(":blue[INVOICE]")
with col1:
    st.write(':blue[Faisaltech]')
    st.write(":blue[471, Camelia 7, Arabian Ranches 8]")
    st.write(':blue[Dubai, UAE]')
    st.write(" ")
    st.write(":blue[**Bill To:**]")




colb1,colb2,colb3=st.columns([2,1,1])


with colb1:
    customer = st.text_input('w',placeholder='Customer Name',label_visibility= 'collapsed')
    adress = st.text_input('w',placeholder='Enter Adress',label_visibility= 'collapsed')  

with colb2:
        st.write(":blue[**Invoice#:**]")
        st.write('')
        st.write(":blue[**Invoice Date:**]")
        st.write('')
        st.write(":blue[**Due Date:**]")
with colb3:
        invoicenum = st.text_input('w',placeholder='Phone Number',label_visibility= 'collapsed')
        Date=st.date_input("Enter Invoice Date",label_visibility='collapsed')
        due=st.date_input("Enter Due Date",label_visibility='collapsed')
st.write("")
st.write("")

colc1,colc2,colc3,colc4=st.columns(4)
with colc1:
    st.write(":blue[**Description**]")
    description=st.text_input("f",label_visibility='collapsed')
with colc2:
     st.write(":blue[**Quantity**]")
     quantity=st.number_input("y",0,label_visibility='collapsed')
with colc3:
     st.write(":blue[**Price**]")
     price=st.number_input("s",0,label_visibility='collapsed')
with colc4:
     st.write(":blue[**Total Price**]")
     total=st.text_input("g",value=quantity*price,label_visibility='collapsed',disabled=True)
     
        
