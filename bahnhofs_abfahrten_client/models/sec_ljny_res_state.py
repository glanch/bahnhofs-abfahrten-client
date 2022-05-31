from enum import Enum


class SecLJNYResState(str, Enum):
    N = "N"
    B = "B"
    S = "S"

    def __str__(self) -> str:
        return str(self.value)
