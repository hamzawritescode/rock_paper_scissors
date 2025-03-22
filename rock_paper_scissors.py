
    # ------------------------------------------------ Rock, Paper, Scissors Game ----------------------------------------------------------- #

    # --- Note: If you see things more than required in the code, it's because I'm trying to make the code more interactive and user-friendly, + I am experienced  --- #


    # -------------------------------------------------------- Importing Modules & Welcome Message ------------------------------------------ #

import random # Importing random module to generate random numbers for computer's choice
print(f"Welcome to Rock, Paper, Scissors Game!") # Welcome message

    # -------------------------------------------------------- Variables -------------------------------------------------------------------- #

player = int(input(f"Enter your choice: 1 for Rock ✊, 2 for Paper ✋, 3 for Scissors ✌️: ")) # player variable to store player's choice
computer = int(random.randint(1, 3)) # Computer Variable to store computer's choice using random.randint() function


    # -------------------------------------------------------- Deciding the winner ------------------------------------------------------------------ #

    # -------------------------------------------------------- Player Wins ------------------------------------------------------------------------ #

if player == 1 and computer == 3:
    print(f"Player Wins! Rock ✊ beats Scissors✌️!")

elif player == 2 and computer == 1:
    print(f"Player Wins! Paper✋ beats Rock ✊!")

elif player == 3 and computer == 2:
    print(f"Player Wins! Scissors✌️ beats Paper✋!")

# -------------------------------------------------------- Computer Wins ---------------------------------------------------------------------- #

elif player == 1 and computer == 2:
    print(f"Computer Wins! Paper✋ beats Rock ✊!")

elif player == 2 and computer == 3:
    print(f"Computer Wins! Scissors✌️ beats Paper✋!")

elif player == 3 and computer == 1:
    print(f"Computer Wins! Rock ✊ beats Scissors✌️!")

# -------------------------------------------------------- Tie ------------------------------------------------------------------------------- #

elif player == computer:
    print(f"It's a Tie!")

# -------------------------------------------------------- Invalid Input For Player ---------------------------------------------------------------------- #

else:
    print(f"Invalid Input! Please try again!") # If player enters invalid input

# -------------------------------------------------------- End of Rock, Paper, Scissors Game ----------------------------------------------------------- #