# CLI_Soccer
This simple CLI (Command Line Interface), read a TXT file and return the standing according
to the rules:
- Win: 3 points 
- Tie: 1 points
- Lose: 0 points 
- If two teams have the same point are order alphabetically

## Example Input / Output
### Format for the Input
File: input.txt
```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```
### Format for the Output
Console output:
```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## Docker
1. Install Docker Engine from the following page instructions: `https://docs.docker.com/engine/install/ubuntu/`
2. Docker Build `docker build --pull --rm -f "Dockerfile" -t cli_soccer:latest "."`
3. Run in interctve mode `docker run -it  cli_soccer`
4. Should start the CMD loop.

## Instructions for using a virtual environment 
1. Create virtual environment `python3 -m venv myenv`
2. Activate it `source myenv/bin/activate` or windows CDM `.\myenv\Scripts\activate.bat` or PS `.\myenv\Scripts\Activate.ps1` 
3. `python -m pip install -r soccer_app/requirements.txt`
4. `cd soccer_App/`
5. `python main.py`
6. Should start the CMD loop.

### Commands
These are the commands available in the app:
- load: Add matches to the current league.
- results: Show the current standings of the teams.
- quit: Exit the application.

## Examples:
##### Load
Add a serial of matches to the ranking table
- Command: `load [FILE]` | `l [FILE]`
- Example: `load inputs/input1.txt`
tip:You can type only `load` or `l` to load the default file `inputs/input1.txt`
- Exceptions: `Error Format in the Input File, please check your matches in line: {number_line}.` that could happend because some of these cases:
  - Missing team information.
  - Match format is incorrect.

##### Results
Print the curret ranking table
- Command: `results` | `r`
- Example: `r`
- Output: 
```
1. Tarantulas, 18 pts
1. Lions, 15 pts
2. Snakes, 3 pts
3. FC Awesome, 3 pts
4. Grouches, 0 pts
```
- exeptions: If you try to visualize a result with no matches you will get the following output:
`Please load first a file with matches....`

##### Quit
Exit the application
- Command: quit | q
- Example: `q`
- Output: `exiting ... `

### CHARACTERISTICS
- Can be used with DOCKER or with a Python Virtual Environment.
- Scalable to use any Python Framework as Django or Flask.
- Scalable to add more statistics to each team.
- PEP8 as a coding guideline (Can be use other Type Checker as MyPy).
- Use CMD library to improve the user experience in console.
- Handling errors (Custom Exceptios). 
- Full test coverage 100% (using coverage library).
- Similar approach to MVC architecure. 
