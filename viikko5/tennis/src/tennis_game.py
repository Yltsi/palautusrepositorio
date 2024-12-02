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
        if self.is_tied():
            return self.get_tied_score()
        if self.is_endgame():
            return self.get_endgame_score()
        return self.get_standard_score()

    def is_tied(self):
        return self.player1_score == self.player2_score

    def get_tied_score(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def is_endgame(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def get_endgame_score(self):
        score_difference = self.player1_score - self.player2_score
        if abs(score_difference) == 1:
            return f"Advantage {self.get_leading_player()}"
        return f"Win for {self.get_leading_player()}"

    def get_leading_player(self):
        return self.player1_name if self.player1_score > self.player2_score else self.player2_name

    def get_standard_score(self):
        return f"{self.get_score_name(self.player1_score)}-{self.get_score_name(self.player2_score)}"

    def get_score_name(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        