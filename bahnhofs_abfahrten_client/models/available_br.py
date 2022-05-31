from enum import Enum


class AvailableBR(str, Enum):
    VALUE_0 = "401"
    VALUE_1 = "402"
    VALUE_2 = "403"
    VALUE_3 = "406"
    VALUE_4 = "407"
    VALUE_5 = "411"
    VALUE_6 = "412"
    VALUE_7 = "415"
    VALUE_8 = "410.1"

    def __str__(self) -> str:
        return str(self.value)
