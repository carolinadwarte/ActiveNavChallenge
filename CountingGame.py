# This is the interface for counting games.
from abc import ABC, abstractmethod


class CountingGameBase(ABC):
    """_summary_
    A base class for counting games, these methods are expected by any delivery method.
    """

    @abstractmethod
    def getName(self) -> str:
        """_summary_
            Get Name of the game.
        Returns:
            str: The name of the game e.g. "FizzBuzz"
        """
        pass

    @abstractmethod
    def calculate_string(self, num: int) -> str | int:
        """_summary_
            Deals with game specific logic.
        Args:
            num (int): the number to be 'played'
        Returns:
            int | str: based on the games response e.g. 7 or "Fizzbuzz"
        """
        pass
