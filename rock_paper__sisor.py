import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK =1
    PAPER =2
    SCISSORS =3
    
def play_rps():
    playerchoice=input("\nEnter...\n1 for Rock,\n2 for Paper\n3 for Scissors:\n\n")
    
    if playerchoice not in ["1","2","3"]:
        print("You must enter 1,2,3 ")
        return play_rps()
    
    player =int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\n You choice "+str(RPS(player)).replace('RPS.','').title() + ".")
    print("Python choice "+str(RPS(computer)).replace('RPS.','').title()+".\n")

    if player ==1 and computer ==3:
        print("You Win!")
    elif player ==2 and computer ==1:
        print("You Win!")
    elif player ==3 and computer ==2:
        print("You Win!")
    elif player == computer:
        print("TIE GAME")                
    else:
        print("Python Wins!")
        
    playagain = input("\nPlay again? \nY for Yes or\nQ for Quit\n\n ")

    if playagain.lower()=="y":
        return play_rps()
    else:
        print("\n")
        print("Thank you for Playing\n")
        sys.exit("Bye!")
        
play_rps()
             

