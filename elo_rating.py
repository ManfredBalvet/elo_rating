import math
import json

class Player:
    def __init__(self, name, elo, k, point_factor, result, expected_score_player, expected_score_team):
        self.name = name
        self.elo = elo
        self.k = k
        self.point_factor = point_factor
        self.result = result
        self.expected_score = expected_score_player
        self.expected_score_team = expected_score_team

def get_expected_player_score(player, opponents, data):
    expected_player_score = 0
    for opponent in opponents:
        expected_player_score =+ 1 / (1 + 10 ^ (data[opponent]["elo"] - data[player]["elo"])/500)

    return expected_player_score / len(opponents)

def get_expected_team_score(team, data):
    expected_team_score = 0
    for player in team:
        expected_player_score =+ data[player][expected_player_score]
    return expected_team_score / len(team)

def get_k(game_played):
    return 50 / (1 +(game_played) / 300)

def get_point_factor(score_team_1, score_team_2):
    return 2 + (math.log10(abs(score_team_1 - score_team_2) + 1)) ^3

def get_result(score_team_1, score_team_2):
    if score_team_1 > score_team_2:
        return 1
    elif score_team_1 < score_team_2:
        return 0
    else:
        return 0.5

def get_new_rating(player):
    return player.elo + player.k * player.point_factor * (player.result - (player.expected_team_score + player.expected_player_score)/2)

def record_new_game(team_A, score_A, score_B, team_B, data):
    teams = [team_A, team_B]
    players = team_A + team_B
    for player in players:
        if player not in data:
            data[player] = {"elo" : 1500, "game_played" : 0}
        player.elo = data[player]["elo"]

    for player in players:
        if player in team_A:
            opponents = team_B
        elif player in team_B:
            opponents = team_A
        
        player.expected_score = get_expected_player_score(player, opponents, data)

    for team in teams:
        for player in team:
            if player in team_A:
                opponents = team_B
            elif player in team_B:
                opponents = team_A
        
            player.expected_team_score = get_expected_team_score(team, opponents, data)

    for player in players:
        data[player]["game_played"] =+ 1
        player.k = get_k(data[player]["game_played"])

    for player in team_A:
        player.point_factor = get_point_factor(score_A, score_B)
        player.result = get_result(score_A, score_B)
    
    for player in team_B:
        player.point_factor = get_point_factor(score_B, score_A)
        player.result = get_result(score_B, score_A)
    
    for player in players:
        data[player]["elo"] = get_new_rating(player)


with open("elo_rating.json", "r") as file:
    data = json.load(file)




