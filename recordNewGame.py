import math

class Player:
    def __init__(self, name, elo, k, point_factor, result, team, expected_player_score, expected_team_score):
        self.name = name
        self.elo = elo
        self.k = k
        self.point_factor = point_factor
        self.result = result
        self.team = team
        self.expected_player_score = expected_player_score
        self.expected_team_score = expected_team_score

def get_expected_player_score(player, opponents, data):
    expected_player_score = 0
    for opponent in opponents:
        expected_player_score += (1 / (1 + (10 ** ((data[opponent]["elo"] - data[player]["elo"])/500))))
        
    return expected_player_score / len(opponents)

def get_k(game_played):
    return (50 / (1 + ((game_played) / 300)))

def get_point_factor(score):
    return 2 + (math.log10(abs(score[0] - score[1]) + 1)) **3

def get_result(score):
    if score[0] > score[1]:
        return 1
    elif score[0] < score[1]:
        return 0
    elif score[0] == score[1]:
        return 0.5

def record_new_game(team_A, score_A, score_B, team_B, data):
    players = []

    for i, player in enumerate(team_A + team_B):
        if player not in data.keys():
            data[player] = {"elo" : 1500, "elo_change" : 0, "game_played" : 0, "win" : 0, "loss" : 0, "draw" : 0}
        
        if player in team_A:
            team = "A"
            score = [score_A, score_B]
        elif player in team_B:
            team = "B"
            score = [score_B, score_A]

        data[player]["game_played"] += 1


        players.append(Player(
            player, # name
            data[player]["elo"], #elo
            get_k(data[player]["game_played"]), #k
            get_point_factor(score), # point_factor
            get_result(score), # result
            team, # team
            0, # expected_plsyer_score_player
            0, # expected_team_score
        ))

    for i, player in enumerate(team_A + team_B):
        if players[i].team == "A":
            opponents = team_B
        elif players[i].team == "B":
            opponents = team_A
        
        players[i].expected_player_score = get_expected_player_score(player, opponents, data)

    expected_score_team_A = 0
    expected_score_team_B = 0
    for i, player in enumerate(team_A + team_B):
        
        if player in team_A:
            expected_score_team_A += ((players[i].expected_player_score) / (len(team_A)))
        elif player in team_B:
            expected_score_team_B += ((players[i].expected_player_score) / (len(team_B)))

    for i, player in enumerate(team_A + team_B):
        if player in team_A:
            players[i].expected_team_score = expected_score_team_A
        elif player in team_B:
            players[i].expected_team_score = expected_score_team_B
        
        if players[i].result == 0:
            data[player]["loss"] += 1
        elif players[i].result == 0.5:
            data[player]["draw"] += 1
        elif players[i].result == 1:
            data[player]["win"] += 1

        data[player]["elo_change"] = round(players[i].k * players[i].point_factor * (players[i].result - ((players[i].expected_team_score + players[i].expected_player_score)/2)))
        data[player]["elo"] = players[i].elo + data[player]["elo_change"]

    return data
