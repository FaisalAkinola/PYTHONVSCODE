import streamlit as st 
import pandas as pd 


link="medicalquiz.csv"
try:
    score=pd.read_csv(link)
except:
    score=pd.DataFrame()                       


def home():
    global currentpage
    st.title("Quiz")
    name=st.text_input("Enter Name")
    
    
    if st.pills("",["Begin"]):
        if name:
            link.loc[0,name]=0
            currentpage='qf1'
        else:
            st.error("Must Enter A Name to Start")



def qf1():
    st.subheader('Question 1')
    st.write('')
    '---'
    q1=st.selectbox('What is the main job of your heart?',["Choose","A) Pumping blood","B) Digesting food","C) Storing energy","D) Breathing air"])
    if st.button("Next Question"):
        if q1=="Choose":
            st.error("Enter an answer")
        elif q1=="A) Pumping blood":
            # link.loc[0, name]+=1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf2():
    st.subheader('Question 2')
    st.write('')
    '---'
    q2=st.selectbox('What do vaccines help protect you from?',["Choose","A) Common cold","B) Diseases like measles and flu","C) Cuts and bruises","D) None of the above"])
    if st.button("Next Question"):
        if q2=="Choose":
            st.error("Enter an answer")
        elif q2=="B) Diseases like measles and flu":
            # link.loc[0, name]+=1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf3():
    st.subheader('Question 3')
    st.write('')
    '---'
    q3=st.selectbox('Why is it important to wash your hands?',["Choose","A) To smell nice","B) To prevent getting sick","C) To look clean","D) None of the above"])
    if st.button("Next Question"):
        if q3=="Choose":
            st.error("Enter an answer")
        elif q3=="B) To prevent getting sick":
            # link.loc[0, name]+=1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf4():
    st.subheader('Question 4')
    st.write('')
    '---'
    q4=st.selectbox('What should you do if you have a fever?',["Choose","A) Go play outside","B) Tell an adult and rest","C) Eat a lot of candy","D) Stay up late"])
    if st.button("Next Question"):
        if q4=="Choose":
            st.error("Enter an answer")
        elif q4=="B) Tell an adult and rest":
            # link.loc[0, name]+=1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf5():
    st.subheader('Question 5')
    st.write('')
    '---'
    q5=st.selectbox('What does a doctor do?',["Choose","A) Fix cars","B) Help people stay healthy","C) Teach math","D) None of the above"])
    if st.button("Next Question"):
        if q5=="Choose":
            st.error("Enter an answer")
        elif q5=="B) Help people stay healthy":
            # link.loc[0, name]+=1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf6():
    st.subheader('Question 6')
    st.write('')
    '---'
    q6=st.selectbox('What is a healthy snack?',["Choose","A) Candy","B) Fruits and vegetables","C) Chips","D) Soda"])
    if st.button("Next Question"):
        if q6=="Choose":
            st.error("Enter an answer")
        elif q6=="B) Fruits and vegetables":
            # link.loc[0, name]+=1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf7():
    st.subheader('Question 7')
    st.write('')
    '---'
    q7 = st.selectbox('What does it mean to be allergic to something?', ["Choose", "A) You like it a lot", "B) Your body reacts badly to it", "C) You can’t eat it", "D) None of the above"])
    if st.button("Next Question"):
        if q7 == "Choose":
            st.error("Enter an answer")
        elif q7 == "B) Your body reacts badly to it":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf8():
    st.subheader('Question 8')
    st.write('')
    '---'
    q8 = st.selectbox('What should you do if you get a cut?', ["Choose", "A) Ignore it", "B) Wash it and put a bandage on it", "C) Show it to your friends", "D) None of the above"])
    if st.button("Next Question"):
        if q8 == "Choose":
            st.error("Enter an answer")
        elif q8 == "B) Wash it and put a bandage on it":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf9():
    st.subheader('Question 9')
    st.write('')
    '---'
    q9 = st.selectbox('Why is it important to eat breakfast?', ["Choose", "A) It’s the best meal of the day", "B) It gives you energy for school", "C) You can skip it", "D) None of the above"])
    if st.button("Next Question"):
        if q9 == "Choose":
            st.error("Enter an answer")
        elif q9 == "B) It gives you energy for school":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf10():
    st.subheader('Question 10')
    st.write('')
    '---'
    q10 = st.selectbox('What is one way to keep your bones strong?', ["Choose", "A) Eating junk food", "B) Drinking milk or eating dairy", "C) Avoiding exercise", "D) None of the above"])
    if st.button("Next Question"):
        if q10 == "Choose":
            st.error("Enter an answer")
        elif q10 == "B) Drinking milk or eating dairy":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf11():
    st.subheader('Question 11')
    st.write('')
    '---'
    q11 = st.selectbox('What is the purpose of first aid?', ["Choose", "A) To help with homework", "B) To give immediate care in emergencies", "C) To make food", "D) None of the above"])
    if st.button("Next Question"):
        if q11 == "Choose":
            st.error("Enter an answer")
        elif q11 == "B) To give immediate care in emergencies":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf12():
    st.subheader('Question 12')
    st.write('')
    '---'
    q12 = st.selectbox('What can help you breathe better when you’re sick?', ["Choose", "A) Eating ice cream", "B) Drinking warm fluids", "C) Running around", "D) None of the above"])
    if st.button("Next Question"):
        if q12 == "Choose":
            st.error("Enter an answer")
        elif q12 == "B) Drinking warm fluids":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf13():
    st.subheader('Question 13')
    st.write('')
    '---'
    q13 = st.selectbox('What is a common symptom of a cold?', ["Choose", "A) Runny nose", "B) Happy thoughts", "C) Dancing", "D) None of the above"])
    if st.button("Next Question"):
        if q13 == "Choose":
            st.error("Enter an answer")
        elif q13 == "A) Runny nose":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf14():
    st.subheader('Question 14')
    st.write('')
    '---'
    q14 = st.selectbox('Why should you cover your mouth when you cough?', ["Choose", "A) To look funny", "B) To prevent spreading germs", "C) To make a sound", "D) None of the above"])
    if st.button("Next Question"):
        if q14 == "Choose":
            st.error("Enter an answer")
        elif q14 == "B) To prevent spreading germs":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf15():
    st.subheader('Question 15')
    st.write('')
    '---'
    q15 = st.selectbox('What is a safe way to exercise?', ["Choose", "A) Jumping on the bed", "B) Playing sports or riding a bike", "C) Sitting all day", "D) None of the above"])
    if st.button("Next Question"):
        if q15 == "Choose":
            st.error("Enter an answer")
        elif q15 == "B) Playing sports or riding a bike":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf16():
    st.subheader('Question 16')
    st.write('')
    '---'
    q16 = st.selectbox('What does a dentist check?', ["Choose", "A) Your eyes", "B) Your teeth", "C) Your hair", "D) None of the above"])
    if st.button("Next Question"):
        if q16 == "Choose":
            st.error("Enter an answer")
        elif q16 == "B) Your teeth":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf17():
    st.subheader('Question 17')
    st.write('')
    '---'
    q17 = st.selectbox('What should you do if you feel dizzy?', ["Choose", "A) Keep running", "B) Sit down and tell an adult", "C) Eat a lot of candy", "D) None of the above"])
    if st.button("Next Question"):
        if q17 == "Choose":
            st.error("Enter an answer")
        elif q17 == "B) Sit down and tell an adult":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf18():
    st.subheader('Question 18')
    st.write('')
    '---'
    q18 = st.selectbox('What is the main function of your lungs?', ["Choose", "A) To pump blood", "B) To help you breathe", "C) To digest food", "D) None of the above"])
    if st.button("Next Question"):
        if q18 == "Choose":
            st.error("Enter an answer")
        elif q18 == "B) To help you breathe":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf19():
    st.subheader('Question 19')
    st.write('')
    '---'
    q19 = st.selectbox('What can help you stay healthy during cold and flu season?', ["Choose", "A) Washing hands frequently", "B) Eating more sweets", "C) Skipping sleep", "D) None of the above"])
    if st.button("Next Question"):
        if q19 == "Choose":
            st.error("Enter an answer")
        elif q19 == "A) Washing hands frequently":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.rerun()
        else:
            pass

def qf20():
    st.subheader('Question 20')
    st.write('')
    '---'
    q20 = st.selectbox('What does it mean if someone has a headache?', ["Choose", "A) They are happy", "B) They might need rest or water", "C) They want to play", "D) None of the above"])
    if st.button("Next Question"):
        if q20 == "Choose":
            st.error("Enter an answer")
        elif q20 == "B) They might need rest or water":
            # link.loc[0, name] += 1
            # link.to_csv("medicalquiz.csv", index=False)
            st.success("Quiz Completed!")
        else:
            st.success("Quiz Completed!")
