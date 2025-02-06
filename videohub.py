import streamlit as st

menu=st.sidebar.selectbox("Menu",['Video Categories','Video Ratings'])

if menu=='Video Categories':
    category=st.sidebar.pills('Choose Videos',['All','Education','Animals','Space','Sport','Food'],default='All')
    
    if category=='All' or category=='Education':
        st.subheader("Education")
        '---'

        ed1,ed2,ed3,ed4=st.columns(4)

        with ed1:
            st.image('https://i.ytimg.com/an_webp/HdU_rf7eMTI/mqdefault_6s.webp?du=3000&sqp=CJ7elL0G&rs=AOn4CLBDI1niU_DkJBQbH117rXdW-rbUWg')
            st.write("2-Digit Long Division")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=HdU_rf7eMTI')
            '---'
            
        with ed2:
            st.image('https://i.ytimg.com/vi/5iTOphGnCtg/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD3N0YuITBUaDumMSoUjJAuiZLwjw')
            st.write("General Chemistry")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=5iTOphGnCtg')
        with ed3:
            st.image('https://i.ytimg.com/vi/CxGSnA-RTsA/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCCJ9wzBLDhibEkyRw5qiwRVvrPcA')
            st.write("Computer Science")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=CxGSnA-RTsA')
        with ed4:
            st.image('https://i.ytimg.com/vi/pQgxiQAMTTo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDnByTpOrx5GVQChzFpTzbr_39xJg')
            st.write("Engineering Map")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=pQgxiQAMTTo')