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
# May 15
data = record_new_game(["Sidney", "Oliver"], 11, 7, ["David", "Geneviève"], data)
data = record_new_game(["Sidney", "Brandon"], 11, 9, ["David", "Oliver"], data)
data = record_new_game(["Sidney"], 12, 10, ["Brandon"], data)
# May 16
data = record_new_game(["Brandon", "David"], 11, 8, ["Sidney", "Oliver"], data)
data = record_new_game(["Brandon", "Oliver"], 12, 10, ["Sidney", "David"], data)
data = record_new_game(["Brandon", "Sidney"], 6, 11, ["David", "Oliver"], data)
data = record_new_game(["Brandon", "David"], 12, 10, ["Sidney", "Oliver"], data)
data = record_new_game(["Sidney"], 11, 7, ["David", "Oliver"], data)
data = record_new_game(["Sidney"], 11, 9, ["David"], data)
data = record_new_game(["Sidney"], 11, 8, ["Oliver"], data)
data = record_new_game(["Sidney"], 12, 10, ["Brandon"], data)
# May 17
data = record_new_game(["Oliver", "David"], 7, 11, ["Sidney"], data)
data = record_new_game(["Sidney", "David"], 5, 11, ["Oliver"], data)
data = record_new_game(["David"], 10, 12, ["Oliver", "Sidney"], data)
# May 21
data = record_new_game(["Brandon", "Sidney"], 11, 7, ["Oliver"], data)
# May 22
data = record_new_game(["Brandon"], 12, 10, ["Sidney"], data)
data = record_new_game(["Brandon"], 11, 3, ["Sidney"], data)
# May 23
data = record_new_game(["David", "Sidney"], 11, 5, ["Kayra", "Oliver"], data)
data = record_new_game(["David", "Sidney"], 11, 8, ["Brandon", "Oliver"], data)
data = record_new_game(["Brandon", "Sidney"], 11, 6, ["David", "Oliver"], data)
# May 24
data = record_new_game(["Sidney"], 12, 10, ["David"], data)
data = record_new_game(["Sidney"], 11, 6, ["Kayra"], data)
data = record_new_game(["Sidney"], 12, 10, ["David"], data)
# May 27
data = record_new_game(["Oliver"], 11, 5, ["Brandon", "Sidney"], data)
# May 28
data = record_new_game(["David", "Sidney"], 6, 11, ["Brandon", "Oliver"], data)
data = record_new_game(["David", "Sidney"], 9, 11, ["Brandon", "Oliver"], data)
data = record_new_game(["Oliver", "Kayra"], 8, 11, ["Brandon", "Sidney"], data)
data = record_new_game(["Oliver", "David"], 11, 7, ["Sidney", "Kayra"], data)
data = record_new_game(["Brandon", "Kayra"], 5, 11, ["David", "Oliver"], data)
# May 29
data = record_new_game(["David", "Kayra"], 2, 11, ["Sidney", "Oliver"], data)
data = record_new_game(["David", "Kayra"], 3, 11, ["Sidney", "Oliver"], data)
data = record_new_game(["David", "Sidney"], 11, 9, ["Kayra", "Oliver"], data)
# May 31
data = record_new_game(["Sidney", "Kayra"], 11, 8, ["Manfred", "Jordan"], data)
data = record_new_game(["David", "Kayra"], 3, 11, ["Sidney", "Jordan"], data)
data = record_new_game(["David", "Oliver"], 11, 7, ["Sidney", "Kayra"], data)
data = record_new_game(["Oliver", "Brandon"], 10, 12, ["David", "Kayra"], data)
data = record_new_game(["Oliver", "David"], 11, 8, ["Brandon", "Manfred"], data)
data = record_new_game(["Brandon", "Oliver"], 11, 6, ["Jordan", "Sidney"], data)
data = record_new_game(["Oliver"], 11, 8, ["Sidney"], data)
# June 4
data = record_new_game(["David", "Kayra"], 11, 8, ["Brandon", "Manfred"], data)
data = record_new_game(["David", "Sidney"], 11, 8, ["Kayra", "Manfred"], data)
# June 6
data = record_new_game(["Sidney", "Brandon"], 11, 8, ["David", "Manfred"], data)
data = record_new_game(["Sidney", "Brandon"], 9, 11, ["Manfred", "Oliver"], data)
data = record_new_game(["Sidney", "Brandon"], 11, 6, ["Manfred", "David"], data)
data = record_new_game(["David", "Manfred"], 11, 6, ["Brandon", "Oliver"], data)
data = record_new_game(["David", "Sidney"], 9, 11, ["Brandon", "Oliver"], data)


data = OrderedDict(sorted(data.items(),
       key = lambda x: getitem(x[1], 'elo'), reverse=True))

print('| Name | elo | elo_change | game_played | win | loss | w/l |')
for player, value in data.items():
    if value["game_played"] >= 10:
        print(player + "{:8} {:7} {:10} {:10} {:6} {:6}".format(value["elo"], value["elo_change"], value["game_played"], value["win"], value["loss"], value["w/l"]))

with open("elo_rating.json", "w") as json_file:
    json.dump(data, json_file)
