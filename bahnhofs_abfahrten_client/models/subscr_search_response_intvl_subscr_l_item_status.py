from enum import Enum


class SubscrSearchResponseIntvlSubscrLItemStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
