from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.coach_sequence_baureihe import CoachSequenceBaureihe
from ..models.coach_sequence_coach import CoachSequenceCoach
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoachSequenceGroup")


@attr.s(auto_attribs=True)
class CoachSequenceGroup:
    """
    Attributes:
        coaches (List[CoachSequenceCoach]):
        name (str):
        origin_name (str):
        destination_name (str):
        number (str):
        train_name (Union[Unset, str]):
        baureihe (Union[Unset, CoachSequenceBaureihe]):
    """

    coaches: List[CoachSequenceCoach]
    name: str
    origin_name: str
    destination_name: str
    number: str
    train_name: Union[Unset, str] = UNSET
    baureihe: Union[Unset, CoachSequenceBaureihe] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        coaches = []
        for coaches_item_data in self.coaches:
            coaches_item = coaches_item_data.to_dict()

            coaches.append(coaches_item)

        name = self.name
        origin_name = self.origin_name
        destination_name = self.destination_name
        number = self.number
        train_name = self.train_name
        baureihe: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baureihe, Unset):
            baureihe = self.baureihe.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "coaches": coaches,
                "name": name,
                "originName": origin_name,
                "destinationName": destination_name,
                "number": number,
            }
        )
        if train_name is not UNSET:
            field_dict["trainName"] = train_name
        if baureihe is not UNSET:
            field_dict["baureihe"] = baureihe

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        coaches = []
        _coaches = d.pop("coaches")
        for coaches_item_data in _coaches:
            coaches_item = CoachSequenceCoach.from_dict(coaches_item_data)

            coaches.append(coaches_item)

        name = d.pop("name")

        origin_name = d.pop("originName")

        destination_name = d.pop("destinationName")

        number = d.pop("number")

        train_name = d.pop("trainName", UNSET)

        _baureihe = d.pop("baureihe", UNSET)
        baureihe: Union[Unset, CoachSequenceBaureihe]
        if isinstance(_baureihe, Unset):
            baureihe = UNSET
        else:
            baureihe = CoachSequenceBaureihe.from_dict(_baureihe)

        coach_sequence_group = cls(
            coaches=coaches,
            name=name,
            origin_name=origin_name,
            destination_name=destination_name,
            number=number,
            train_name=train_name,
            baureihe=baureihe,
        )

        return coach_sequence_group
