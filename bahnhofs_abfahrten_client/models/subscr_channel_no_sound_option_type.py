from enum import Enum


class SubscrChannelNoSoundOptionType(str, Enum):
    NO_SOUND = "NO_SOUND"

    def __str__(self) -> str:
        return str(self.value)
