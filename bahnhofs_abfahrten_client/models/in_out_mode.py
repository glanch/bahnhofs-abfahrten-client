from enum import Enum


class InOutMode(str, Enum):
    B = "B"
    I = "I"
    N = "N"
    O = "O"

    def __str__(self) -> str:
        return str(self.value)
