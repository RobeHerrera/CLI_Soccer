class Team:
    """
    Model for soccer team.
    Scalable class to be able to add more member and methods like:
        - Number of players
        - Player's names
        - Player's positions
        - Goals
        - Shots
        - And more statistics
    """

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name},{self.score}"

    def __repr__(self):
        return f"Team('{self.name}',{self.score})"

    def __iter__(self):
        return self.name

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Team):
            if self.name == other.name and self.score == other.score:
                return True
        return False
