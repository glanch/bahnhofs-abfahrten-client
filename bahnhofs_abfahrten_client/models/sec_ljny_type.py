from enum import Enum


class SecLJNYType(str, Enum):
    JNY = "JNY"

    def __str__(self) -> str:
        return str(self.value)
