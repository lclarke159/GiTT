import random


def player():
    user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()
    if user_choice != ("R" or "P" or "S"):
        return "ERROR!!"
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
    if comp_choice == loses_to[player_choice]:
        print("Computer chose", comp_choice, "You win")
        return "W"
    if player_choice == loses_to[comp_choice]:
        print(f"Computer chose", comp_choice, "You lose")
        return "L"
    if player_choice == comp_choice:
        print("tie")
        return "D"


loses_to = {
    "R": "S",
    "P": "R",
    "S": "P",
}
computer_score = 0
player_score = 0

while True:
    result = (play(player(), computer()))
    if result == "W":
        player_score += 1
        print("The score is", computer_score, "-", player_score)
    if result == "L":
        computer_score += 1
        print("The score is", computer_score, "-", player_score)
    if result == "D":
        print("The score is", computer_score, "-", player_score)
