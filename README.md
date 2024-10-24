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

## Installation

Required software:
- [Python 3.11](https://www.python.org/downloads/) or later
- Python Packages: 
    - `tkinter` for the gui
        - Install using command: `python3 -m pip install tkinter`
    - `pytest` for testing
        - Install using command: `python3 -m pip install pytest`
