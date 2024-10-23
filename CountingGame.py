from abc import ABC, abstractmethod


class CountingGameBase(ABC):

    @abstractmethod
    def getName(self) -> str:
        return ""

    @abstractmethod
    def calculate_string(self, num: int):
        pass

    @abstractmethod
    def rangeCheck(self, num: int):
        pass
