from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.oebb_time_format import OEBBTimeFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="OEBBTime")


@attr.s(auto_attribs=True)
class OEBBTime:
    """
    Attributes:
        scheduled (OEBBTimeFormat):
        reported (Union[Unset, OEBBTimeFormat]):
    """

    scheduled: OEBBTimeFormat
    reported: Union[Unset, OEBBTimeFormat] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        scheduled = self.scheduled.to_dict()

        reported: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reported, Unset):
            reported = self.reported.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "scheduled": scheduled,
            }
        )
        if reported is not UNSET:
            field_dict["reported"] = reported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheduled = OEBBTimeFormat.from_dict(d.pop("scheduled"))

        _reported = d.pop("reported", UNSET)
        reported: Union[Unset, OEBBTimeFormat]
        if isinstance(_reported, Unset):
            reported = UNSET
        else:
            reported = OEBBTimeFormat.from_dict(_reported)

        oebb_time = cls(
            scheduled=scheduled,
            reported=reported,
        )

        return oebb_time
