from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.jny_cl import JnyCl
from ..models.trip_search_traveler import TripSearchTraveler

T = TypeVar("T", bound="TripSearchTarifRequest")


@attr.s(auto_attribs=True)
class TripSearchTarifRequest:
    """
    Attributes:
        class_ (JnyCl):
        traveler (List[TripSearchTraveler]):
    """

    class_: JnyCl
    traveler: List[TripSearchTraveler]

    def to_dict(self) -> Dict[str, Any]:
        class_ = self.class_.value

        traveler = []
        for traveler_item_data in self.traveler:
            traveler_item = traveler_item_data.to_dict()

            traveler.append(traveler_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "class": class_,
                "traveler": traveler,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        class_ = JnyCl(d.pop("class"))

        traveler = []
        _traveler = d.pop("traveler")
        for traveler_item_data in _traveler:
            traveler_item = TripSearchTraveler.from_dict(traveler_item_data)

            traveler.append(traveler_item)

        trip_search_tarif_request = cls(
            class_=class_,
            traveler=traveler,
        )

        return trip_search_tarif_request
