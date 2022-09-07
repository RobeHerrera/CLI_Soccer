import re
from  exceptions.soccer_exceptions import IncorrectMatchFormat


class Rank:
    """Soccer league ranking table."""
    #
    # def _record_win(self, team):
    #     self.teams[team] += 3
    #
    # def _record_tie(self, team):
    #     self.teams[team] += 1

    def __init__(self):
        self.teams = ()
        self.scores = ()

    def record_result(self, line):
        """Update the table's teams and their points based on a match result.
        REGEX:
            TEAM: (\S+.*)\s+\d+\s*$ (from the back take the group after the first integer)
                - Francisco
                - San Francisco
                - San Francisco 49
                - San Francisco 49 er
            SCORE:(\d+)\s*$ (from the back take the first integer)
                - 100 <BLANK>
        """

        # self.scores = ()
        for teamResult in line.split(','):
            print(teamResult)
            try:
                # Return only the name team
                team = re.search("(\S+.*)\s+\d+\s*$", teamResult).group(1)
                score = int(re.search("(\d+)\s*$", teamResult).group(1))
                print(self.teams)
                print(self.scores)
            except AttributeError as e:
                raise IncorrectMatchFormat(teamResult)

        # Check if


        # for name in result.teams:
        #     if name not in self.teams:
        #         self.teams[name] = 0
        # team1, team2 = result.teams
        # score1, score2 = result.scores
        # if score1 == score2:
        #     self._record_tie(team1)
        #     self._record_tie(team2)
        # else:
        #     self._record_win(team1 if score1 > score2 else team2)

    # def _rank_comparison(self, team1, team2):
    #     """Comparison for sorting by points, or by team name if points are tied."""
    #     points1 = self.teams[team1]
    #     points2 = self.teams[team2]
    #     if points1 == points2:
    #         return locale.strcoll(team1, team2)
    #     else:
    #         return 1 if points1 < points2 else -1
    #
    # def generate_rankings(self):
    #     """Generate ordered ranking strings of teams and their points in the table."""
    #     lastPoints = 0
    #     rank = 1
    #     for index, team in enumerate(sorted(self.teams, cmp=self._rank_comparison), start=1):
    #         points = self.teams[team]
    #         if points != lastPoints:
    #             rank = index
    #         points_string = "pt" if points == 1 else "pts"
    #         yield "%d. %s, %d %s" % (rank, team, points, points_string)
    #         lastPoints = points
    #
    # def print_rankings(self):
    #     """Print descending ranking of teams and their points in the table."""
    #     for line in self.generate_rankings():
    #         print line
