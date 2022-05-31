from enum import Enum


class TravelerType(str, Enum):
    E = "E"
    K = "K"
    B = "B"

    def __str__(self) -> str:
        return str(self.value)
