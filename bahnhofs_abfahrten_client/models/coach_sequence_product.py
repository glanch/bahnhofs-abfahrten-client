from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoachSequenceProduct")


@attr.s(auto_attribs=True)
class CoachSequenceProduct:
    """
    Attributes:
        number (str):
        type (str):
        line (Union[Unset, str]):
    """

    number: str
    type: str
    line: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        type = self.type
        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "number": number,
                "type": type,
            }
        )
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number")

        type = d.pop("type")

        line = d.pop("line", UNSET)

        coach_sequence_product = cls(
            number=number,
            type=type,
            line=line,
        )

        return coach_sequence_product
