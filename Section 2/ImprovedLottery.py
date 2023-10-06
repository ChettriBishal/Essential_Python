import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player = players[0]

for player in players:
    matched_number = len(player["numbers"].intersection(lottery_numbers))
    if matched_number > len(top_player["numbers"].intersection(lottery_numbers)):
        top_player = player 

winnings = 100 ** len(top_player['numbers'].intersection(lottery_numbers))
print(f"{top_player['name']} won {winnings}")


'''
For this exercise we've provided you with a list of lottery players, and also with 6 random lottery numbers.

Find out the player with the most correct numbers, and print out their winnings and their name

Your task is to find who matched the most numbers, and print out a string with their name and the amount they won.
For this exercise, assume there will only be 1 winner. 
Don't worry about two players matching the same amount of numbers.

For example:

Jen won 1000. 

The winnings are calculated with this formula:

winnings = 100 ** len(numbers_matched) 

'''