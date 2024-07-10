import streamlit as st

st.set_page_config(layout='wide')
colc1,colc2,colc3=st.columns(3)
with colc1:
    i1, i2,i3 = st.columns(3)
    with i2:
        st.image("minecraft.png",use_column_width=True)
with colc2:
    st.title("Mia's Minecraft Adventure Calculator")
    st.write("Welcome to Mia's Minecraft Adventure Calculator! Let's help Mia plan her Minecraft journey.")
with colc3:
    i1, i2,i3 = st.columns(3)
    with i2:
        st.image("minecraft.png",use_column_width=True)
col1,col2,col3=st.columns(3)
with col1:
    st.header("Download the Game")
    download_choice=st.radio("Download The Game: $200", ("None","Yes",'No'))
if download_choice=="Yes":
        download_cost = 200
        with col1:
            st.success("Download Started")
        
        st.write(f"Downloading the game costs: ${download_cost}")
        
        with col2:
            st.header("Choose a World")
            world_choice = st.radio("Select a world:", ("Survival ($20)", "Creative ($100)"))
            if world_choice == "Survival ($20)":
                world_cost = 20
                st.success("Survival World Chosen")
            else:
                world_cost = 100
                st.success("Creative World Chosen")
            st.write(f"Selected world cost: ${world_cost}")

        with col3:
            st.header("Choose Costumes")
            st.write("Select costumes:")
            ninja_costume = st.checkbox("Ninja Costume ($15)")
            wizard_costume = st.checkbox("Wizard Costume ($25)")
            robot_costume = st.checkbox("Robot Costume ($30)")

            costumeNum=0
            total_costumes_cost = 0
            if ninja_costume:
                costumeNum+=1
                total_costumes_cost += 15
            if wizard_costume:
                costumeNum+=1
                total_costumes_cost += 25
            if robot_costume:
                costumeNum+=1
                total_costumes_cost += 30
            st.success(f"{costumeNum} Costume(s) Chosen")

            st.write(f"Selected Costume(s) Cost: ${total_costumes_cost}")
        st.divider()



        colb1,colb2,colb3=st.columns(3)

        with colb1:
            st.header("Add a Farm")
            add_farm = st.checkbox("Add a farm ($25)")
            farm_cost = 25 if add_farm else 0
            st.write(f"Farm cost: ${farm_cost}")
            if add_farm:
                st.success("Farm Added")
        with colb3:
            st.header("Purchase Gems")
            st.write("Select gems:")
            diamonds = st.checkbox("Diamonds ($45)")
            silver = st.checkbox("Silver ($20)")
            gold = st.checkbox("Gold ($30)")

            gemNum=0
            total_gems_cost = 0
            if diamonds:
                total_gems_cost += 45
                gemNum+=1
            if silver:
                total_gems_cost += 20
                gemNum+=1
            if gold:
                total_gems_cost += 30
                gemNum+=1

            st.write(f"Selected gems cost: ${total_gems_cost}")
            st.success(f"{gemNum} Gem(s) Selected")


        with colb2:
            total_cost = download_cost + world_cost + total_costumes_cost + farm_cost + total_gems_cost
            st.title("Total Cost")
            st.write(f"The total cost of Mia's Minecraft adventure is: ${total_cost}")
        st.divider()

else:
    with col1:
        st.error("Must Download To Continue")