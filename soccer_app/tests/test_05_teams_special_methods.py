import pytest
from model.soccer_team import Team


def test_str_team():
    """ Test string override method """
    team1 = Team('Lions', 1)
    str_team = str(team1)
    assert str_team == "'Lions',1"


def test_repr_team():
    """ Test representation override method """
    assert repr(Team('Lions', 1)) == "<Team('Lions',1)>"


def test_not_eql_team():
    """ Test not equals teams """
    team1 = Team('Lions', 1)
    team2 = Team('Lions', 1)
    assert team1 == team2


def test_eql_team():
    """ Test equals teams """
    team1 = Team('Lions', 1)
    team2 = Team('Snakes', 1)
    assert team1 != team2
