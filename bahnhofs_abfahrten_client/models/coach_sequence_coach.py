from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.coach_sequence_coach_class import CoachSequenceCoachClass
from ..models.coach_sequence_coach_features import CoachSequenceCoachFeatures
from ..models.coach_sequence_coach_seats import CoachSequenceCoachSeats
from ..models.coach_sequence_position import CoachSequencePosition
from ..models.fahrzeug_kategorie import FahrzeugKategorie
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoachSequenceCoach")


@attr.s(auto_attribs=True)
class CoachSequenceCoach:
    """
    Attributes:
        class_ (CoachSequenceCoachClass): 0: Unknown; 1: erste; 2: zweite; 3: 1&2; 4: Not for passengers
        category (FahrzeugKategorie):
        position (CoachSequencePosition):
        features (CoachSequenceCoachFeatures):
        closed (Union[Unset, bool]):
        uic (Union[Unset, str]): only filled for real time information
        type (Union[Unset, str]):
        identification_number (Union[Unset, str]): Wagenordnungsnummer
        seats (Union[Unset, CoachSequenceCoachSeats]):
    """

    class_: CoachSequenceCoachClass
    category: FahrzeugKategorie
    position: CoachSequencePosition
    features: CoachSequenceCoachFeatures
    closed: Union[Unset, bool] = UNSET
    uic: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    identification_number: Union[Unset, str] = UNSET
    seats: Union[Unset, CoachSequenceCoachSeats] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        class_ = self.class_.value

        category = self.category.value

        position = self.position.to_dict()

        features = self.features.to_dict()

        closed = self.closed
        uic = self.uic
        type = self.type
        identification_number = self.identification_number
        seats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seats, Unset):
            seats = self.seats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "class": class_,
                "category": category,
                "position": position,
                "features": features,
            }
        )
        if closed is not UNSET:
            field_dict["closed"] = closed
        if uic is not UNSET:
            field_dict["uic"] = uic
        if type is not UNSET:
            field_dict["type"] = type
        if identification_number is not UNSET:
            field_dict["identificationNumber"] = identification_number
        if seats is not UNSET:
            field_dict["seats"] = seats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        class_ = CoachSequenceCoachClass(d.pop("class"))

        category = FahrzeugKategorie(d.pop("category"))

        position = CoachSequencePosition.from_dict(d.pop("position"))

        features = CoachSequenceCoachFeatures.from_dict(d.pop("features"))

        closed = d.pop("closed", UNSET)

        uic = d.pop("uic", UNSET)

        type = d.pop("type", UNSET)

        identification_number = d.pop("identificationNumber", UNSET)

        _seats = d.pop("seats", UNSET)
        seats: Union[Unset, CoachSequenceCoachSeats]
        if isinstance(_seats, Unset):
            seats = UNSET
        else:
            seats = CoachSequenceCoachSeats.from_dict(_seats)

        coach_sequence_coach = cls(
            class_=class_,
            category=category,
            position=position,
            features=features,
            closed=closed,
            uic=uic,
            type=type,
            identification_number=identification_number,
            seats=seats,
        )

        return coach_sequence_coach
