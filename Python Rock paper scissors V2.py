import time
import random

List_outcomes = ["Rock" , "Paper" , "Scissors"]
# Preferals



AI_Outcome = random.choice(List_outcomes)
User_input =input("'Rock' , 'Paper' or 'Scissors' ?\n""\ntype 'quit' to quit the program: ").capitalize()
time.sleep(1)
while User_input not in ("Rock" , "Paper" , "Scissors","Quit"):
    User_input =input("'Rock' , 'Paper' or 'Scissors' ?\n""\ntype 'quit' to quit the program: ").capitalize()


if AI_Outcome == User_input:
    print("It is a draw")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
elif AI_Outcome == "Rock" and User_input == "Paper":
    print("You Won! ")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
elif AI_Outcome == "Paper" and User_input == "Scissors":
    print("You Won! ")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
elif AI_Outcome == "Scissors" and User_input == "Rock":
    print("You Won! ")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
elif User_input == "Rock" and AI_Outcome == "Paper":
    print("You Lost ! ")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
elif User_input == "Paper" and AI_Outcome == "Scissors":
    print("You Lost ! ")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
elif User_input == "Scissors" and AI_Outcome == "Rock":
    print("You Lost ! ")
    print("AI chose " + str(AI_Outcome))
    print("You chose " + str(User_input))
    
elif User_input == "Quit":
    print('thanls for playing :) ')
    exit
else:
    pass

    print("Type Only 'Rock','Paper' or 'Scissors' ")

