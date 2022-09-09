import pytest
from tests.test_fixtures import *
from unittest import TestCase
from model.league_stats import Rank


def test_match_parsing(happy_path):
    """ Test correct parsing, white-box """
    out = Rank._read_file(happy_path.file_name)
    output_matches = happy_path.data
    assert out == output_matches


def test_record_result(happy_path):
    """ Test correct record of the values from the file """
    rank = Rank()
    rank.record_result(happy_path.file_name)
    # Option 1
    TestCase().assertDictEqual(rank.teams, happy_path.scores)
    # Option 2
    # assert str(rank.teams) == str(output_stands)

