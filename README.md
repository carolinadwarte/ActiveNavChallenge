# Counting Game

```commandline
usage: game.py [-h] [-l] [-g GAME] [--ui] [-r RANGE RANGE]

options:
  -h, --help            show this help message and exit
  -l, --list            List available games
  -g GAME, --game GAME  Specify the game to be played
  --ui                  Open UI
  -r RANGE RANGE, --range RANGE RANGE
                        Specify a range of numbers (start end)
```

This is a program that runs one of two counting games. It can be interacted with via CLI or via the built in GUI.  

## Example inputs
To run the included tests: `python -m pytest`  
Example to input ranges via the terminal: `python3 game.py -r 5 7`  
If a range is not specified it will default to use [1,100].  
Example to choose a specific game via the terminal: `python3 game.py -g BangWhizz`   
To run the ui: `python3 game.py --ui`  
The menu in the ui can be used to select a different game.


## Installation

Required software:
- [Python 3.11](https://www.python.org/downloads/) or later
- Python Packages: 
    Before installing the Python packages, a virtual environment needs to be set up. To do this, run:  
        `python3 -m venv venv`  
        `source venv/bin/activate`
    Make sure python is configured to use tkinter, to install on mac use: 
        `brew install python-tk`    
    - `tkinter` for the gui
        - Install using command: `python3 -m pip install tk`
    - `pytest` for testing
        - Install using command: `python3 -m pip install pytest`
