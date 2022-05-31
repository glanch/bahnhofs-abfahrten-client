from enum import Enum


class OEBBAccessType(str, Enum):
    STIEGENAUFGANG = "STIEGENAUFGANG"
    AUFZUG = "AUFZUG"
    ROLLTREPPE = "ROLLTREPPE"

    def __str__(self) -> str:
        return str(self.value)
