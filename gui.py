import logging
import tkinter as tk
from CountingGame import CountingGameBase


class Gui:
    ui = tk.Tk()
    log = logging.getLogger(__name__)

    def __init__(self, gameList: list[CountingGameBase]):
        self.game = gameList[0]
        self.gameList = gameList
        self.ui.title("Counting Games")

        # current game
        self.currentGameName = tk.Label(self.ui, text="FizzBuzz", font=("Arial", 20))
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

        # Button to trigger FizzBuzz calculation
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

    def changeGame(self, game: CountingGameBase):
        self.log.debug(f"Setting game to: {game.getName()}")
        self.game = game
        self.currentGameName.config(text=self.game.getName())

    def show(self):
        try:
            num = int(self.entryBox.get())
            msg = self.game.calculate_string(num)
            if msg is None:
                msg = "Value out of bounds"
        except ValueError:
            msg = "Please enter a valid number"

        self.result_label.config(text=msg)

    def start(self):
        self.ui.mainloop()
