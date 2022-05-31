from enum import Enum


class HimFilterMode(str, Enum):
    BIT = "BIT"
    EXC = "EXC"
    INC = "INC"
    UNDEF = "UNDEF"

    def __str__(self) -> str:
        return str(self.value)
