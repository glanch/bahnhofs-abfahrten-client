from enum import Enum


class HimFilterType(str, Enum):
    ADMIN = "ADMIN"
    CAT = "CAT"
    CH = "CH"
    COMP = "COMP"
    DEPT = "DEPT"
    EID = "EID"
    HIMCAT = "HIMCAT"
    HIMID = "HIMID"
    LINE = "LINE"
    OPR = "OPR"
    PID = "PID"
    PROD = "PROD"
    REG = "REG"
    TRAIN = "TRAIN"

    def __str__(self) -> str:
        return str(self.value)
