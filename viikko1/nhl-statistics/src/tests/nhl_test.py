import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):

        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
    
    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)
    
    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
    
    def test_top_scorers(self):
        top_player = self.stats.top(1)
        self.assertEqual(top_player[0].name, "Gretzky")

    def test_top_scorers_by_goals(self):
        top_player = self.stats.top(1, sort_by=SortBy.GOALS)
        self.assertEqual(top_player[0].name, "Lemieux")

    def test_top_scorers_by_assists(self):
        top_player = self.stats.top(1, sort_by=SortBy.ASSISTS)
        self.assertEqual(top_player[0].name, "Gretzky")