from enum import Enum


class AllowedSotMode(str, Enum):
    JI = "JI"
    RC = "RC"

    def __str__(self) -> str:
        return str(self.value)
