from CountingGame import CountingGameBase


class FizzBuzzGame(CountingGameBase):
    def getName(self) -> str:
        return "FizzBuzz"

    def rangeCheck(self, num: int):
        """_summary_
        Checks if the given number is in range.
        Args:
            num (int): the number to be checked

        Returns:
            bool: True if in range, False otherwise
        """
        range = (1, 100)
        return not (num < range[0] or num > range[1])

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
