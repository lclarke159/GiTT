# SINGLE game of Rock Paper Scissors where each user choice has its own function
# TODO make game play continuously (While True currently go to infinite loop)


import random

# Dictionary for storing choices
rps_dict = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
    9: "an invalid selection"
}

# Gets user choice and converts it to uppercase
user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()

# Computer selection
computer_choice = random.randint(0, 2)


def rock():
    if computer_choice == 0:
        print("Tie!")
    elif computer_choice == 1:
        print("You Lose - paper covers rock!!")
    elif computer_choice == 2:
        print("You win - rock smashes scissors!!")


def paper():
    if computer_choice == 1:
        print("Tie!")
    elif computer_choice == 2:
        print("You Lose - scissors cut paper!")
    elif computer_choice == 0:
        print("You win - paper covers rock!!")


def scissors():
    if computer_choice == 2:
        print("Tie!")
    elif computer_choice == 1:
        print("You Win - scissors cut paper!")
    elif computer_choice == 0:
        print("You lose - rock smashes scissors!!")


if user_choice == "R":
    rock()
elif user_choice == "P":
    paper()
elif user_choice == "S":
    scissors()
else:
    print("You must make a valid selection!!")
