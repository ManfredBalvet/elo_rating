from recordNewGame import record_new_game
import json
import random
from collections import OrderedDict
from operator import getitem


with open("elo_rating.json", "r") as file:
    data = json.load(file)

# data = record_new_game(team_A, score_A, score_B, team_B, data)
 
# # Simulate games
# games_to_simulate = 3*20*4
# players = ["Manfred", "David", "Oliver", "Sidney", "Brandon"]
# for game in range(games_to_simulate):
#     random.shuffle(players)
#     team_A = [players[0], players[1]]
#     team_B = [players[2], players[3]]
#     point_gap = random.randint(2, 11)
#     score = [11, 11 - point_gap]
#     random.shuffle(score)
#     score_A = score[0]
#     score_B = score[1]
#     print(f"Game {game + 1}: {team_A[0]} & {team_A[1]} {score_A}:{score_B} {team_B[0]} & {team_B[1]}")


#     data = record_new_game(team_A, score_A, score_B, team_B, data)


data = record_new_game(["Brandon"], 11, 7, ["Sidney"], data)
data = record_new_game(["David", "Oliver"], 11, 8, ["Manfred", "Jordan"], data)
data = record_new_game(["David", "Oliver"], 11, 8, ["Manfred", "Brandon"], data)
data = record_new_game(["David", "Oliver"], 11, 4, ["Manfred", "Brandon"], data)
data = record_new_game(["David", "Oliver"], 11, 8, ["Manfred", "Brandon"], data)
data = record_new_game(["Brandon", "Oliver"], 12, 10, ["Matthew", "Moustache"], data)
data = record_new_game(["Brandon", "Oliver"], 11, 4, ["Matthew", "Moustache"], data)

data = record_new_game(["David"], 5, 11, ["Brandon"], data)
data = record_new_game(["Brandon"], 6, 11, ["Manfred"], data)
data = record_new_game(["David"], 11, 8, ["Manfred"], data)
data = record_new_game(["Brandon"], 11, 9, ["David"], data)
data = record_new_game(["Brandon"], 11, 5, ["Manfred"], data)
data = record_new_game(["David"], 11, 7, ["Brandon"], data)
data = record_new_game(["David"], 12, 10, ["Manfred"], data)
data = record_new_game(["Brandon"], 11, 7, ["Manfred"], data)

data = record_new_game(["Brandon"], 11, 4, ["Manfred"], data)
data = record_new_game(["David"], 10, 12, ["Brandon"], data)
data = record_new_game(["Brandon"], 12, 10, ["Manfred"], data)
data = record_new_game(["David"], 11, 7, ["Brandon"], data)
data = record_new_game(["David"], 8, 11, ["Manfred"], data)
data = record_new_game(["Manfred"], 12, 10, ["Brandon"], data)
data = record_new_game(["David"], 11, 9, ["Manfred"], data)
data = record_new_game(["David"], 11, 9, ["Brandon"], data)

data = record_new_game(["Brandon"], 11, 7, ["Oliver"], data)
data = record_new_game(["Brandon", "Oliver"], 11, 6, ["Manfred", "Shilei"], data)
data = record_new_game(["Brandon", "Oliver"], 11, 9, ["Manfred", "David"], data)
data = record_new_game(["Brandon", "Oliver"], 11, 5, ["David", "Shilei"], data)
data = record_new_game(["Oliver"], 11, 8, ["Manfred"], data)


# Sort data by elo
data = OrderedDict(sorted(data.items(),
       key = lambda x: getitem(x[1], 'elo'), reverse=True))

print('| Name    | elo   | elo_change | game_played | win  | loss | w/l  |')
for player, value in data.items():
    if value["game_played"] >= 10:
        print(f'| {player:<7} | {value["elo"]:<5} | {value["elo_change"]:<10} | {value["game_played"]:<11} | {value["win"]:<4} | {value["loss"]:<4} | {value["w/l"]:<4} |')

with open("elo_rating.json", "w") as json_file:
    json_file.write("{\n")
    for i, (player, value) in enumerate(data.items()):
        json_file.write(f'    "{player}": {{"elo": {value["elo"]}, "elo_change": {value["elo_change"]}, "game_played": {value["game_played"]}, "win": {value["win"]}, "loss": {value["loss"]}, "w/l": {value["w/l"]}}}')
        if i < len(data) - 1:
            json_file.write(",\n")
        else:
            json_file.write("\n")
    json_file.write("}\n")