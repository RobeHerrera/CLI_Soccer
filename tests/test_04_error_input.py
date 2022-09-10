import pytest
from model.soccer_team import Team
from unittest import TestCase
from model.league_stats import Rank

# Global instances for all the test case
rank = Rank()


@pytest.fixture
def happy_path():
    """ Test when an error in input team occurred """
    happy_path.matches = f"""
Lions 1 ,Snakes 3
Snakes 3,
     """
    happy_path.file_name = 'tests/my_test.txt'
    with open(happy_path.file_name, 'w') as f:
        f.write(happy_path.matches)

    happy_path.data = []

    happy_path.scores = {}

    happy_path.table = f""

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
    # assert str(rank.rank_teams) == str(happy_path.scores)


def test_table_ranking(happy_path):
    """ Test ranking table """
    table_str = rank.table_ranking()
    # Option 1
    TestCase().assertMultiLineEqual(table_str, happy_path.table)
    # Option 2
    # assert str(table_str) == str(happy_path.table)
