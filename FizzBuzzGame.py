from CountingGame import CountingGameBase


class FizzBuzzGame(CountingGameBase):

    def getName(self) -> str:
        return "FizzBuzz"

    def rangeCheck(self, num: int):
        range = (0, 100)
        # check if num is between 0 - 100
        if num < range[0] or num > range[1]:
            return False
        return True

    def calculate_string(self, num: int):
        """Return input if no modication would be made, returns string otherwise"""
        # check if num is between 0 - 100
        if not self.rangeCheck(num):
            return None

        # conditions for x to be multiple of y: y/x=0
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
