from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CoachSequencePosition")


@attr.s(auto_attribs=True)
class CoachSequencePosition:
    """
    Attributes:
        start_percent (float):
        end_percent (float):
    """

    start_percent: float
    end_percent: float

    def to_dict(self) -> Dict[str, Any]:
        start_percent = self.start_percent
        end_percent = self.end_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "startPercent": start_percent,
                "endPercent": end_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_percent = d.pop("startPercent")

        end_percent = d.pop("endPercent")

        coach_sequence_position = cls(
            start_percent=start_percent,
            end_percent=end_percent,
        )

        return coach_sequence_position
