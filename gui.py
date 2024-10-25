# An example alternative delivery method for a counting game.
# Presents a UI for a user to input a single number.
import logging
import tkinter as tk
from CountingGame import CountingGameBase


class Gui:
    ui = tk.Tk()
    log = logging.getLogger(__name__)

    def __init__(self, gameList: list[CountingGameBase]):
        self.gameList = gameList
        self.ui.title("Counting Games")

        # current game
        self.currentGameName = tk.Label(self.ui, text="", font=("Arial", 20))
        self.currentGameName.pack()

        # window size
        self.ui.geometry("400x200")
        # Menu
        menu = tk.Menu(self.ui)
        self.ui.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="Game", menu=filemenu)

        for game in gameList:
            filemenu.add_command(
                label=game.getName(), command=lambda game=game: self.changeGame(game)
            )

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.ui.quit)
        # prompting the user for input
        inputPrompt = tk.Label(self.ui, text="Your Input:", font=("Arial", 20))
        inputPrompt.pack()
        self.entryBox = tk.Entry(self.ui)
        self.entryBox.pack()

        # Button to trigger game calculation
        checkButton = tk.Button(
            self.ui, text="Check", command=self.show, font=("Arial", 20)
        )
        checkButton.pack()

        # Static "Result:" label, positioned on the left
        result_label_frame = tk.Frame(self.ui)
        result_label_frame.pack()

        outputLabel = tk.Label(result_label_frame, text="Result: ", font=("Arial", 20))
        outputLabel.pack(side=tk.LEFT)

        # Label to display the result
        self.result_label = tk.Label(result_label_frame, text="", font=("Arial", 20))
        self.result_label.pack(side=tk.LEFT)

        # Set the current game to the first in the list
        self.changeGame(gameList[0])

    def changeGame(self, game: CountingGameBase):
        """_summary_
            Changes the game being played buy the GUI.
        Args:
            game (CountingGameBase): game to be played.
        """
        self.log.debug(f"Setting game to: {game.getName()}")
        self.game = game
        self.currentGameName.config(text=self.game.getName())

    def show(self):
        """_summary_
        Reads the number from the entry box and calculates the result from the game.
        """
        try:
            num = int(self.entryBox.get())
            msg = self.game.calculate_string(num)
        except ValueError:
            msg = "Please enter a valid number"

        self.result_label.config(text=msg)

    def start(self):
        """_summary_
        Runs the GUI indefinitely.
        """
        self.ui.mainloop()
