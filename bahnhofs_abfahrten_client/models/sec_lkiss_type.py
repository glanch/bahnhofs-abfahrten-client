from enum import Enum


class SecLKISSType(str, Enum):
    KISS = "KISS"

    def __str__(self) -> str:
        return str(self.value)
