from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.oebb_sector import OEBBSector

T = TypeVar("T", bound="OEBBPlatformInfo")


@attr.s(auto_attribs=True)
class OEBBPlatformInfo:
    """
    Attributes:
        platform (int):
        length (float):
        sectors (List[OEBBSector]):
    """

    platform: int
    length: float
    sectors: List[OEBBSector]

    def to_dict(self) -> Dict[str, Any]:
        platform = self.platform
        length = self.length
        sectors = []
        for sectors_item_data in self.sectors:
            sectors_item = sectors_item_data.to_dict()

            sectors.append(sectors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "platform": platform,
                "length": length,
                "sectors": sectors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        platform = d.pop("platform")

        length = d.pop("length")

        sectors = []
        _sectors = d.pop("sectors")
        for sectors_item_data in _sectors:
            sectors_item = OEBBSector.from_dict(sectors_item_data)

            sectors.append(sectors_item)

        oebb_platform_info = cls(
            platform=platform,
            length=length,
            sectors=sectors,
        )

        return oebb_platform_info
