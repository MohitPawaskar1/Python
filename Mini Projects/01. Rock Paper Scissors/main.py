'''
    1 for Rock
    
    2 for Paper

    3 for Scissors
'''

import random

computer = random.choice([1, 2, 3])

user = int(input("Enter your choice: "))

dic = {1:"Rock", 2:"Paper", 3:"Scissors"}

print(f"You chose {dic[user]} & Computer chose {dic[computer]}")
if (user == computer):
    print("It's a TIE...")

else:
    if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        print("User Wins!")
    else:
        print("Computer Wins!")