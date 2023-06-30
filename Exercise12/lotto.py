# import random to pick random numbers
import random

# create a blank list to store numbers
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
    # If  number has already appeared do nothing and run while command again
    else:
        pass

# Follows same principle as above to draw a bonus ball and add to blank bonus ball list
# useful for if we even want more than one bonus ball later
bonus_list = []
bonus_ball = random.randint(1, 9)
bonus_list.append(bonus_ball)

# Sort balls in ascending order
lotto_numbers_asc = sorted(lotto_numbers)
# add bonus ball to give complete list of numbers
complete_balls = lotto_numbers_asc + bonus_list

print("Tonight's lucky numbers in ascending order are: ")
print(lotto_numbers_asc)
print("...and the bonus is: ")
print(bonus_ball)

# fun formatting stuff - brackets for balls and sep='' to remove spaces from concatenation
print(
    "(", complete_balls[0], ")""(", complete_balls[1], ")""(", complete_balls[2], ")""(", complete_balls[3], ")""(",
    complete_balls[4], ")"" | (", complete_balls[5], ")", sep='')


# fun formatting stuff - using dictionary and unicode to show numbers in balls
# ball_dictionary = {
#     1: "\u2460",
#     2: "\u2461",
#     3: "\u2462",
#     4: "\u2463",
#     5: "\u2464",
#     6: "\u2465",
#     7: "\u2466",
#     8: "\u2467",
#     9: "\u2468",
#     10: "\u2469",
#     11: "\u246A",
#     12: "\u246B",
#     13: "\u246C",
#     14: "\u246D",
#     15: "\u246E",
#     16: "\u246F",
#     17: "\u2470",
#     18: "\u2471",
#     19: "\u2472",
#     20: "\u2473",
#     21: "\u3251",
#     22: "\u3252",
#     23: "\u3253",
#     24: "\u3254",
#     25: "\u3255",
#     26: "\u3256",
#     27: "\u3257",
#     28: "\u3258",
#     29: "\u3259",
#     30: "\u325A",
#     31: "\u325B",
#     32: "\u325C",
#     33: "\u325D",
#     34: "\u325E",
#     35: "\u325F",
#     36: "\u32B1",
#     37: "\u32B2",
#     38: "\u32B3",
#     39: "\u32B4",
#     40: "\u32B5",
#     41: "\u32B6",
#     42: "\u32B7",
#     43: "\u32B8",
#     44: "\u32B9",
#     45: "\u32BA",
#     46: "\u32BB",
#     47: "\u32BC",
#     48: "\u32BD",
#     49: "\u32BE",
#     50: "\u32BF",
# }
# bonus_dictionary = {
#     1: "\u278A",
#     2: "\u278B",
#     3: "\u278C",
#     4: "\u278D",
#     5: "\u278E",
#     6: "\u278F",
#     7: "\u2790",
#     8: "\u2791",
#     9: "\u2792",
#     10: "\u2793",
# }
#
# print(
#     ball_dictionary[complete_balls[0]], ball_dictionary[complete_balls[1]], ball_dictionary[complete_balls[2]],
#     ball_dictionary[complete_balls[3]], ball_dictionary[complete_balls[4]], bonus_dictionary[complete_balls[5]])

