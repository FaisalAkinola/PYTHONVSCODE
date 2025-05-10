import streamlit as st
import webbrowser
import pandas as pd
import plotly.express as px

videolink = "videoviews.csv"

try:
    videoviews=pd.read_csv(videolink)

except:
    videoviews=pd.DataFrame()





menu=st.sidebar.selectbox("Menu",['Video Categories','Video Ratings'])



if menu=='Video Ratings':
    # st.table(videoviews)
    melt_table=videoviews.melt(var_name='Video Title', value_name='Views')
    # st.table(melt_table)
    chart= st.sidebar.pills('Choose Chart',['Bar','Pie','All'])
    piechart=px.pie(melt_table, names='Video Title', values='Views')
    barchart=px.bar(melt_table, x='Video Title', y='Views')
    if chart =='All'or chart=='Bar':
        st.plotly_chart(barchart)

    if chart=='All' or chart== 'Pie':
        st.plotly_chart(piechart)

if menu=='Video Categories':
    category=st.sidebar.pills('Choose Videos',['All','Education','Animals','Space','Food'],default='All')

    
    if category=='All' or category=='Education':
        st.subheader("Education")
        '---'

        ed1,ed2,ed3,ed4=st.columns(4)

        with ed1:
            st.image('data:image/jpeg;base64,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')
            st.write("2-Digit Long Division")

            if st.button("Play Video",key=1):
                webbrowser.open('https://www.youtube.com/watch?v=HdU_rf7eMTI')

                try:
                    videoviews.loc[0, '2-Digit Long Division'] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, '2-Digit Long Division'] =1
                    videoviews.to_csv(videolink,index=False)    


            '---'
            st.image('https://i.ytimg.com/vi/3tisOnOkwzo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLC4s4aH8s4Bvq09EXK_0F0A2GKLHg')
            st.write("General Biology")
            if st.button("Play Video",key=2):
                webbrowser.open('https://www.youtube.com/watch?v=3tisOnOkwzo')
                try:
                    videoviews.loc[0, 'General Biology'] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, 'General Biology'] =1
                    videoviews.to_csv(videolink,index=False)    

        with ed2:
            st.image('https://i.ytimg.com/vi/5iTOphGnCtg/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD3N0YuITBUaDumMSoUjJAuiZLwjw')
            st.write("General Chemistry")
            if st.button("Play Video",key=3):
                webbrowser.open('https://www.youtube.com/watch?v=5iTOphGnCtg')
                try:
                    videoviews.loc[0, 'General Chemistry'] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, 'General Chemistry'] =1
                    videoviews.to_csv(videolink,index=False)    

        
            '---'
            st.image('https://i.ytimg.com/vi/88bMVbx1dzM/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAY0-BLX8cc1YWIdfh9C2kx-EH2Fg')
            st.write("What If You Keep Zooming In?")
            if st.button("Play Video",key=4):
                webbrowser.open('https://www.youtube.com/watch?v=88bMVbx1dzM')
                try:
                    videoviews.loc[0, "What If You Keep Zooming In?"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "What If You Keep Zooming In?"] =1
                    videoviews.to_csv(videolink,index=False)   
        with ed3:
            st.image('https://i.ytimg.com/vi/CxGSnA-RTsA/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCCJ9wzBLDhibEkyRw5qiwRVvrPcA')
            st.write("Computer Science")
            if st.button("Play Video",key=5):
                webbrowser.open('https://www.youtube.com/watch?v=CxGSnA-RTsA')
                try:
                    videoviews.loc[0, "Computer Science"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Computer Science"] =1
                    videoviews.to_csv(videolink,index=False)  
            '---'
            st.image('https://i.ytimg.com/vi/9zCH37330f8/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCXGIMilh-Rpwa3Qj7SrK3TgEMw4w')
            st.write("Allergies Explained")
            if st.button("Play Video",key=6):
                webbrowser.open('https://www.youtube.com/watch?v=9zCH37330f8&t=614s')
                try:
                    videoviews.loc[0, "Allergies Explained"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Allergies Explained"] =1
                    videoviews.to_csv(videolink,index=False)
        with ed4:
            st.image('https://i.ytimg.com/vi/pQgxiQAMTTo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDnByTpOrx5GVQChzFpTzbr_39xJg')
            st.write("Engineering Map")
            if st.button("Play Video",key=7):
                webbrowser.open('https://www.youtube.com/watch?v=pQgxiQAMTTo')
                try:
                    videoviews.loc[0, "Engineering Map"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Engineering Map"] =1
                    videoviews.to_csv(videolink,index=False)
            '---'
            st.image('https://i.ytimg.com/vi/HpcTJW4ur54/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLA2479iRov2yvr2bVAbPMAvExQuCA')
            st.write("How to Terraform Mars")
            if st.button("Play Video",key=8):
                webbrowser.open('https://www.youtube.com/watch?v=HpcTJW4ur54&t=594s')
                try:
                    videoviews.loc[0, "How to Terraform Mars"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "How to Terraform Mars"] =1
                    videoviews.to_csv(videolink,index=False)





    if category=='All' or category=='Animals':
        st.subheader("Animals")
        '---'
        an1,an2,an3,an4=st.columns(4)
        with an1:
            st.image('https://i.ytimg.com/vi/pRenHo1iv8Y/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBlWq7lCpndPES1RyTcO1xTUuSoyA')
            st.write("Frozen Forest Life")
            if st.button("Play Video",key=9):
                webbrowser.open('https://www.youtube.com/watch?v=pRenHo1iv8Y')
                try:
                    videoviews.loc[0, "Frozen Forest Life"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Frozen Forest Life"] =1
                    videoviews.to_csv(videolink,index=False)

            '---'
            st.image('https://i.ytimg.com/vi/m1IUGdK7X0U/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDEBEr9k2cvPp-g9RlHq4GCjNyEsg')
            st.write("Oceans Odysseys")
            if st.button("Play Video",key=10):
                webbrowser.open('https://www.youtube.com/watch?v=m1IUGdK7X0U')
                try:
                    videoviews.loc[0, "Oceans Odysseys"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Oceans Odysseys"] =1
                    videoviews.to_csv(videolink,index=False)

        with an2:
            st.image('https://i.ytimg.com/vi/ZCYDe0mU2Iw/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCbpkW7HALNZme6jSdVIc7Uli9lAg')
            st.write("Equator Wildlife")
            if st.button("Play Video",key=11):
                webbrowser.open('https://www.youtube.com/watch?v=ZCYDe0mU2Iw')
                try:
                    videoviews.loc[0, "Equator Wildlife"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Equator Wildlife"] =1
                    videoviews.to_csv(videolink,index=False)

            '---'
            st.image('https://i.ytimg.com/vi/GXnfBYPsAuE/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLByUn8E8Ms5O-9ltDZm-43s2k7SWg')
            st.write("Winter Wildlife")
            if st.button("Play Video",key=12):
                webbrowser.open('https://www.youtube.com/watch?v=u-dEnJpCGAQ')
                try:
                    videoviews.loc[0, "Winter Wildlife"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Winter Wildlife"] =1
                    videoviews.to_csv(videolink,index=False)

        with an3:
            st.image('https://i.ytimg.com/vi/u-dEnJpCGAQ/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLASQtMQ8_oAbpLoXAhnxscd_uPaqg')
            st.write("Wild Animal World")
            if st.button("Play Video",key=13):
                webbrowser.open('https://www.youtube.com/watch?v=u-dEnJpCGAQ&t=1879s')
                try:
                    videoviews.loc[0, "Wild Animal World"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Wild Animal World"] =1
                    videoviews.to_csv(videolink,index=False)

            '---'
            st.image('https://i.ytimg.com/vi/OlbOOzX_fDs/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAjC_ZHLqThbmpCUyvYlYXjMtywTw')
            st.write("World's Deadliest")
            if st.button("Play Video",key=14):
                webbrowser.open('https://www.youtube.com/watch?v=OlbOOzX_fDs')
                try:
                    videoviews.loc[0, "World's Deadliest"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "World's Deadliest"] =1
                    videoviews.to_csv(videolink,index=False)

        with an4:
            st.image('https://i.ytimg.com/vi/4IenX7OHumk/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBWscdDWEUPf3WRzCN2rSCGUXEM1g')
            st.write("Savage Kingdom")
            if st.button("Play Video",key=15):
                webbrowser.open('https://www.youtube.com/watch?v=4IenX7OHumk')
                try:
                    videoviews.loc[0, "Savage Kingdom"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Savage Kingdom"] =1
                    videoviews.to_csv(videolink,index=False)

            '---'
            st.image('https://i.ytimg.com/vi/zRuuRPM3X3o/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBFuCUhuJ6NSOLijWqioBvHiod2DQ')
            st.write("Enchanting Forests")
            if st.button("Play Video",key=16):
                webbrowser.open('https://www.youtube.com/watch?v=zRuuRPM3X3o')
                try:
                    videoviews.loc[0, "Enchanting Forests"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Enchanting Forests"] =1
                    videoviews.to_csv(videolink,index=False)


    if category=='All' or category=='Space':
        st.subheader("Space")
        '---'
        sp1,sp2,sp3,sp4=st.columns(4)
        with sp1:
            st.image('https://i.ytimg.com/vi/hyNwBiCs7Ro/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLArY_mOEbjK08L-GXH84wt1jxL05A')
            st.write("Unexplained Universe")
            if st.button("Play Video",key=17):
                webbrowser.open('https://www.youtube.com/watch?v=hyNwBiCs7Ro')
                try:
                    videoviews.loc[0, "Unexplained Universe"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Unexplained Universe"] =1
                    videoviews.to_csv(videolink,index=False)
        
            '---'
            st.image('https://i.ytimg.com/vi/tVs7MwizT50/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDUYMg_nFETbN8iR76QVXuHgehjRQ')
            st.write("Anomalies of Space")
            if st.button("Play Video",key=18):
                webbrowser.open('https://www.youtube.com/watch?v=tVs7MwizT50')
                try:
                    videoviews.loc[0, "Anomalies of Space"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Anomalies of Space"] =1
                    videoviews.to_csv(videolink,index=False)

        with sp2:
            st.image('https://i.ytimg.com/vi/iqnpZngxYMs/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBbXMEmngxRyAToTEPpu1SCXlXSYQ')
            st.write("Cosmophobia")
            if st.button("Play Video",key=19):
                webbrowser.open('https://www.youtube.com/watch?v=ZCYDe0mU2Iw')
                try:
                    videoviews.loc[0, "Cosmophobia"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Cosmophobia"] =1
                    videoviews.to_csv(videolink,index=False)
        
            '---'
            st.image('data:image/jpeg;base64,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')
            st.write("What Voyager Saw")
            if st.button("Play Video",key=20):
                webbrowser.open('https://www.youtube.com/watch?v=UyzBoUvN3PM')
                try:
                    videoviews.loc[0, "What Voyager Saw"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "What Voyager Saw"] =1
                    videoviews.to_csv(videolink,index=False)
        with sp3:
            st.image('https://i.ytimg.com/vi/34OJXQeIn64/maxresdefault.jpg')
            st.write("Beyond the Universe")
            if st.button("Play Video",key=21):
                webbrowser.open('https://www.youtube.com/watch?v=34OJXQeIn64')
                try:
                    videoviews.loc[0, "Beyond the Universe"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Beyond the Universe"] =1
                    videoviews.to_csv(videolink,index=False)
            '---'
            st.image('https://i.ytimg.com/vi/Yla5i5tzXKE/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDwg6Jc_oDlNW2rqPWt3_Tkjsf_BQ')
            st.write("The Milky Way")
            if st.button("Play Video",key=22):
                webbrowser.open('https://www.youtube.com/watch?v=Yla5i5tzXKE')
                try:
                    videoviews.loc[0, "The Milky Way"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "The Milky Way"] =1
                    videoviews.to_csv(videolink,index=False)
        with sp4:
            st.image('https://i.ytimg.com/vi/1Ul2tR7qxqM/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCXH4HCPHZtENVPrcho4HKpeTg5hQ')
            st.write("James Webb Telescope")
            if st.button("Play Video",key=23):
                webbrowser.open('https://www.youtube.com/watch?v=1Ul2tR7qxqM')
                try:
                    videoviews.loc[0, "James Webb Telescope"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "James Webb Telescope"] =1
                    videoviews.to_csv(videolink,index=False)
            '---'
            st.image('https://i.ytimg.com/vi/CQVNu_RODM8/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAylJmFXA65K2tl5K9L32y8-TtmBg')
            st.write("3 Hours Space Facts")
            if st.button("Play Video",key=24):
                webbrowser.open('https://www.youtube.com/watch?v=CQVNu_RODM8')
                try:
                    videoviews.loc[0, "3 Hours Space Facts"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "3 Hours Space Facts"] =1
                    videoviews.to_csv(videolink,index=False)


    if category=='All' or category=='Food':
        st.subheader("Food")
        '---'
        fo1,fo2,fo3,fo4=st.columns(4)
        with fo1:
            st.image('https://i.ytimg.com/vi/1IETVrtbYbg/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLD4mlp8Pr1mLOZTOZ6bnyuQA1mtaw')
            st.write("Restuarant Stir-Fry")
            if st.button("Play Video",key=25):
                webbrowser.open('https://www.youtube.com/watch?v=1IETVrtbYbg')
                try:
                    videoviews.loc[0, "Restuarant Stir-Fry"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Restuarant Stir-Fry"] =1
                    videoviews.to_csv(videolink,index=False)
        
            '---'
            st.image('https://i.ytimg.com/vi/03Pug39GA6Y/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLAj0NGdflu35p0F1ijAj59DNvwokA')
            st.write("Pro Chef vs Home Cook")
            if st.button("Play Video",key=26):
                webbrowser.open('https://www.youtube.com/watch?v=03Pug39GA6Y')
                try:
                    videoviews.loc[0, "Pro Chef vs Home Cook"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Pro Chef vs Home Cook"] =1
                    videoviews.to_csv(videolink,index=False)

        with fo2:
            st.image('https://i.ytimg.com/vi/Hju_pkIqa28/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBguhS4Mif7QEdkw5pXjj2N9YU-kA')
            st.write("Most Expensive Cheese")
            if st.button("Play Video",key=27):
                webbrowser.open('https://www.youtube.com/watch?v=Hju_pkIqa28')
                try:
                    videoviews.loc[0, "Most Expensive Cheese"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Most Expensive Cheese"] =1
                    videoviews.to_csv(videolink,index=False)
            '---'
            st.image('https://i.ytimg.com/vi/D4-xSUJGpuY/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLCZpOHPoAHNXlTp2ByhwK9sFQHQfA')
            st.write("Burger Competition")
            if st.button("Play Video",key=28):
                webbrowser.open('https://www.youtube.com/watch?v=D4-xSUJGpuY')
                try:
                    videoviews.loc[0, "Burger Competition"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Burger Competition"] =1
                    videoviews.to_csv(videolink,index=False)
        with fo3:
            st.image('https://i.ytimg.com/vi/XnQ7Py8D6v0/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDV5jzb6artxgQ7FguT0GoFm5TPJg')
            st.write("Japanese Fast Food")
            if st.button("Play Video",key=29):
                webbrowser.open('https://www.youtube.com/watch?v=XnQ7Py8D6v0')
                try:
                    videoviews.loc[0, "Japanese Fast Food"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Japanese Fast Food"] =1
                    videoviews.to_csv(videolink,index=False)
            '---'
            st.image('https://i.ytimg.com/vi/VI83td8OJyo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLB30ez--NMTnDfYlEWZ8fK21PFMlg')
            st.write("UK vs USA Cheese")
            if st.button("Play Video",key=30):
                webbrowser.open('https://www.youtube.com/watch?v=VI83td8OJyo')
                try:
                    videoviews.loc[0, "UK vs USA Cheese"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "UK vs USA Cheese"] =1
                    videoviews.to_csv(videolink,index=False)
        with fo4:
            st.image('https://i.ytimg.com/vi/pD9mk0Y_pyo/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDmP-RrLFk0thvVjHNte4HqzLweZg')
            st.write("Global School Lunches")
            if st.button("Play Video",key=31):
                webbrowser.open('https://www.youtube.com/watch?v=pD9mk0Y_pyo&t=12s')
                try:
                    videoviews.loc[0, "Global School Lunches"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Global School Lunches"] =1
                    videoviews.to_csv(videolink,index=False)
            '---'
            st.image('https://i.ytimg.com/vi/y8cm_QLbLX0/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLARV_7P1NtFR6wLCrqXh20XCThiyA')
            st.write("Michelin Street Tacos")
            if st.button("Play Video",key=32):
                webbrowser.open('https://www.youtube.com/watch?v=y8cm_QLbLX0')
                try:
                    videoviews.loc[0, "Michelin Street Tacos"] +=1
                    videoviews.to_csv(videolink,index=False)
                except KeyError:
                    videoviews.loc[0, "Michelin Street Tacos"] =1
                    videoviews.to_csv(videolink,index=False)