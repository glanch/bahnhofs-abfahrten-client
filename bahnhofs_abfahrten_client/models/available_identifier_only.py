from enum import Enum


class AvailableIdentifierOnly(str, Enum):
    VALUE_0 = "401.LDV"
    VALUE_1 = "401.9"
    VALUE_2 = "411.S1"
    VALUE_3 = "411.S2"
    VALUE_4 = "412.7"
    VALUE_5 = "412.13"
    VALUE_6 = "403.R"
    VALUE_7 = "403.S1"
    VALUE_8 = "403.S2"
    VALUE_9 = "406.R"
    IC2TWIN = "IC2.TWIN"
    IC2KISS = "IC2.KISS"
    MET = "MET"
    TGV = "TGV"

    def __str__(self) -> str:
        return str(self.value)
