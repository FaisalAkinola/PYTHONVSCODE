"""
create a python program to ask the daily sales of a store which as the following departments (food, clothings, equipments, bags and books). Then get the total sales 
"""
print("please enter your sales year: ")
food=int(input('how much food did you sell: '))
clothing=int(input('how many clothes did you sell: '))
equipment=int(input('how much epuipment did you sell: '))
bags=int(input('how many bags did you sell: '))
books=int(input('how many books did you sell: '))
total=(food+clothing+equipment+bags+books)
print("total sales is",total)