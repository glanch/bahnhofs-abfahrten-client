from enum import Enum


class SubscrChannelNoSoundOptionValue(str, Enum):
    VALUE_0 = "1"

    def __str__(self) -> str:
        return str(self.value)
