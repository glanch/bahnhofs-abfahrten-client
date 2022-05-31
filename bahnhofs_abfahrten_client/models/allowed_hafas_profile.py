from enum import Enum


class AllowedHafasProfile(str, Enum):
    DB = "db"
    OEBB = "oebb"
    BVG = "bvg"
    HVV = "hvv"
    RMV = "rmv"
    SNCB = "sncb"
    AVV = "avv"
    NAHSH = "nahsh"
    INSA = "insa"
    ANACHB = "anachb"
    VAO = "vao"
    SBB = "sbb"
    DBNETZ = "dbnetz"
    PKP = "pkp"
    DBREGIO = "dbregio"
    SMARTRBL = "smartrbl"
    VBN = "vbn"

    def __str__(self) -> str:
        return str(self.value)
