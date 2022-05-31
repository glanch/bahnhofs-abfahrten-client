from enum import Enum


class PossibleShort(str, Enum):
    VALUE_0 = "1"
    VALUE_1 = "2"
    VALUE_2 = "3"
    VALUE_3 = "4"
    VALUE_4 = "3R"
    T = "T"
    VALUE_6 = "3V"
    M = "M"

    def __str__(self) -> str:
        return str(self.value)
