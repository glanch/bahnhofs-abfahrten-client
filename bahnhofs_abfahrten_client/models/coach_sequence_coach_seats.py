from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoachSequenceCoachSeats")


@attr.s(auto_attribs=True)
class CoachSequenceCoachSeats:
    """
    Attributes:
        comfort (Union[Unset, str]):
        disabled (Union[Unset, str]):
        family (Union[Unset, str]):
    """

    comfort: Union[Unset, str] = UNSET
    disabled: Union[Unset, str] = UNSET
    family: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        comfort = self.comfort
        disabled = self.disabled
        family = self.family

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if comfort is not UNSET:
            field_dict["comfort"] = comfort
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if family is not UNSET:
            field_dict["family"] = family

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comfort = d.pop("comfort", UNSET)

        disabled = d.pop("disabled", UNSET)

        family = d.pop("family", UNSET)

        coach_sequence_coach_seats = cls(
            comfort=comfort,
            disabled=disabled,
            family=family,
        )

        return coach_sequence_coach_seats
