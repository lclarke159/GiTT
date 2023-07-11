import random
#  Uses function for player selection, computer selection and to play the game.
#  Includes scoreboard for keeping track of scores

# TODO Invalid selection gives message "None" instead of "Make a valid selection!!"

def player():
    user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()
    if user_choice not in ["R", "P", "S"]:
        return "Make a valid selection!!"
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
    loses_to = {
        "R": "S",
        "P": "R",
        "S": "P",
    }
    if player_choice == comp_choice:
        print(f"Computer chose {selection_dictionary[computer()]}, it's a tie!")
        return "Have another go!!"
    elif player_choice == "R" and comp_choice == "S":
        print("Rock crushes scissors - you win!!")
        return "Well done!!"
    elif player_choice == "P" and comp_choice == "R":
        print("Paper covers rock - you win!!")
        return "Well done!!"
    elif player_choice == "S" and comp_choice == "P":
        print("Scissors cut paper - you win!!")
        return "Well done!!"
    elif player_choice == "R" and comp_choice == "P":
        print("Paper covers rock - you lose!!")
        return "Unlucky!!"
    elif player_choice == "P" and comp_choice == "S":
        print("Scissors cut paper - you lose!!")
        return "Unlucky!!"
    elif player_choice == "S" and comp_choice == "R":
        print("Rock crushes scissors - you lose!!")
        return "Unlucky!!"


computer_score = 0
player_score = 0

while True:
    result = play(player(), computer())
    print(result)
    if result == "Well done!!":
        player_score += 1
    elif result == "Unlucky!!":
        computer_score += 1
    print("The score is", computer_score, "-", player_score)
