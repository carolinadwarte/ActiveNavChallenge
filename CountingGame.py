from abc import ABC, abstractmethod


class CountingGameBase(ABC):
    """_summary_
    A base class for counting games, these methods are expected by the UI.
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
    def calculate_string(self, num: int) -> str | int | None:
        """_summary_

        Args:
            num (int): the number to be 'played'
        """
        pass

    @abstractmethod
    def rangeCheck(self, num: int) -> bool:
        pass
