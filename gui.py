import tkinter as tk
from CountingGame import CountingGameBase

class Gui():
    ui = tk.Tk()

    def __init__(self, game: CountingGameBase):
        self.game = game
        self.ui.title("FizzBuzz - Counting Game")
        #window size
        self.ui.geometry("400x200")
        # prompting the user for input
        inputPrompt = tk.Label(self.ui, text="Your Input:", font=("Arial", 20))
        inputPrompt.pack()
        self.entryBox = tk.Entry(self.ui)
        self.entryBox.pack()

        # Button to trigger FizzBuzz calculation
        checkButton = tk.Button(self.ui, text="Check FizzBuzz", command=self.show, font=("Arial", 20))
        checkButton.pack()

        # Static "Result:" label, positioned on the left
        result_label_frame = tk.Frame(self.ui)
        result_label_frame.pack()

        outputLabel = tk.Label(result_label_frame, text="Result: ", font=("Arial", 20))
        outputLabel.pack(side=tk.LEFT)

        # Label to display the result
        self.result_label = tk.Label(result_label_frame, text="", font=("Arial", 20))
        self.result_label.pack(side=tk.LEFT)

    def show(self):
        try:
            num = int(self.entryBox.get())
            msg = self.game.calculate_string(num)
            if msg is None:
                msg = "Value out of bounds"
        except ValueError:
            msg = "Please enter a valid number"
        
        self.result_label.config(text=msg)

    def uiStructure(self):
        self.ui.mainloop()

    