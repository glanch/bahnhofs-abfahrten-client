from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OEBBTimeFormat")


@attr.s(auto_attribs=True)
class OEBBTimeFormat:
    """
    Attributes:
        days (int):
        hours (int):
        minutes (int):
    """

    days: int
    hours: int
    minutes: int

    def to_dict(self) -> Dict[str, Any]:
        days = self.days
        hours = self.hours
        minutes = self.minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "days": days,
                "hours": hours,
                "minutes": minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days = d.pop("days")

        hours = d.pop("hours")

        minutes = d.pop("minutes")

        oebb_time_format = cls(
            days=days,
            hours=hours,
            minutes=minutes,
        )

        return oebb_time_format
