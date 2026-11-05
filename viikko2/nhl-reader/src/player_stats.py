# pylint: disable=too-few-public-methods
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        filtered_players = list(filter(lambda player: player.nationality == nationality, players))

        return sorted(
            filtered_players, key=lambda player: player.points, reverse=True
        )

    def top_scorers_by_team(self, team):
        players = self.reader.get_players()

        filtered_players = list(filter(lambda player: player.team == team, players))

        return sorted(
            filtered_players, key=lambda player: player.points, reverse=True
        )

    def top_goal_scorers(self):
        players = self.reader.get_players()

        return sorted(players, key=lambda player: player.goals, reverse=True)
