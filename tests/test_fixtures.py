import pytest
from model.soccer_team import Team

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

    # TODO: add the table ranking
    happy_path.table = ""
    return happy_path




