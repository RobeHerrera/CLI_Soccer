# CLI_Soccer
This simple CLI (Command Line Interface), read a TXT file and return the standing according
to the rules:
- Win: 3 points 
- Tie: 1 points
- Lose: 0 points 
- If two teams have the same point are order alphabetically

## Example Input / Output
### Input
input.txt
```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```
### Output
Console output
```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## Instructions for using a virtual environment 
1. Create virtual environment `python3 -m venv myenv`
2. Activate it `source myenv/bin/activate` or windows CDM `.\myenv\Scripts\activate.bat` or PS `.\myenv\Scripts\Activate.ps1` 
3. `python -m pip install -r requirements.txt`
4. `cd CLI_Soccer/`
5. `python manage.py runserver`

## Usage
`python soccer_stands.py` to start the CLI loop

### CHARACTERISTICS
- Can be used also with Python Virtual Environment.
- Scalable to use any Python Framework as Django or Flask.
- Scalable to add more statistics to each team
- PEP8 as a coding guideline.
- Use CMD library to improve the user experience.
- Handling errors. 
- Testable see the folder 'tests' for more reference.
- Full test coverage 100% (using coverage library).

### Docker:
- Build Image `docker compose up`
- Run in interctve mode `docker run -it  cli_soccer`


