from typing import Any, Dict, Type, TypeVar

import attr

from ..models.oebb_access_type import OEBBAccessType

T = TypeVar("T", bound="OEBBAccess")


@attr.s(auto_attribs=True)
class OEBBAccess:
    """
    Attributes:
        platform (str):
        distance (float):
        name (str):
        type (OEBBAccessType):
    """

    platform: str
    distance: float
    name: str
    type: OEBBAccessType

    def to_dict(self) -> Dict[str, Any]:
        platform = self.platform
        distance = self.distance
        name = self.name
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "platform": platform,
                "distance": distance,
                "name": name,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        platform = d.pop("platform")

        distance = d.pop("distance")

        name = d.pop("name")

        type = OEBBAccessType(d.pop("type"))

        oebb_access = cls(
            platform=platform,
            distance=distance,
            name=name,
            type=type,
        )

        return oebb_access
