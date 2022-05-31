from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.route_tarif_fare import RouteTarifFare

T = TypeVar("T", bound="RouteTarifFareSet")


@attr.s(auto_attribs=True)
class RouteTarifFareSet:
    """
    Attributes:
        fares (List[RouteTarifFare]):
    """

    fares: List[RouteTarifFare]

    def to_dict(self) -> Dict[str, Any]:
        fares = []
        for fares_item_data in self.fares:
            fares_item = fares_item_data.to_dict()

            fares.append(fares_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "fares": fares,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fares = []
        _fares = d.pop("fares")
        for fares_item_data in _fares:
            fares_item = RouteTarifFare.from_dict(fares_item_data)

            fares.append(fares_item)

        route_tarif_fare_set = cls(
            fares=fares,
        )

        return route_tarif_fare_set
