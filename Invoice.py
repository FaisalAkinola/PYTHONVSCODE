import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64
csvfile=pd.read_csv('invoice.csv')

st.set_page_config(page_title="Invoice Generator",page_icon=":cyclone",layout="centered",initial_sidebar_state='expanded')




menu=st.sidebar.selectbox('Menu',['Invoice Creator','Change Details'])
if menu=='Change Details':
    
    #logo,name,addr,country,acc name,number,bank name
    adminpass=st.sidebar.text_input("Enter Admin Password",type='password')
    if adminpass=='12345':
        logo=st.file_uploader("Change Your Logo Here",type=['jpg','png','jpeg'])
        savelogo=st.button("Save Image")
        if savelogo:
            filename='logo.jpg'

    
            with open(filename, 'wb') as writename:
                writename.write(logo.getbuffer())
            st.success("Image Changed")
        else:
            st.error("Upload Image File")



        left,right=st.columns(2)
        with left:
            name=st.text_input("Change Company Name Here")
            country=st.text_input("Change Company Country Here")
            accname=st.text_input("Change Account Name Here")
        with right:
            address=st.text_input("Change Company Address Here")
            bank=st.text_input("Change Bank Name Here")
            accnumber=st.text_input("Change Account Number Here")
        if st.button("Save Changes"):
            #changes={'Company Name':[name],'Company Country':[country],'Account Name':[accname],'Company Adress':[address],'Bank Name':[bank],'Account Number':[accnumber]}
            changes={}
            if name:
                changes['name']=[name]
            else:
                changes['name']=csvfile['name'].iloc   [0]
            if country:
                changes['country']=[country]
            else:
                changes['country']=csvfile['country'].iloc[0]
            if accname:
                changes['accname']=[accname]
            else:
                changes['accname']=csvfile['accname'].iloc[0]
            if address:
                changes['address']=[address]
            else:
                changes['address']=csvfile['address'].iloc[0]
            if bank:
                changes['bank']=[bank]
            else:
                changes['bank']=csvfile['bank'].iloc[0]
            if accnumber:
                changes['accnumber']=[accnumber]
            else:
                changes['accnumber']=csvfile['bank'].iloc[0]

            changestable=pd.DataFrame(changes)
            changestable.to_csv('invoice.csv',index=False)
            st.success("Invoice Saved")







if menu=='Invoice Creator':
    name2 = csvfile['name'].iloc[0]
    country2 = csvfile['country'].iloc[0]
    accname2 = csvfile['accname'].iloc[0]
    address2 = csvfile['address'].iloc[0]
    bank2 = csvfile['bank'].iloc[0]
    accnumber2 = csvfile['accnumber'].iloc[0]


    st.sidebar.write("**OPTIONAL**")
    tax=st.sidebar.number_input("Enter Tax %",0,100)
    discount=st.sidebar.number_input("Enter Discount %",0,100)
    
    Image1,Image2,Image3=st.columns(3)
    with Image1:
        st.image("logo.jpg",width=50)
    col1,col2=st.columns(2)
    with Image3:
        st.title(":blue[Invoice]")
    with col1:
        st.write(f':blue[{name2}]')
        st.write(f":blue[{address2}]")
        st.write(f':blue[{country2}]')
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
            Invoicenum = st.text_input('w',placeholder='Invoice Number',label_visibility= 'collapsed')
            Date=st.date_input("Enter Invoice Date",label_visibility='collapsed')
            day=Date.day
            month=Date.strftime('%B')
            year=Date.year
            Date=f'{day} {month} {year}'


            due=st.date_input("Enter Due Date",label_visibility='collapsed')
            day=due.day
            month=due.strftime('%B')
            year=due.year
            due=f'{day} {month} {year}'



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
        total=int(total)
    cole1,cole2,cole3,cole4=st.columns(4)
    with cole2:
        st.write(":blue[**Tax(%)**]")
        taxamount=total*(tax/100)
        st.write(f':blue[{taxamount}]')
    with cole3:
        st.write(":blue[**Discount(%)**]")   
        disamount=total*(discount/100)
        st.write(f':blue[{disamount}]')
        realtotal=total+taxamount-disamount

    st.divider()
    cold1,cold2=st.columns(2)
    with cold1:
        st.write(":blue[**Payment Info**]")
        st.write(f":blue[Acc Name: {accname2}]")
        st.write(f":blue[Acc Number: {accnumber2}]")
        st.write(f":blue[Bank Name: {bank2}]")
    with cold2:
        st.write(":blue[**Payment Due:**]")
        st.header(f":violet[**${realtotal:,}**]")

    def generate_pdf():
        pdf=FPDF()

        pdf.add_page()

        pdf.set_font("Times", size=12)
        colx1=10
        coly1=25

        colw=90
        colh=10
        pdf.set_font("Times", size=25,style='B')
        pdf.image("logo.jpg",x=colx1,y=coly1,w=25)
        pdf.set_xy(colx1+130,coly1)
        pdf.cell(colw,colh, txt='INVOICE',ln=True,align='L')

        pdf.set_font("Times", size=12)
        pdf.set_xy(colx1,coly1+20)
        pdf.cell(colw,colh,txt=f'{name2}',ln=True,align='L')

        pdf.set_xy(colx1,coly1+30)
        pdf.cell(colw,colh,txt=f'{address2}',ln=True,align='L')

        pdf.set_xy(colx1,coly1+40)
        pdf.cell(colw,colh,txt=f'{country2}',ln=True,align='L')

        pdf.set_font("Times", size=12,style='B')
        pdf.set_xy(colx1,coly1+70)
        pdf.cell(colw,colh,txt='Bill To:',ln=True,align='L')

        pdf.set_font("Times", size=12)
        pdf.set_xy(colx1,coly1+80)
        pdf.cell(colw,colh,txt=f'{customer}',ln=True,align='L')

        pdf.set_xy(colx1,coly1+90)
        pdf.cell(colw,colh,txt=f'{adress}',ln=True,align='L')

        pdf.set_xy(colx1+100,coly1+80)
        pdf.cell(colw,colh,txt=f'Invoice#: {Invoicenum}',ln=True,align='L')

        pdf.set_xy(colx1+100,coly1+90)
        pdf.cell(colw,colh,txt=f'Invoice Date: {Date}',ln=True,align='L')

        pdf.set_font("Times", size=12,style='B')
        pdf.set_xy(colx1,coly1+120)
        pdf.cell(colw,colh,txt=f'DESCRIPTION:',ln=True,align='L')

        pdf.set_xy(colx1+70,coly1+120)
        pdf.cell(colw,colh,txt=f'QUANTITY:',ln=True,align='L')

        pdf.set_xy(colx1+115,coly1+120)
        pdf.cell(colw,colh,txt=f'PRICE:',ln=True,align='L')

        pdf.set_xy(colx1+150,coly1+120)
        pdf.cell(colw,colh,txt=f'TOTAL:',ln=True,align='L')


        pdf.set_line_width(0.5)
        pdf.line(colx1,coly1+130,colx1+170,coly1+130)

        pdf.set_xy(colx1,coly1+132)
        pdf.cell(colw,colh,txt=f'{description}',ln=True,align='L')

        pdf.set_xy(colx1+70,coly1+132)
        pdf.cell(colw,colh,txt=f'{quantity:,}',ln=True,align='L')

        pdf.set_xy(colx1+115,coly1+132)
        pdf.cell(colw,colh,txt=f'{price:,}',ln=True,align='L')

        pdf.set_xy(colx1+150,coly1+132)
        pdf.cell(colw,colh,txt=f'${total:,}',ln=True,align='L')
        
        pdf.set_line_width(0.5)
        pdf.line(colx1,coly1+142,colx1+170,coly1+142)

        pdf.set_xy(colx1+115,coly1+140)
        pdf.cell(colw,colh,txt='Tax:',ln=True,align='L')

        pdf.set_xy(colx1+140,coly1+140)
        pdf.cell(colw,colh,txt=f'{taxamount:,}',ln=True,align='L')

        pdf.set_xy(colx1+115,coly1+147)
        pdf.cell(colw,colh,txt='Discount:',ln=True,align='L')

        pdf.set_xy(colx1+140,coly1+147)
        pdf.cell(colw,colh,txt=f'{disamount:,}',ln=True,align='L')




        







        pdf.set_font("Times", size=12,style='B')    
        pdf.set_xy(colx1,coly1+172)
        pdf.cell(colw,colh,txt=f'PAYMENT INFORMATION:',ln=True,align='L')

        pdf.set_font("Times", size=12)
        pdf.set_xy(colx1,coly1+180)
        pdf.cell(colw,colh,txt=f'Acc Name: {accname2}',ln=True,align='L')

        pdf.set_font("Times", size=12)
        pdf.set_xy(colx1,coly1+185)
        pdf.cell(colw,colh,txt=f'Acc Number: {accnumber2}',ln=True,align='L')

        pdf.set_font("Times", size=12)
        pdf.set_xy(colx1,coly1+190)
        pdf.cell(colw,colh,txt=f'Bank Name: {bank2}',ln=True,align='L')

        pdf.set_font("Times", size=12)
        pdf.set_xy(colx1,coly1+195)
        pdf.cell(colw,colh,txt=f'Due Date:{due}',ln=True,align='L')

        pdf.set_font("Times", size=12,style='B')    
        pdf.set_xy(colx1+125,coly1+172)
        pdf.cell(colw,colh,txt=f'PAYMENT DUE:',ln=True,align='L')


        pdf.set_font("Times", size=18,style='B')    
        pdf.set_xy(colx1+125,coly1+182)
        pdf.cell(colw,colh,txt=f'${realtotal:,}',ln=True,align='L')




        pdf_file='invoice.pdf'
        pdf.output(pdf_file)
        return pdf_file


    #Generate the PDF
    pdf_func = generate_pdf()


    #Read the PDF FUNCT as binary data
    with open(pdf_func, 'rb') as binary:
        pdf_data = binary.read()

    but1,but2=st.columns(2)
    # with but2:
        # if customer and adress and Invoicenum and description and quantity and price and Date and due:
        #     if st.button(":blue[View Invoice]"):
        #     #Write the PDF using base64
        #          pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')


        #      #Generate the HTML to embed the PDF
        #          pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'


        #      #Display the embedded pdf (Markdown helps us use HTML in streamlit)
        #          st.markdown(pdf_embed,unsafe_allow_html=True)
    with but1:
            if customer and adress and Invoicenum and description and quantity and price and Date and due:
                st.download_button(label=':blue[**Download PDF**]',data=pdf_data, file_name='GeneratedInvoice.pdf',mime='application/pdf')
            else:
                st.error("Kindly Fill All Boxes")