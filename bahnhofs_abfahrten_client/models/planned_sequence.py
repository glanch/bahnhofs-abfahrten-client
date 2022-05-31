from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.possible_short import PossibleShort
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlannedSequence")


@attr.s(auto_attribs=True)
class PlannedSequence:
    """
    Attributes:
        raw_type (str):
        type (str):
        short_type (Union[Unset, PossibleShort]):
    """

    raw_type: str
    type: str
    short_type: Union[Unset, PossibleShort] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        raw_type = self.raw_type
        type = self.type
        short_type: Union[Unset, str] = UNSET
        if not isinstance(self.short_type, Unset):
            short_type = self.short_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "rawType": raw_type,
                "type": type,
            }
        )
        if short_type is not UNSET:
            field_dict["shortType"] = short_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raw_type = d.pop("rawType")

        type = d.pop("type")

        _short_type = d.pop("shortType", UNSET)
        short_type: Union[Unset, PossibleShort]
        if isinstance(_short_type, Unset):
            short_type = UNSET
        else:
            short_type = PossibleShort(_short_type)

        planned_sequence = cls(
            raw_type=raw_type,
            type=type,
            short_type=short_type,
        )

        return planned_sequence
