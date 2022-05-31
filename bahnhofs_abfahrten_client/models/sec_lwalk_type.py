from enum import Enum


class SecLWALKType(str, Enum):
    WALK = "WALK"
    TRSF = "TRSF"

    def __str__(self) -> str:
        return str(self.value)
