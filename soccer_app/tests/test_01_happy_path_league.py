import pytest
from model.soccer_team import Team
from unittest import TestCase
from model.league_stats import Rank

# Global instances for all the test case
rank = Rank()


@pytest.fixture
def happy_path():
    """ Test when everything is in place, with a small amount of teams"""
    happy_path.matches = f"""
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
"""
    happy_path.file_name = 'tests/my_test.txt'
    with open(happy_path.file_name, 'w') as f:
        f.write(happy_path.matches)

    happy_path.data = [
        {"homeTeam": "Lions", "homeScore": 3, "visitTeam": "Snakes", "visitScore": 3},
        {"homeTeam": "Tarantulas", "homeScore": 1, "visitTeam": "FC Awesome", "visitScore": 0},
        {"homeTeam": "Lions", "homeScore": 1, "visitTeam": "FC Awesome", "visitScore": 1},
        {"homeTeam": "Tarantulas", "homeScore": 3, "visitTeam": "Snakes", "visitScore": 1},
        {"homeTeam": "Lions", "homeScore": 4, "visitTeam": "Grouches", "visitScore": 0}
    ]

    happy_path.scores = {
        'Lions': Team('Lions', 5),
        'Snakes': Team('Snakes', 1),
        'Tarantulas': Team('Tarantulas', 6),
        'FC Awesome': Team('FC Awesome', 1),
        'Grouches': Team('Grouches', 0)
    }

    happy_path.table = f"""1. Tarantulas, 6 pts
2. Lions, 5 pts
3. Snakes, 1 pt
3. FC Awesome, 1 pt
5. Grouches, 0 pts
"""
    return happy_path


def test_match_parsing(happy_path):
    """ Test correct parsing, white-box """
    out = Rank._read_file(happy_path.file_name)
    output_matches = happy_path.data
    assert out == output_matches


def test_record_result(happy_path):
    """ Test correct record of the values from the file """
    rank.record_result(happy_path.file_name)
    # Option 1
    TestCase().assertDictEqual(rank.rank_teams, happy_path.scores)
    # Option 2
    # assert str(rank.teams) == str(output_stands)


def test_table_ranking(happy_path):
    """ Test ranking table """
    table_str = rank.table_ranking()
    # Option 1
    TestCase().assertMultiLineEqual(table_str, happy_path.table)
    # Option 2
    # assert str(table_str) == str(happy_path.table)
