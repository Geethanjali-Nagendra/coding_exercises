import random 

"""Provided a list of lottery players, and also with 6 random lottery numbers.
Find out the player with the most correct numbers, and print out their winnings and their name
Task is to find who matched the most numbers, and print out a string with their name and the amount they won. For this exercise, 
assume there will only be 1 winner. 
For example: Jen won 1000. 
The winnings are calculated with this formula:
winnings = 100 ** len(numbers_matched) """

lottery_numbers = set(random.sample(range(21), 6)) # generate 6 random numbers from 0 to 20
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]
max_correct = 0
best_player = None
for player in players:
    matched_numbers = player["numbers"].intersection(lottery_numbers)
    num_of_correct_matches = len(matched_numbers)

    if num_of_correct_matches > max_correct:
        max_correct = num_of_correct_matches
        best_player = player
winnings = 100 ** max_correct
print(f"{best_player['name']} won {winnings}.")
