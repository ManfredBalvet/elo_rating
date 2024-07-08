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



data = record_new_game(["David", "Kayra"], 11, 9, ["Sidney", "Oliver"], data)
data = record_new_game(["David", "Kayra"], 9, 11, ["Shilei", "Oliver"], data)
data = record_new_game(["David", "Kayra"], 6, 11, ["Shilei", "Oliver"], data)
data = record_new_game(["Sidney", "Manfred"], 12, 10, ["Kayra", "Oliver"], data)
data = record_new_game(["David", "Oliver"], 11, 8, ["Jordan", "Kayra"], data)
data = record_new_game(["Jordan", "Shilei"], 11, 5, ["Manfred", "Sidney"], data)
data = record_new_game(["David", "Oliver"], 11, 9, ["Shilei", "Jordan"], data)

data = record_new_game(["Sidney"], 11, 6, ["Oliver"], data)
data = record_new_game(["Sidney"], 4, 11, ["Oliver"], data)
data = record_new_game(["Sidney"], 5, 11, ["Oliver"], data)
data = record_new_game(["Sidney"], 2, 11, ["Oliver"], data)
data = record_new_game(["Sidney"], 9, 11, ["Oliver"], data)
data = record_new_game(["Kayra"], 5, 11, ["Oliver"], data)

data = OrderedDict(sorted(data.items(),
       key = lambda x: getitem(x[1], 'elo'), reverse=True))

print('| Name | elo | elo_change | game_played | win | loss | w/l |')
for player, value in data.items():
    if value["game_played"] >= 10:
        print(player + "{:8} {:7} {:10} {:10} {:6} {:6}".format(value["elo"], value["elo_change"], value["game_played"], value["win"], value["loss"], value["w/l"]))

with open("elo_rating.json", "w") as json_file:
    json.dump(data, json_file)
