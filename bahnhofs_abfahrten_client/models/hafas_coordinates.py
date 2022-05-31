from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="HafasCoordinates")


@attr.s(auto_attribs=True)
class HafasCoordinates:
    """
    Attributes:
        lat (float):
        lng (float):
    """

    lat: float
    lng: float

    def to_dict(self) -> Dict[str, Any]:
        lat = self.lat
        lng = self.lng

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "lat": lat,
                "lng": lng,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lat = d.pop("lat")

        lng = d.pop("lng")

        hafas_coordinates = cls(
            lat=lat,
            lng=lng,
        )

        return hafas_coordinates
