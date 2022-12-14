import operator
import re
from exceptions.soccer_exceptions import IncorrectMatchFormat, MissingInformationTeam
from model.soccer_team import Team


class Rank(object):
    """
    Soccer league statistics.
        Features:
            - record_result(file) -> load in memory matches from file.
            - print_ranking() -> print ranking table.

    SCALABLE:
        - Can implement for more statistics like, goals, shots, etc.
    """

    def __init__(self):
        self.rank_teams = {}

    @staticmethod
    def _read_file(file):
        """
        Filter data from the txt file and put everything in memory
        Update the table's teams and their points based on a match result.
        REGEX:
            TEAM: (from the back take the group after the first integer)
                - Francisco
                - San Francisco
                - San Francisco 49
                - San Francisco 49 er
            SCORE: (from the back take the first integer)
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
            {"homeTeam": Chivas, homeScore:1, "visitTeam": America, visitScore:0},
            {"homeTeam": Atlas, homeScore:1, "visitTeam": Chivas, visitScore:3},
            {"homeTeam": America, homeScore:1, "visitTeam": Atlas, visitScore:2}
            ]
        """
        matches = []
        with open(file) as f:
            for number_line, line in enumerate(f, start=1):

                # Skip empty / blank lines
                line = line.strip('\n')
                if line.isspace() or len(line) == 0:
                    continue

                """
                    Fix when the input file is similar to :
                        Snakes 3 , Lions 49er 3
                        Snakes 5
                    Missing the second team and with no comma.
                """
                team = ()
                score = ()
                try:
                    teams_scores = line.split(',')
                    if len(teams_scores) < 2:
                        raise MissingInformationTeam(line)
                    # Process each match
                    for teamResult in teams_scores:
                        team += re.search(r"(\S+.*)\s+\d+\s*$", teamResult).group(1),
                        score += int(re.search(r"(\d+)\s*$", teamResult).group(1)),
                    matches.append({"homeTeam": team[0], "homeScore": score[0],
                                    "visitTeam": team[1], "visitScore": score[1]})

                # Custom Exceptions
                except MissingInformationTeam as e:
                    print(e)
                    matches = []
                except AttributeError:
                    print(IncorrectMatchFormat(line))
                    matches = []
                finally:
                    if len(matches) == 0:
                        print(f"Error Format in the Input File, please check your matches in line: {number_line}.")
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
            if home_team_name not in self.rank_teams.keys():
                self.rank_teams[home_team_name] = Team(teamResult["homeTeam"])
            if visit_team_name not in self.rank_teams.keys():
                self.rank_teams[visit_team_name] = Team(teamResult["visitTeam"])

            # Record result match
            if home_team_score == visit_team_score:
                self._record_tie(home_team_name)
                self._record_tie(visit_team_name)
            else:
                self._record_win(home_team_name if home_team_score > visit_team_score else visit_team_name)

    def _record_win(self, team_name):
        self.rank_teams[team_name].score += 3

    def _record_tie(self, team_name):
        self.rank_teams[team_name].score += 1

    def table_ranking(self):
        """
        Generate ordered ranking strings of teams and their points in the table.

        Which sorting use according to:
        https://stackoverflow.com/questions/2705104/lambda-vs-operator-attrgetterxxx-as-a-sort-key-function

        Option 1 (operator.attrgetter()) is faster than Option 2 (use self.item[key])
        """

        # Option 1
        # for team in (sorted(self.teams.values(), key=operator.attrgetter('score'), reverse=True)):
        #     print(team.name + " : " + str(team.score))

        # Option 2
        # for team in sorted(self.teams, key=lambda name: self.teams[name].score, reverse=True):
        #     print(team)

        # Using option 1 for sorting
        last_pts = 0
        rank = 1
        table_str = ""
        for index, team in enumerate(
                sorted(self.rank_teams.values(), key=operator.attrgetter('score'), reverse=True), start=1):
            # Method when we have a points tie
            if team.score != last_pts:
                # Rank is equal to the index that's why it start at 1
                rank = index
            # Manage the string when is only one point
            pts_str = "pt" if team.score == 1 else "pts"
            last_pts = team.score
            table_str += f"{rank}. {team.name}, {team.score} {pts_str}\n"
        return table_str
