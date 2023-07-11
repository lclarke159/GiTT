import random


def player():
    user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()
    # if user_choice != "R" or "P" or "S":
    #     return "ERROR!!"
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
        print(f"Computer chose", selection_dictionary[computer()], "tie")
        return "D"
    elif player() == "R" and computer() == "S":
        print("Rock crushes scissors - you win!!")
        return "W"
    elif player() == "P" and computer() == "R":
        print("Paper covers rock - you win!!")
        return "W"
    elif player() == "S" and computer() == "P":
        print("Scissors cut paper - you win!!")
        return "W"
    elif player() == "R" and computer() == "P":
        print("Paper covers rock - you lose!!")
        return "L"
    elif player() == "P" and computer() == "S":
        print("Scissors cut paper - you lose!!")
        return "L"
    elif player() == "S" and computer() == "R":
        print("Rock crushes scissors - you lose!!")
        return "L"






computer_score = 0
player_score = 0

while True:
    result = (play(player(), computer()))
    print(result)
    if result == "W":
        player_score += 1
        print("The score is", computer_score, "-", player_score)
    if result == "L":
        computer_score += 1
        print("The score is", computer_score, "-", player_score)
    if result == "D":
        print("The score is", computer_score, "-", player_score)
