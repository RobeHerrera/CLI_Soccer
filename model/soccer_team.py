class Team:
    """
    Model for soccer team.
    Scalable class to be able to add more member and methods like:
        - Number of players
        - Statistics
        -
    """
    def __int__(self, name, score=0):
        self.name = name
        self.score = score

    def add_score(self, score):
        self.score += score
