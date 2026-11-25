scores = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):

        if self.player1_score == self.player2_score:
            return self.even_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_win()
        else:
            return self.regular_score()


    def even_score(self):
        
        if self.player1_score < 3:
            return f"{scores[self.player1_score]}-All"
        return "Deuce"

    def advantage_win(self):
        difference = self.player1_score - self.player2_score
        leader = "player1" if difference > 0 else "player2"

        if abs(difference) == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"

    def regular_score(self):
        player1 = scores[self.player1_score]
        player2 = scores[self.player2_score]
        return f"{player1}-{player2}"