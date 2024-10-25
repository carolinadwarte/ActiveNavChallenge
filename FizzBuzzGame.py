# A class to represent the FizzBuzz game.
from CountingGame import CountingGameBase


class FizzBuzzGame(CountingGameBase):
    def getName(self) -> str:
        return "FizzBuzz"

    def calculate_string(self, num: int):
        # conditions for x to be multiple of y: y%x=0
        multipleOf3 = num % 3 == 0
        multipleOf5 = num % 5 == 0

        match num:
            # the first condition checks if num is multiple of both 3 and 5 before checking individually
            case _ if multipleOf3 and multipleOf5:
                return "FizzBuzz"
            case _ if multipleOf3:
                return "Fizz"
            case _ if multipleOf5:
                return "Buzz"
            case _:
                return num
