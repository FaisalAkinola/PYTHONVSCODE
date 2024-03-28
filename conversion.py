#Converting data from one type to another

# types of data

# 1. integer == whole numbers
# 2. string == Anything in quotes
# 3. float == decimal
# 4.boolean == True or False

# Method 1:
score = int('60')#convert the original data before storing in the variable

# Method 2:
score = '60' #keep original state of data
score2 = int(score) #create a new variable to save a diff data type
print(score) #str
print(score2) #int

#int, float, str, bool

#please note, the default data type for input is a STRING

# classwork:


# convert these to float or integer or string using a new variable
#print and all must run and display well

score = 75.9
score2=float(score)
print("Your score was", score2)

age = 12
age2=str(age)
print("You are",age,"years old")

height = 9.7
height2=float(height)
print("You are",height2,'tall')

weight = "75.9"
weight2=float(weight)
print("you weigh", weight2)

reject = False
reject2=str(reject)
print("it is", reject2)
# convert these to float or integer or string without using a variable

age = int(27.8)

allow = True
allow=bool(True)

reject = False
reject=bool(False)

weight = 170.989687967567
weight=str(170.989687)
date = 2023.8

average = 75


#Ask the user to enter any 3 digit number and mulitply it by 2

#Ask the user to enter a word and then convert it to a boolean
digit=input("Enter a Digit and the program will multiply it by 2")
digit2=int(digit)

