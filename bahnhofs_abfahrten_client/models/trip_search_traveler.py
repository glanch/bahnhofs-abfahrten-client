from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.loyality_card import LoyalityCard
from ..models.traveler_type import TravelerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TripSearchTraveler")


@attr.s(auto_attribs=True)
class TripSearchTraveler:
    """
    Attributes:
        type (TravelerType):
        loyality_card (Union[Unset, LoyalityCard]):
    """

    type: TravelerType
    loyality_card: Union[Unset, LoyalityCard] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        loyality_card: Union[Unset, str] = UNSET
        if not isinstance(self.loyality_card, Unset):
            loyality_card = self.loyality_card.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if loyality_card is not UNSET:
            field_dict["loyalityCard"] = loyality_card

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = TravelerType(d.pop("type"))

        _loyality_card = d.pop("loyalityCard", UNSET)
        loyality_card: Union[Unset, LoyalityCard]
        if isinstance(_loyality_card, Unset):
            loyality_card = UNSET
        else:
            loyality_card = LoyalityCard(_loyality_card)

        trip_search_traveler = cls(
            type=type,
            loyality_card=loyality_card,
        )

        return trip_search_traveler
