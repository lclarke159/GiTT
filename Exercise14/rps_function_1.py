import random

# TODO Handle a non valid user selection (currently returns error on the next turn when making valid selection)

#  Different functions for player choice, computer choice and to play the game using a dictionary for losses

# Sets a dictionary for what item loses to what
# Allows for expansion without adding too much more code
loses_to = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


# Gets user choice, converts it to uppercase and returns it as user()
def player():
    user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()
    if user_choice == "R":
        return "rock"
    elif user_choice == "P":
        return "paper"
    elif user_choice == "S":
        return "scissors"
    else:
        print("You must make a valid selection!!")


# Gets Random computer selection and returns it as computer()
def computer():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        return "rock"
    elif computer_choice == 1:
        return "paper"
    elif computer_choice == 2:
        return "scissors"


def play(player_choice, comp_choice):
    # if player() == "ERROR!!":
    #     print("You must make a valid section")
    if comp_choice == loses_to[player_choice]:
        # return "Computer chose", comp_choice, "You win"
        print("Computer chose", comp_choice, "...you win")
        return "Well done!!"
    elif player_choice == loses_to[comp_choice]:
        # return f"Computer chose", comp_choice, "Computer wins"
        print("Computer chose", comp_choice, "...computer wins")
        return "Unlucky!!"
    elif player_choice == comp_choice:
        # return "tie"
        print("Computer chose", comp_choice, "...its a tie")
        return "Have another go!!"


# Continuous play
while True:
    print(play(player(), computer()))
