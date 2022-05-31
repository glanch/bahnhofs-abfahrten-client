from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OEBBSectorInfo")


@attr.s(auto_attribs=True)
class OEBBSectorInfo:
    """
    Attributes:
        scheduled (str):
        reported (Union[Unset, str]):
    """

    scheduled: str
    reported: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        scheduled = self.scheduled
        reported = self.reported

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
        scheduled = d.pop("scheduled")

        reported = d.pop("reported", UNSET)

        oebb_sector_info = cls(
            scheduled=scheduled,
            reported=reported,
        )

        return oebb_sector_info
