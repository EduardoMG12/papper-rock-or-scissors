import random

print("Hey guy, do you go play paper, rock or scissors?")
keyPress = '';
while keyPress != 1:
    keyPress = int(input("press 0 stop or press 1 continue: "))
    if keyPress == 0:
         exit();

computerChange = random.randint(1,3)
if computerChange == 1:
    computerChangeValue = "rock";
elif computerChange == 2:
    computerChangeValue = "paper";
elif computerChange == 3:
    computerChangeValue = "scissors";

playerChange = int(0);    
while (playerChange < 1) or (playerChange > 3):
    print("[1] rock\n[2] paper\n[3] scissors")
    playerChange = int(input("Change paper, rocks, or scissors: "))
if playerChange == 1:
    playerChangeValue = "rock";
elif playerChange == 2:
    playerChangeValue = "paper";
elif playerChange == 3:
    playerChangeValue = "scissors";

if computerChange == playerChange:
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");
elif (playerChange == 1) and (computerChange == 2):
    print(f"\033[32;5;208mYou wins");
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");
elif (playerChange == 1) and (computerChange == 3):
    print(f"\033[32;5;208mComputer wins");
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");
elif (playerChange == 2) and (computerChange == 1):
    print(f"\033[32;5;208mYou wins");
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");
elif (playerChange == 2) and (computerChange == 3):
    print(f"\033[32;5;208mComputer wins");
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");
elif (playerChange == 3) and (computerChange == 2):
    print(f"\033[32;5;208mYou wins");
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");
elif (playerChange == 3) and (computerChange == 1):
    print(f"\033[32;5;208mComputer wins");
    print(f"The computer change is {computerChangeValue} and the player change is {playerChangeValue}");