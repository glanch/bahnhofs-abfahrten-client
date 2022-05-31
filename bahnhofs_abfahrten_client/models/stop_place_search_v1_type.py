from enum import Enum


class StopPlaceSearchV1Type(str, Enum):
    S = "S"
    ALL = "ALL"

    def __str__(self) -> str:
        return str(self.value)
