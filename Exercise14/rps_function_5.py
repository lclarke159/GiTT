import random


#  Uses function for player selection, computer selection and to play the game.
#  Includes scoreboard for keeping track of scores
# includes ascii dict to make more user-friendly / engaging

def player():
    user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()
    if user_choice not in ["R", "P", "S"]:
        return "Make a valid selection2!!"
    else:
        return user_choice


def computer():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        return "R"
    elif computer_choice == 1:
        return "P"
    elif computer_choice == 2:
        return "S"


def play(player_choice, comp_choice):
    selection_dictionary = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    ascii_dict = {
        "R": """ ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        "P": """ PAPER!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
        "S": """ SCISSORS!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    }

    loses_to = {
        "R": "S",
        "P": "R",
        "S": "P",
    }
    if player_choice == comp_choice:
        print(f"Computer chose... {ascii_dict[comp_choice]} it's a tie!")
        return "Have another go!!"
    elif player_choice == "R" and comp_choice == "S":
        print(f"Computer chose... {ascii_dict[comp_choice]} Rock crushes scissors - you win!!")
        return "Well done!!"
    elif player_choice == "P" and comp_choice == "R":
        print(f"Computer chose... {ascii_dict[comp_choice]} Paper covers rock - you win!!")
        return "Well done!!"
    elif player_choice == "S" and comp_choice == "P":
        print(f"Computer chose... {ascii_dict[comp_choice]} Scissors cut paper - you win!!")
        return "Well done!!"
    elif player_choice == "R" and comp_choice == "P":
        print(f"Computer chose... {ascii_dict[comp_choice]} Paper covers rock - you lose!!")
        return "Unlucky!!"
    elif player_choice == "P" and comp_choice == "S":
        print(f"Computer chose... {ascii_dict[comp_choice]} Scissors cut paper - you lose!!")
        return "Unlucky!!"
    elif player_choice == "S" and comp_choice == "R":
        print(f"Computer chose... {ascii_dict[comp_choice]} Rock crushes scissors - you lose!!")
        return "Unlucky!!"
    else:                                                    # Required or no selection results in 'none' being printed
        return "Please make a valid selection!!"



computer_score = 0
player_score = 0

while True:
    result = play(player(), computer())
    print(result)
    if result == "Well done!!":
        player_score += 1
    elif result == "Unlucky!!":
        computer_score += 1
    # else:
    #     print("Make a valid selection4!!")
    print("The score is", computer_score, "-", player_score)


