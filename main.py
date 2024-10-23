
from FizzBuzzGame import FizzBuzzGame
from gui import Gui

if __name__ == "__main__":
    """ Code inside this closure will only run if this file is called directly """
    x = Gui(FizzBuzzGame())
    x.uiStructure()

#    for num in range(1, 101):
#        print(calculate_string(num))
