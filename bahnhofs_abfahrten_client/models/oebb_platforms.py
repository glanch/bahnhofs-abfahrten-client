from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OEBBPlatforms")


@attr.s(auto_attribs=True)
class OEBBPlatforms:
    """
    Attributes:
        scheduled (int):
        reported (int):
    """

    scheduled: int
    reported: int

    def to_dict(self) -> Dict[str, Any]:
        scheduled = self.scheduled
        reported = self.reported

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "scheduled": scheduled,
                "reported": reported,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheduled = d.pop("scheduled")

        reported = d.pop("reported")

        oebb_platforms = cls(
            scheduled=scheduled,
            reported=reported,
        )

        return oebb_platforms
