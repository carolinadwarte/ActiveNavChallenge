# Entry point for the program, parses any arguments passed via the command line
from logging import basicConfig, DEBUG
from BangWhizGame import BangWhizGame
from CountingGame import CountingGameBase
from FizzBuzzGame import FizzBuzzGame
from gui import Gui
import argparse

basicConfig(level=DEBUG)


def find_game(name: str, game_list: list[CountingGameBase]):
    """_summary_
        Finds a game with a given name in the game list.
    Args:
        name (str): name of the game to find
        game_list (list[CountingGameBase]): list of games to search

    Returns:
        A game if found a match for the name else None.
    """
    for game in game_list:
        if game.getName() == name:
            return game


if __name__ == "__main__":
    # Add any new counting games here
    game_list: list[CountingGameBase] = [FizzBuzzGame(), BangWhizGame()]

    # Command line argument descriptions
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--list", help="List available games", action="store_true"
    )
    parser.add_argument("--ui", help="Open UI", action="store_true")
    parser.add_argument("-g", "--game", help="Specify the game to be played")
    parser.add_argument(
        "-r",
        "--range",
        help="Specify a range of numbers (start end)",
        nargs=2,
        type=int,
        default=[1, 100],
    )

    args = parser.parse_args()
    if args.range[0] >= args.range[1]:
        print("Invalid range: Start of range must be less than end.")
    elif args.list:
        print(f"Available games: {' '.join(game.getName() for game in game_list)}")
    elif args.ui:
        # Start the UI with the given games
        ui = Gui(game_list)
        ui.start()
    elif args.game:
        game = find_game(args.game, game_list)
        if game is None:
            print(f"Couldn't find game with name: {args.game}")
        else:
            print(f"Running {args.game}...")
            for i in range(args.range[0], args.range[1] + 1):
                print(game.calculate_string(i))
