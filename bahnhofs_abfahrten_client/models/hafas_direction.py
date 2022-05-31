from enum import Enum


class HafasDirection(str, Enum):
    B = "B"
    F = "F"
    FB = "FB"

    def __str__(self) -> str:
        return str(self.value)
