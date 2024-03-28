#IF ELIF ELSE

#recall that if else is used by python to run a code if the "if condition" is True
# or it runs "else" if the "if condition" is False


#elif means Else If
#elif is simply used to add more options/conditions to your code
#elif MUST be after your IF and before your ELSE
#You can have as many as possible elif in your code


name = input("Please enter your name: ")

maths = int(input('Enter Maths score: '))

# 90 above A+
# 80-89 A
# 70-79 B
# 60-69 C
# 50-59 D
#49 below is F

if (maths > 90): #condition, remember to end with a colon
    print("You got an A+")
    print("You passed the test") 
    print("Congratulations") 

elif (maths >=80) and (maths <=89):
    print('You got an A')
    print("You passed the test") 
    print("Congratulations") 
elif (maths >=70) and (maths <=79):
    print('You got a B')
    print("You passed the test") 
    print("Congratulations") 
   
elif (maths >=60) and (maths <=69):
    print('You got a C')
    print("You passed the test") 
    print("Congratulations")

elif (maths >=50) and (maths <=59):
    print('You got a D')
    print("You passed the test") 
    print("You can do better though")

else: #condition, remember to end with a colon
    print('You got an F')
    print("You failed the test") 
    print("Sorry try again later") 

age=int(input("What is your age: "))
if(age > 18):
    print("Go to the adult class")
else:
    print("Go to the child class")

print("An Icecream costs 25")
icecreamnumb=int(input("How many Icecreams do you want: "))
cost=icecreamnumb*25
if (icecreamnumb>5):
    print("Thank you for buying lots of icecream")
    cost=cost-10
    print("The cost is:",cost)
else:
    print('Thank you for buying')
print("The total is",cost)


#HOMEWORK 1:
#Ask a user to enter his age
#Use your python program to check and display if user is older than 18. if older than 18 please display "Please go to the adult class" else display "You should be in the children's class"

#HOMEWORK 2:

#"""
#An icecream man sells an icecream for 25$. Create a program in Python to ask how many icecreams people want to get and then tell them the total
#  price. If anyone buys more than 5 icecreams deduct 10 $ from their total price and also tell them Thank you for buying many icecreams
#"""
