import tkinter as tk
from fizzbuzz import calculate_string

def show():
    try:
        num = int(entryBox.get())
        msg = calculate_string(num)
        if msg is None:
            msg = "Value out of bounds"
    except ValueError:
        msg = "Please enter a valid number"
    
    result_label.config(text=msg)

root = tk.Tk()
root.title("FizzBuzz - Counting Game")
#window size
root.geometry("400x200")
# prompting the user for input
inputPrompt = tk.Label(root, text="Your Input:", font=("Arial", 20))
inputPrompt.pack()
entryBox = tk.Entry(root)
entryBox.pack()

# Button to trigger FizzBuzz calculation
checkButton = tk.Button(root, text="Check FizzBuzz", command=show, font=("Arial", 20))
checkButton.pack()

# Static "Result:" label, positioned on the left
result_label_frame = tk.Frame(root)
result_label_frame.pack()

outputLabel = tk.Label(result_label_frame, text="Result: ", font=("Arial", 20))
outputLabel.pack(side=tk.LEFT)

# Label to display the result
result_label = tk.Label(result_label_frame, text="", font=("Arial", 20))
result_label.pack(side=tk.LEFT)

root.mainloop()