import random


def main_balls():
    lotto_numbers = []
    # set ball count at 0 and generate random numbers until 5 numbers have been generated
    ball_count = 0
    while ball_count < 5:
        new_ball = random.randint(1, 50)
        # Make sure the number does not already appear in the list (unique numbers only)
        if new_ball not in lotto_numbers:
            # adds new ball to list of lotto_numbers
            lotto_numbers.append(new_ball)
            # adds 1 to ball_count
            ball_count += 1
        else:
            pass
    return lotto_numbers
    # If  number has already appeared do nothing and run while command again


def bonus_balls():
    bonus_list = []
    bonus_ball = random.randint(1, 9)
    bonus_list.append(bonus_ball)
    return bonus_list


print(main_balls(), bonus_balls())
