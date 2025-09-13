import streamlit as st 
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import datetime
import base64

link="medicalquiz.csv"

try:
    score=pd.read_csv(link)
except:
    score=pd.DataFrame()                 


menu=st.sidebar. selectbox("Menu",["Take Quiz","View Results"])

def generate_pdf():
    pdf=FPDF(orientation = 'Landscape', format = 'A4')
    pdf.add_page()

    colx=20
    coly=25

    colw=90
    colh=10
    imageurl='certificate.png'

    pdf.image(imageurl, x=0, y=0, w=300, h=200)
    pdf.set_font("Helvetica", size=40, style='I')
    pdf.set_xy(colx+80, coly+68)
    pdf.cell(colw,colh, txt=st.session_state.user, align='C')

    pdf.set_font("Times", size=24)
    pdf.set_xy(colx+27, coly+125)
    pdf.cell(colw,colh, txt=f"{st.session_state.score}%", align='C')

    pdf.set_xy(colx+145, coly+125)
    pdf.cell(colw,colh, txt=f"{st.session_state.date}", align='C')


    pdf_file=f'{st.session_state.user}certificate.pdf'
    pdf.output(pdf_file)
    return pdf_file



if menu=="Take Quiz":
    if 'currentpage' not in st.session_state:
        st.session_state.currentpage = 'homepage'
        
    # st.write(st.session_state)

    def home():

        st.title("Quiz")
        st.session_state.name=st.text_input("Enter Name")
        
        
        if st.pills("",["Begin"]):
            if st.session_state.name:
                
                st.session_state.currentpage='qf1'
                date=datetime.datetime.now()
                st.session_state.date=date.strftime("%d-%m-%Y")
            
                score.loc[0, st.session_state.name]=0
                score.to_csv(link, index=False)
                st.rerun()
            else:
                st.error("Must Enter A Name to Start")



    def qf1():
        col1, col2 =st.columns(2)
        with col1:
            st.subheader('Question 1')
        

        st.write('')
        '---'

        q1=st. pills('What is the main job of your heart?',[ "A) Pumping blood","B) Digesting food","C) Storing energy","D) Breathing air"])  
        if q1:
            st.session_state.q1=q1
        with col2:
            try:
                if st.session_state.q1== None:
                    st.info("Current Answer: None Selected")
                    
                        
                else:
                    st.info(f"Current Answer: {st.session_state.q1}")
                        
            except:  
                st.info("Current Answer: None Selected")   


        if st.button("Next Question"):
            st.session_state.currentpage='qf2'
            st.rerun()


    def qf2():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 2')
        st.write('')
        '---'
        q2 = st.pills('What do vaccines help protect you from?', ["A) Common cold","B) Diseases like measles and flu","C) Cuts and bruises","D) None of the above"])
        if q2:
            st.session_state.q2 = q2
        with col2:
            try:
                if st.session_state.q2 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q2}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf3'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf1'
            st.rerun()


    def qf3():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 3')
        st.write('')
        '---'
        q3 = st.pills('Why is it important to wash your hands?', ["A) To smell nice","B) To prevent getting sick","C) To look clean","D) None of the above"])
        if q3:
            st.session_state.q3 = q3
        with col2:
            try:
                if st.session_state.q3 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q3}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf4'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf2'
            st.rerun()

  

    def qf4():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 4')
        st.write('')
        '---'
        q4 = st.pills('What should you do if you have a fever?', ["A) Go play outside","B) Tell an adult and rest","C) Eat a lot of candy","D) Stay up late"])
        if q4:
            st.session_state.q4 = q4
        with col2:
            try:
                if st.session_state.q4 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q4}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf5'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf3'
            st.rerun()

    def qf5():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 5')
        st.write('')
        '---'
        q5 = st.pills('What does a doctor do?', ["A) Fix cars","B) Help people stay healthy","C) Teach math","D) None of the above"])
        if q5:
            st.session_state.q5 = q5
        with col2:
            try:
                if st.session_state.q5 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q5}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf6'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf4'
            st.rerun()

    def qf6():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 6')
        st.write('')
        '---'
        q6 = st.pills('What is a healthy snack?', ["A) Candy","B) Fruits and vegetables","C) Chips","D) Soda"])
        if q6:
            st.session_state.q6 = q6
        with col2:
            try:
                if st.session_state.q6 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q6}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf7'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf5'
            st.rerun()

    def qf7():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 7')
        st.write('')
        '---'
        q7 = st.pills('What does it mean to be allergic to something?', ["A) You like it a lot","B) Your body reacts badly to it","C) You can’t eat it","D) None of the above"])
        if q7:
            st.session_state.q7 = q7
        with col2:
            try:
                if st.session_state.q7 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q7}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf8'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf6'
            st.rerun()

    def qf8():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 8')
        st.write('')
        '---'
        q8 = st.pills('What should you do if you get a cut?', ["A) Ignore it","B) Wash it and put a bandage on it","C) Show it to your friends","D) None of the above"])
        if q8:
            st.session_state.q8 = q8
        with col2:
            try:
                if st.session_state.q8 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q8}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf9'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf7'
            st.rerun()

    def qf9():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 9')
        st.write('')
        '---'
        q9 = st.pills('Why is it important to eat breakfast?', ["A) It’s the best meal of the day","B) It gives you energy for school","C) You can skip it","D) None of the above"])
        if q9:
            st.session_state.q9 = q9
        with col2:
            try:
                if st.session_state.q9 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q9}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf10'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf8'
            st.rerun()

    def qf10():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 10')
        st.write('')
        '---'
        q10 = st.pills('What is one way to keep your bones strong?', ["A) Eating junk food","B) Drinking milk or eating dairy","C) Avoiding exercise","D) None of the above"])
        if q10:
            st.session_state.q10 = q10
        with col2:
            try:
                if st.session_state.q10 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q10}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf11'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf9'
            st.rerun()

    def qf11():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 11')
        st.write('')
        '---'
        q11 = st.pills('What is the purpose of first aid?', ["A) To help with homework","B) To give immediate care in emergencies","C) To make food","D) None of the above"])
        if q11:
            st.session_state.q11 = q11
        with col2:
            try:
                if st.session_state.q11 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q11}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf12'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf10'
            st.rerun()

    def qf12():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 12')
        st.write('')
        '---'
        q12 = st.pills('What can help you breathe better when you’re sick?', ["A) Eating ice cream","B) Drinking warm fluids","C) Running around","D) None of the above"])
        if q12:
            st.session_state.q12 = q12
        with col2:
            try:
                if st.session_state.q12 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q12}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf13'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf11'
            st.rerun()

    def qf13():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 13')
        st.write('')
        '---'
        q13 = st.pills('What is a common symptom of a cold?', ["A) Runny nose","B) Happy thoughts","C) Dancing","D) None of the above"])
        if q13:
            st.session_state.q13 = q13
        with col2:
            try:
                if st.session_state.q13 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q13}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf14'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf12'
            st.rerun()

    def qf14():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 14')
        st.write('')
        '---'
        q14 = st.pills('Why should you cover your mouth when you cough?', ["A) To look funny","B) To prevent spreading germs","C) To make a sound","D) None of the above"])
        if q14:
            st.session_state.q14 = q14
        with col2:
            try:
                if st.session_state.q14 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q14}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf15'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf13'
            st.rerun()

    def qf15():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 15')
        st.write('')
        '---'
        q15 = st.pills('What is a safe way to exercise?', ["A) Jumping on the bed","B) Playing sports or riding a bike","C) Sitting all day","D) None of the above"])
        if q15:
            st.session_state.q15 = q15
        with col2:
            try:
                if st.session_state.q15 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q15}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf16'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf14'
            st.rerun()

    def qf16():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 16')
        st.write('')
        '---'
        q16 = st.pills('What does a dentist check?', ["A) Your eyes","B) Your teeth","C) Your hair","D) None of the above"])
        if q16:
            st.session_state.q16 = q16
        with col2:
            try:
                if st.session_state.q16 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q16}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf17'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf15'
            st.rerun()

    def qf17():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 17')
        st.write('')
        '---'
        q17 = st.pills('What should you do if you feel dizzy?', ["A) Keep running","B) Sit down and tell an adult","C) Eat a lot of candy","D) None of the above"])
        if q17:
            st.session_state.q17 = q17
        with col2:
            try:
                if st.session_state.q17 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q17}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf18'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf16'
            st.rerun()

    def qf18():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 18')
        st.write('')
        '---'
        q18 = st.pills('What is the main function of your lungs?', ["A) To pump blood","B) To help you breathe","C) To digest food","D) None of the above"])
        if q18:
            st.session_state.q18 = q18
        with col2:
            try:
                if st.session_state.q18 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q18}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf19'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf17'
            st.rerun()

    def qf19():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 19')
        st.write('')
        '---'
        q19 = st.pills('What can help you stay healthy during cold and flu season?', ["A) Washing hands frequently","B) Eating more sweets","C) Skipping sleep","D) None of the above"])
        if q19:
            st.session_state.q19 = q19
        with col2:
            try:
                if st.session_state.q19 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q19}")
            except:
                st.info("Current Answer: None Selected")
        if st.button("Next Question"):
            st.session_state.currentpage = 'qf20'
            st.rerun()
        if st.button("Previous Question"):
            st.session_state.currentpage = 'qf18'
            st.rerun()

    def qf20():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Question 20')
        st.write('')
        '---'
        q20 = st.pills('What does it mean if someone has a headache?', ["A) They are happy","B) They might need rest or water","C) They want to play","D) None of the above"])
        if q20:
            st.session_state.q20 = q20
        with col2:
            try:
                if st.session_state.q20 == None:
                    st.info("Current Answer: None Selected")
                else:
                    st.info(f"Current Answer: {st.session_state.q20}")
            except:
                st.info("Current Answer: None Selected")
        finish=st.button('Finish')
        if finish:
            if 'q1' not in st.session_state:
                st.error("Question 1 Has Not Been Answered")
            elif st.session_state.q1=="A) Pumping blood":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q2' not in st.session_state:
                st.error("Question 2 Has Not Been Answered")
            elif st.session_state.q2=="B) Diseases like measles and flu":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q3' not in st.session_state:
                st.error("Question 3 Has Not Been Answered")
            elif st.session_state.q3=="B) To prevent getting sick":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q4' not in st.session_state:
                st.error("Question 4 Has Not Been Answered")
            elif st.session_state.q4=="B) Tell an adult and rest":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q5' not in st.session_state:
                st.error("Question 5 Has Not Been Answered")
            elif st.session_state.q5=="B) Help people stay healthy":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q6' not in st.session_state:
                st.error("Question 6 Has Not Been Answered")
            elif st.session_state.q6=="B) Fruits and vegetables":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q7' not in st.session_state:
                st.error("Question 7 Has Not Been Answered")
            elif st.session_state.q7=="B) Your body reacts badly to it":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q8' not in st.session_state:
                st.error("Question 8 Has Not Been Answered")
            elif st.session_state.q8=="B) Wash it and put a bandage on it":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q9' not in st.session_state:
                st.error("Question 9 Has Not Been Answered")
            elif st.session_state.q9=="B) It gives you energy for school":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q10' not in st.session_state:
                st.error("Question 10 Has Not Been Answered")
            elif st.session_state.q10=="B) Drinking milk or eating dairy":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q11' not in st.session_state:
                st.error("Question 11 Has Not Been Answered")
            elif st.session_state.q11=="B) To give immediate care in emergencies":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)   
            if 'q12' not in st.session_state:
                st.error("Question 12 Has Not Been Answered")
            elif st.session_state.q12=="B) Drinking warm fluids":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)   
            if 'q13' not in st.session_state:
                st.error("Question 13 Has Not Been Answered")
            elif st.session_state.q13=="A) Runny nose":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False) 
            if 'q14' not in st.session_state:
                st.error("Question 14 Has Not Been Answered")
            elif st.session_state.q14=="B) To prevent spreading germs":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False) 
            if 'q15' not in st.session_state:
                st.error("Question 15 Has Not Been Answered")
            elif st.session_state.q15=="B) Playing sports or riding a bike":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q16' not in st.session_state:
                st.error("Question 16 Has Not Been Answered")
            elif st.session_state.q16=="B) Your teeth":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q17' not in st.session_state:
                st.error("Question 17 Has Not Been Answered")
            elif st.session_state.q17=="B) Sit down and tell an adult":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q18' not in st.session_state:
                st.error("Question 18 Has Not Been Answered")
            elif st.session_state.q18=="B) To help you breathe":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q19' not in st.session_state:
                st.error("Question 19 Has Not Been Answered")
            elif st.session_state.q19=="A) Washing hands frequently":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
            if 'q20' not in st.session_state:
                st.error("Question 20 as Not Been Answered")
            elif st.session_state.q20=="B) They might need rest or water":
                score.loc[0, st.session_state.name]+=1
                score.to_csv(link, index=False)
                
            st.session_state.currentpage='summary'


            
                
            

        if st.button("Previous Question"):
            st.session_state.currentpage='qf19'
            st.rerun()



    def summary():
        st.success("You Have Finished Your Quiz")
        
        if st.button("Back to Home"):
            st.session_state.currentpage='homepage'
            st.rerun()




        

    if st.session_state.currentpage == 'homepage':
        home()    

    elif st.session_state.currentpage =='qf1':
        qf1()
    elif st.session_state.currentpage =='qf2':
        qf2()
    elif st.session_state.currentpage =='qf3':
        qf3()
    elif st.session_state.currentpage =='qf4':
        qf4()
    elif st.session_state.currentpage =='qf5':
        qf5()
    elif st.session_state.currentpage =='qf6':
        qf6()
    elif st.session_state.currentpage =='qf7':
        qf7()
    elif st.session_state.currentpage =='qf8':
        qf8()
    elif st.session_state.currentpage =='qf9':
        qf9()
    elif st.session_state.currentpage =='qf10':
        qf10()
    elif st.session_state.currentpage =='qf11':
        qf11()
    elif st.session_state.currentpage =='qf12':
        qf12()
    elif st.session_state.currentpage =='qf13':
        qf13()
    elif st.session_state.currentpage =='qf14':
        qf14()
    elif st.session_state.currentpage =='qf15':
        qf15()
    elif st.session_state.currentpage =='qf16':
        qf16()
    elif st.session_state.currentpage =='qf17':
        qf17()
    elif st.session_state.currentpage =='qf17':
        qf17()
    elif st.session_state.currentpage =='qf18':
        qf18()
    elif st.session_state.currentpage =='qf19':
        qf19()
    elif st.session_state.currentpage =='qf20':
        qf20()
    elif st.session_state.currentpage =='summary':
        summary()

if menu=="View Results":
    # st.write(st.session_state.date)

    melt=score.melt(var_name="Name", value_name="Score")
    melt["Percentage"]=((melt["Score"]/20.0)*100)
    with st.expander("View Quiz Table"):
        st.table(melt)
    

    chart=st.radio("Choose A Chart",["Bar","Pie"])

    pie=px.pie(melt, names='Name', values='Score')
    bar=px.bar(melt, x='Name', y='Score')

    if chart=="Bar":
        st.plotly_chart(bar)
    if chart=="Pie":    
        st.plotly_chart(pie)
    

    if st.sidebar.toggle("View Certificate"):
            st.sidebar.write("---")
            search=st.sidebar.text_input("Input Name")
            st.sidebar.text_input("[Optional: Enter Email Adress]")
            find=st.sidebar.button("Find User")
            if find:
                if search:
                    
                    search_result=melt[melt['Name'].str.lower()==search.lower()]
                    st.session_state.user = str(search_result['Name'].iloc[0]).capitalize()
                    st.session_state.score = str(search_result['Percentage'].iloc[0]).capitalize()
                    # st.write(st.session_state.user)
                    # st.write(search_result)
                    # st.write(st.session_state.score)

                    pdf_func = generate_pdf()


    
                    with open(pdf_func, 'rb') as binary:
                        pdf_data = binary.read()

                    col1,col2,col3,=st.columns(3)

                    with col2:
                        st.download_button(label=':blue[**Download File**]',data=pdf_data, file_name=f"{st.session_state.user}'s Certificate.pdf",mime='application/pdf')

                    
                    s1,s2,s3=st.columns([0.8,2,1.2])
                    with s2:
                        st.success(f"User {st.session_state.user}'s certificate was generated.")

                    
                        # if st.button(":blue[**View Certificate**]"):
                        #     pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

                        #     pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'


                        #     st.markdown(pdf_embed,unsafe_allow_html=True)