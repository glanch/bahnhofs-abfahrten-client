from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OEBBTrainOnPlatform")


@attr.s(auto_attribs=True)
class OEBBTrainOnPlatform:
    """
    Attributes:
        position (float):
        departure_towards_first_sector (bool):
    """

    position: float
    departure_towards_first_sector: bool

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        departure_towards_first_sector = self.departure_towards_first_sector

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "position": position,
                "departureTowardsFirstSector": departure_towards_first_sector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        departure_towards_first_sector = d.pop("departureTowardsFirstSector")

        oebb_train_on_platform = cls(
            position=position,
            departure_towards_first_sector=departure_towards_first_sector,
        )

        return oebb_train_on_platform
