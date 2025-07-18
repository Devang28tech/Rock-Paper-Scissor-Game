import random

computer=random.choice([-1,0,1])

youstr=input("Enter your choice: ")

youDict = {"r": -1, "p": 0, "s": 1}

reverseDict = {-1:"Rock", 0:"Paper", 1:"Scissors"}

you= youDict[youstr]

print(f"you chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if(you == computer):
    print("It's a tie!")

else:
    if(you == -1 and computer == 1):
        print("You win!")
    elif(you==-1 and computer== 0):
        print("Computer wins!")
    elif(you == 0 and computer ==-1):
        print("You win!")
    elif(you == 0 and computer == 1):
        print("Computer wins!")
    elif(you == 1 and computer == -1):
        print("Computer wins!")         
    elif(you == 1 and computer == 0):
        print("You win!")   
    else:
        print("Invalid input, please try again.")                    

             