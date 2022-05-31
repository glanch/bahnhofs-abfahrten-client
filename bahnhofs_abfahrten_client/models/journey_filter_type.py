from enum import Enum


class JourneyFilterType(str, Enum):
    ADM = "ADM"
    ATTRF = "ATTRF"
    ATTRJ = "ATTRJ"
    ATTRL = "ATTRL"
    BC = "BC"
    CAT = "CAT"
    COUCH = "COUCH"
    CTX_RECON = "CTX_RECON"
    GROUP = "GROUP"
    INFOTEXTS = "INFOTEXTS"
    JID = "JID"
    LID = "LID"
    LINE = "LINE"
    LINEID = "LINEID"
    META = "META"
    NAME = "NAME"
    NUM = "NUM"
    OP = "OP"
    PID = "PID"
    PROD = "PROD"
    ROUTE = "ROUTE"
    SLEEP = "SLEEP"
    STATIONS = "STATIONS"
    UIC = "UIC"

    def __str__(self) -> str:
        return str(self.value)
