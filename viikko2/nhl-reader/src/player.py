class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.nationality = player_dict['nationality']

    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name:<20} {self.team}  {self.goals} + {self.assists} = {points}"