# Two functions - one to play the game one to loop it

# imports random to use later
import random


def play_game():
    # Dictionary for storing choices
    rps_dict = {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
        9: "an invalid selection"
    }
    # Gets user choice and converts it to uppercase
    user_choice = input("Choose (R)ock, (P)aper or (S)cissors and press Enter: ").upper()
    if user_choice == "R":
        user_choice = int(0)
    elif user_choice == "P":
        user_choice = int(1)
    elif user_choice == "S":
        user_choice = int(2)
    else:
        user_choice = int(9)

    # Computer selection
    computer_choice = random.randint(0, 2)

    # Feedback to player
    print("You chose", rps_dict[user_choice], "Computer picked", rps_dict[computer_choice])
    # Decide winner

    if user_choice == computer_choice:
        print("It's a tie!")
        return "D"
    elif user_choice == 0 and computer_choice == 1:
        print("Paper covers rock - you lose!!")
        return "L"
    elif user_choice == 0 and computer_choice == 2:
        print("Rock crushes scissors - you win!!")
        return "W"
    elif user_choice == 1 and computer_choice == 0:
        print("Paper covers rock - you win!!")
        return "W"
    elif user_choice == 1 and computer_choice == 2:
        print("Scissors cut paper - you lose!!")
        return "L"
    elif user_choice == 2 and computer_choice == 0:
        print("Rock crushes scissors - you lose!!")
        return "L"
    elif user_choice == 2 and computer_choice == 1:
        print("Scissors cut paper - you win!!")
        return "W"
    return "You must make a valid selection!!"


computer_score = 0
player_score = 0
while True:
    if play_game() == "W":
        player_score += 1
        print("The score is", computer_score, "-", player_score)
    if play_game() == "L":
        computer_score += 1
        print("The score is", computer_score, "-", player_score)
    if play_game() == "D":
        print("The score is", computer_score, "-", player_score)
    print(play_game())


    # if input("Do you want to play again? (Y/N): ").upper() != "Y":
    #     break


