from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OEBBSector")


@attr.s(auto_attribs=True)
class OEBBSector:
    """
    Attributes:
        name (str):
        length (float):
    """

    name: str
    length: float

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        length = self.length

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "length": length,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        length = d.pop("length")

        oebb_sector = cls(
            name=name,
            length=length,
        )

        return oebb_sector
