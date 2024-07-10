import streamlit as st
st.set_page_config(layout='wide')
st.image("Voting.jpg",width=50)
col1,col2=st.columns(2)
with col1:
    st.title("**Voting Registry**")
    st.write("**Enter Your Legal Age:**")
    age=st.number_input("s",0,120,label_visibility='collapsed')
if age >=18:
    with col2:
        st.subheader(":green[**Cast Your Vote**]")
        colb1,colb2,colb3=st.columns(3)
        with colb1:
            st.write("**Vote The Conservative Party**")
            votec=st.button("**Vote Conservative**")
            if votec:
                st.success("You Have Voted For The Conservative Party")
        with colb2:
            st.write ("**Vote The Labour Party**")
            votel=st.button ("**Vote Labour**")
            if votel:
                st.success("You Have Voted For The Labour Party")
        with colb3:
            st.write("**Vote The Democratic Party**")
            voted=st.button("**Vote Democratic**")
            if voted:
                st.success("You Have Voted For The Democratic Party")
else:
    with col1:
        st.error(" You Are Not Eligable To Vote")

    
    