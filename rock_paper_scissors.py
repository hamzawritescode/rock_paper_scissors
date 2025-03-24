
    # ------------------------------------------------ Rock, Paper, Scissors Game ----------------------------------------------------------- #


import random # Importing random module to generate random numbers for computer's choiceimport random
status = True # initalize status variable to keep the game running
print(f"Welcome to Rock, Paper, Scissors Game!")

while status:
    while player := input(f"Enter your choice: 1 for Rock ✊, 2 for Paper ✋, 3 for Scissors ✌️: "):
        if player != "1" and player != "2" and player != "3":
            print("Invalid Input! Please try again!")
        else:
            player = int(player)
            break

    computer = int(random.randint(1, 3)) # Computer Variable to store computer's choice using random.randint() function

    if player == 1 and computer == 3:
        print(f"Player Wins! Rock ✊ beats Scissors✌️!")
    elif player == 2 and computer == 1:
        print(f"Player Wins! Paper ✋ beats Rock ✊!")
    elif player == 3 and computer == 2:
        print(f"Player Wins! Scissors ✌️  beats Paper✋!")
    elif player == 1 and computer == 2:
        print(f"Computer Wins! Paper ✋ beats Rock ✊!")
    elif player == 2 and computer == 3:
        print(f"Computer Wins! Scissors ✌️ beats Paper✋!")
    elif player == 3 and computer == 1:
        print(f"Computer Wins! Rock ✊ beats Scissors✌️!")
    elif player == computer:
        print(f"It's a tie!")
    else:
        print(f"Invalid Input! Please try again!")
    
    while status_response := input("Do you want to play again? (yes/no): ").lower():
        if status_response == "yes":
            break
        elif status_response == "no":
            status = False
            break
        else:
            print("Invalid Input! Please try again!")
