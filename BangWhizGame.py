from CountingGame import CountingGameBase


class BangWhizGame(CountingGameBase):

    def getName(self) -> str:
        return "BangWhiz"

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
        multipleOf4 = num % 4 == 0
        multipleOf6 = num % 6 == 0

        match num:
            # the first condition checks if num is multiple of both 3 and 5 before checking individually
            case _ if multipleOf4 and multipleOf6:
                return "BangWhiz"
            case _ if multipleOf4:
                return "Bang"
            case _ if multipleOf6:
                return "Whiz"
            case _:
                return num
