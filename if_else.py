#If else is a conditional statement that python use to make decisions

#conditions MUST end with a colon :
# decisions MUST be indented under the condition
#indentation is the space/tab before the decision (very important)
#indentation tells python NOT to read the line of code unless the above condition is TRUE

print('hello')

name = input("Please enter your name: ")

maths = int(input('Enter Maths score: '))

if (maths > 50): #condition, remember to end with a colon
    print("You passed the test") #decision MUST be indented
    print("COngratulations") #decision MUST be indented

else: #condition, remember to end with a colon
    print("You failed the test") #decision MUST be indented
    print("Sorry try again later") #decision MUST be indented

