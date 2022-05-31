from enum import Enum


class LoyalityCard(str, Enum):
    BC25FIRST = "BC25First"
    BC25SECOND = "BC25Second"
    BC50FIRST = "BC50First"
    BC50SECOND = "BC50Second"
    SHCARD = "SHCard"
    ATVORTEILSCARD = "ATVorteilscard"
    CHGENERAL = "CHGeneral"
    CHHALFWITHRAILPLUS = "CHHalfWithRailplus"
    CHHALFWITHOUTRAILPLUS = "CHHalfWithoutRailplus"
    NLWITHRAILPLUS = "NLWithRailplus"
    NLWITHOUTRAILPLUS = "NLWithoutRailplus"
    BC100FIRST = "BC100First"
    BC100SECOND = "BC100Second"

    def __str__(self) -> str:
        return str(self.value)
