import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  # 16 points
            Player("Lemieux", "PIT", 45, 54),  # 99 points
            Player("Kurri",   "EDM", 37, 53),  # 90 points
            Player("Yzerman", "DET", 42, 56),  # 98 points
            Player("Gretzky", "EDM", 35, 89)   # 124 points
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_existing_player(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_non_existing_player(self):
        player = self.stats.search("NonExistingPlayer")
        self.assertIsNone(player)

    def test_team_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertIn("Semenko", [player.name for player in edm_players])
        self.assertIn("Kurri", [player.name for player in edm_players])
        self.assertIn("Gretzky", [player.name for player in edm_players])

    def test_top_players_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 98 points

    def test_top_players_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")  # 45 goals
        self.assertEqual(top_players[1].name, "Yzerman")  # 42 goals
        self.assertEqual(top_players[2].name, "Kurri")    # 37 goals

    def test_top_players_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")  # 89 assists
        self.assertEqual(top_players[1].name, "Lemieux")  # 54 assists
        self.assertEqual(top_players[2].name, "Yzerman")  # 56 assists

    def test_top_players_more_than_available(self):
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 5)  # Should return all players

if __name__ == "__main__":
    unittest.main()
