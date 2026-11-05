"""Player class for representing individual players."""
# pylint: disable=too-few-public-methods
class Player:
    """A class to represent an individual player."""
    def __init__(self, palyer_dict):
        """Initializes the Player class with a dictionary of player data."""
        self.name = palyer_dict['name']
        self.team = palyer_dict['team']
        self.goals = palyer_dict['goals']
        self.assists = palyer_dict['assists']
        self.nationality = palyer_dict['nationality']
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:3} + {self.assists:3} = {self.points:4}"
