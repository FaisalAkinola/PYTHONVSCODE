import streamlit as st
import pandas as pd 
readcsv=pd.read_csv("Donation.csv")
readsum=pd.read_csv("Donations.csv")


menu=st.sidebar.selectbox('Donation Menu',["Create Donation","View Donation"])

if menu== "Create Donation":

    st.title("Create Donation")
    "------------"
    left,right=st.columns(2)
    with left:
        title=st.text_input("Campaign Title",placeholder="Campaign Title Here")
    with right:
        email=st.text_input("Email Adress",placeholder="________@____.__")
    "------------"
    details=st.text_area("Campaign Details",placeholder="Details, Description and Anything to Convince People to Donate!")
    goalselect=st.selectbox("Select A Goal",['0-500','501-5000','5001-50000','50001-300000','300001-1000000'])
    if goalselect:
        if goalselect =='0-500': 
            goal=st.slider("Goal Amount",0,500,250)
        if goalselect =='501-5000':
            goal=st.slider("Goal Amount",501,5000,2500)
        if goalselect =='5001-50000':
            goal=st.slider("Goal Amount",5001,50000,25000)
        if goalselect =='50001-300000':
            goal=st.slider("Goal Amount",50001,300000,150000)
        if goalselect =='300001-1000000':
            goal=st.slider("Goal Amount",300000,1000000,500000)

    if st.button("Submit Donation"):
        st.write (f"The Selected Goal Amount is :green[${goal}]")
        dntdict={'Title':[title],'Email':[email],'Details':[details],'Goal':[goal]}
        table=pd.DataFrame(dntdict)
        join=pd.concat([readcsv,table],ignore_index=True)
        join.to_csv('Donation.csv',index=False)
            
if menu=="View Donation":
    st.subheader("View Donations")
    '--------'
    dnttitle=readcsv['Title']
    # st.write(dnttitle)
    selectitle=st.selectbox("Select Donation to View",dnttitle)


    filtertitle=readcsv[readcsv['Title']==selectitle]
    getdetails=filtertitle['Details'].iloc[0]
    getmail=filtertitle['Email'].iloc[0]
    getgoal=filtertitle['Goal'].iloc[0]
    # st.write(filtertitle)

    filterdonations=readsum[readsum[selectitle]]
    get_donations=filterdonations[filterdonations['Donations']].iloc





    '---------'
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Campaign Details")
        donatecash=st.number_input("Donate To A Cause",0,placeholder='$___')
    with col2:
        st.success(f":green[Funds Raised]")
        st.warning(f":orange[Funds Goal: {getgoal}] ")

    '--------'
    if st.button ("Donate Now"):
        st.success("Thanks For Your Contribution")
        # donate_dict=
    st.write(getdetails)
    st.write(getmail)