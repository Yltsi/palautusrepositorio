import requests
from player import Player
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

class PlayerReader:
    def __init__(self,url):
        self.url=url
        self.players =self.get_players()

    def get_players(self):
        data=requests.get(self.url).json()
        return [Player(player_dict)for player_dict in data] 

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.players
    
    def top_scorers_by_nationality(self, nationality):
        sorted_players = [player for player in self.players if player.nationality == nationality]
        sorted_players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        return sorted_players


def main():
    console = Console()
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    seasons = ["2023-24", "2022-23", "2021-22", "2020-21", "2019-20", "2018-19"]
    nationalities = ["FIN", "SWE", "USA", "CAN", "RUS", "SVK", "LAT", "BLR", "AUS", "CZE", "GER", "DEN", "NOR", "GBR", "SLO"]

    season = Prompt.ask(f"Select season [{'/'.join(seasons)}]:", choices=seasons)
    nationality = Prompt.ask(f"Select nationality [{'/'.join(nationalities)}]:", choices=nationalities)

    console.print(f"\nTop scorers of {nationality} season {season}", style="bold purple")

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("name", style="cyan")
    table.add_column("team", style="green")
    table.add_column("goals", style="yellow")
    table.add_column("assists", style="yellow")
    table.add_column("points", style="yellow")

    for player in players:
        total_points = player.goals + player.assists
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(total_points))

    console.print(table)

if __name__ == "__main__":
    main()
