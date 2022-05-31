from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Coordinate2D")


@attr.s(auto_attribs=True)
class Coordinate2D:
    """2D coordinate within geo reference system.

    Attributes:
        longitude (float): Longitude position in reference system.
        latitude (float): Latitude position in reference system.
    """

    longitude: float
    latitude: float

    def to_dict(self) -> Dict[str, Any]:
        longitude = self.longitude
        latitude = self.latitude

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "longitude": longitude,
                "latitude": latitude,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        longitude = d.pop("longitude")

        latitude = d.pop("latitude")

        coordinate_2d = cls(
            longitude=longitude,
            latitude=latitude,
        )

        return coordinate_2d
