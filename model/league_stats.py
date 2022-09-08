import re
from exceptions.soccer_exceptions import IncorrectMatchFormat
from model.soccer_team import Team


class Rank(object):
    """
    Soccer league statistics.
        Features:
            - record_result(file) -> load in memory matches from file.
            - print_ranking() -> print ranking table.

    TODO:
        - Implement for more statistics like, goals, shots, etc.
    """

    instance = None

    def __init__(self):
        self.teams = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Rank, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def _read_file(file):
        """
        Filter data from the txt file and put everything in memory
        Update the table's teams and their points based on a match result.
        REGEX:
            TEAM: (\S+.*)\s+\d+\s*$ (from the back take the group after the first integer)
                - Francisco
                - San Francisco
                - San Francisco 49
                - San Francisco 49 er
            SCORE:(\d+)\s*$ (from the back take the first integer)
                - 100 <BLANK>

        returns:
            - matches[
            {homeTeam: <TEAM_NAME>, homeScore: <SCORE>,
            visitTeam: <TEAM_NAME>, visitScore: <SCORE>},
            ,
            ....
            ]
        Example:
            matched[
            {homeTeam: Chivas, homeScore:1, visitTeam: America, visitScore:0},
            {homeTeam: Atlas, homeScore:1, visitTeam: Chivas, visitScore:3},
            {homeTeam: America, homeScore:1, visitTeam: Atlas, visitScore:2}
            ]

        TODO:
            - Decide if a bad entry will stop the ejection or
            continue and only ignoring that incorrect entry
            - "myteam 1" (Error, should not accept only one team)
        """
        matches = []
        with open(file) as f:
            for line in f:
                line = line.strip('\n')

                # Process each line in the file
                print("processing line> ", line)
                team = ()
                score = ()
                for teamResult in line.split(','):
                    print(teamResult)
                    try:
                        # Return only the name team
                        team += re.search("(\S+.*)\s+\d+\s*$", teamResult).group(1),
                        score += int(re.search("(\d+)\s*$", teamResult).group(1)),
                    except AttributeError:
                        raise IncorrectMatchFormat(teamResult)
                matches.append({"homeTeam": team[0], "homeScore": score[0],
                                "visitTeam": team[1], "visitScore": score[1]})
        return matches

    def record_result(self, file):
        """
        Adding points to the correspond team
        """

        matches = self._read_file(file)
        for teamResult in matches:
            # Object Team() can be scalable
            home_team_name = teamResult["homeTeam"]
            home_team_score = teamResult["homeScore"]
            visit_team_name = teamResult["visitTeam"]
            visit_team_score = teamResult["visitScore"]

            # Make sure that the team exist in the teams table
            # This LIST is only for scalability proposes or future implementations

            # Add Team Object in to the Dictionary
            if home_team_name not in self.teams.keys():
                print("No esta, agregar: " + home_team_name)
                self.teams[home_team_name] = Team(teamResult["homeTeam"])
            if visit_team_name not in self.teams.keys():
                print("No esta, agregar: " + visit_team_name)
                self.teams[visit_team_name] = Team(teamResult["visitTeam"])

            # Record result match
            if home_team_score == visit_team_score:
                self._record_tie(home_team_name)
                self._record_tie(visit_team_name)
            else:
                self._record_win(home_team_name if home_team_score > visit_team_score else visit_team_name)
        print(self.teams)

    def _record_win(self, team_name):
        self.teams[team_name].score += 3

    def _record_tie(self, team_name):
        self.teams[team_name].score += 1

    @classmethod
    def print_ranking(cls):
        pass
