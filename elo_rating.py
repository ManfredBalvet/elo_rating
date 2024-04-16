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

data = record_new_game(["Oliver"], 11, 7, ["Manfred"], data)
data = record_new_game(["Oliver"], 11, 9, ["Manfred"], data)
data = record_new_game(["Oliver"], 8, 11, ["Manfred"], data)
data = record_new_game(["Oliver"], 10, 12, ["Manfred"], data)
data = record_new_game(["Sidney"], 9, 11, ["Manfred", "Oliver"], data)
data = record_new_game(["Sidney"], 11, 6, ["Manfred", "Oliver"], data)
data = record_new_game(["Sidney"], 9, 11, ["Manfred"], data)

data = OrderedDict(sorted(data.items(),
       key = lambda x: getitem(x[1], 'elo'), reverse=True))

print('| Name | elo | elo_change | game_played | win | loss | draw |')
for player, value in data.items():
    print(player + "{:8} {:7} {:10} {:10} {:6} {:6}".format(value["elo"], value["elo_change"], value["game_played"], value["win"], value["loss"], value["draw"]))

with open("elo_rating.json", "w") as json_file:
    json.dump(data, json_file)
