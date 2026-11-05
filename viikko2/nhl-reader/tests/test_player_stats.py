import os
import sys

# Ensure src is on path so tests can import application modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from player import Player
from player_stats import PlayerStats


def make_player(name, team, goals, assists, nationality):
    return Player({
        'name': name,
        'team': team,
        'goals': goals,
        'assists': assists,
        'nationality': nationality,
    })


class StubReader:
    def __init__(self, players):
        # players should be a list of Player instances
        self._players = players

    def get_players(self):
        return self._players


def test_top_scorers_by_nationality_sorted_and_filtered():
    players = [
        make_player('A One', 'AAA', 10, 5, 'FIN'),  # 15
        make_player('B Two', 'BBB', 5, 5, 'FIN'),    # 10
        make_player('C Three', 'CCC', 8, 1, 'SWE'),  # 9
        make_player('D Four', 'DDD', 7, 4, 'FIN'),   # 11
    ]

    reader = StubReader(players)
    stats = PlayerStats(reader)

    top = stats.top_scorers_by_nationality('FIN')

    assert [p.name for p in top] == ['A One', 'D Four', 'B Two']


def test_top_scorers_by_team_sorted_and_filtered():
    players = [
        make_player('A One', 'NYR', 3, 2, 'CAN'),   # 5
        make_player('B Two', 'NYR', 6, 1, 'USA'),   # 7
        make_player('C Three', 'BOS', 10, 0, 'USA'),# 10
    ]

    reader = StubReader(players)
    stats = PlayerStats(reader)

    top = stats.top_scorers_by_team('NYR')

    assert [p.name for p in top] == ['B Two', 'A One']


def test_top_goal_scorers_sorted_by_goals():
    players = [
        make_player('A One', 'X', 1, 10, 'FIN'),
        make_player('B Two', 'Y', 5, 0, 'SWE'),
        make_player('C Three', 'Z', 3, 2, 'CAN'),
    ]

    reader = StubReader(players)
    stats = PlayerStats(reader)

    top = stats.top_goal_scorers()

    assert [p.name for p in top] == ['B Two', 'C Three', 'A One']
