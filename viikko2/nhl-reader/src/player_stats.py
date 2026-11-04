class PlayerStats:
    
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        filtered_players = list(filter(lambda player: player.nationality == nationality, players))

        return sorted(
            filtered_players, key=lambda player: player.points, reverse=True
        )