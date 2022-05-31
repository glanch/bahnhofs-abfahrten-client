from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.wing_info import WingInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="WingDefinition")


@attr.s(auto_attribs=True)
class WingDefinition:
    """
    Attributes:
        start (Union[Unset, WingInfo]):
        end (Union[Unset, WingInfo]):
    """

    start: Union[Unset, WingInfo] = UNSET
    end: Union[Unset, WingInfo] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start = d.pop("start", UNSET)
        start: Union[Unset, WingInfo]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = WingInfo.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, WingInfo]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = WingInfo.from_dict(_end)

        wing_definition = cls(
            start=start,
            end=end,
        )

        return wing_definition
