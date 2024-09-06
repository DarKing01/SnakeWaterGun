# Snake, Water, Gun Game
import random

'''
0 Snake
1 Water
-1 Gun
'''

computer = random.choice([0, 1, -1])

youStr = input("Enter your choice: ")
youDict = {"s":0, "w":1, "g":-1}
reverseDict = {0:"Snake", 1:"Water", -1:"Gun"}

you = youDict[youStr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw!")
else:
    if(computer == 0 and you == 1):
        print("You Lose!")    
    elif(computer == 0 and you == -1):
        print("You Win!")    
    elif(computer == 1 and you == 0):
        print("You Win!")    
    elif(computer == 1 and you == -1):
        print("You Lose!")    
    elif(computer == -1 and you == 0):
        print("You Lose!")    
    elif(computer == -1 and you == 1):
        print("You Win!")  
    else:
        print("Something went wrong")  
