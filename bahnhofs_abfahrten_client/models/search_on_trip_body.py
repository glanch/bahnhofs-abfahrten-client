from typing import Any, Dict, Type, TypeVar

import attr

from ..models.allowed_sot_mode import AllowedSotMode

T = TypeVar("T", bound="SearchOnTripBody")


@attr.s(auto_attribs=True)
class SearchOnTripBody:
    """
    Attributes:
        sot_mode (AllowedSotMode):
        id (str):
    """

    sot_mode: AllowedSotMode
    id: str

    def to_dict(self) -> Dict[str, Any]:
        sot_mode = self.sot_mode.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sotMode": sot_mode,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sot_mode = AllowedSotMode(d.pop("sotMode"))

        id = d.pop("id")

        search_on_trip_body = cls(
            sot_mode=sot_mode,
            id=id,
        )

        return search_on_trip_body
