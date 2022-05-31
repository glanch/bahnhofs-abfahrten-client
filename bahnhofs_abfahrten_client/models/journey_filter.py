from typing import Any, Dict, Type, TypeVar

import attr

from ..models.journey_filter_mode import JourneyFilterMode
from ..models.journey_filter_type import JourneyFilterType

T = TypeVar("T", bound="JourneyFilter")


@attr.s(auto_attribs=True)
class JourneyFilter:
    """
    Attributes:
        mode (JourneyFilterMode):
        type (JourneyFilterType):
        value (str):
    """

    mode: JourneyFilterMode
    type: JourneyFilterType
    value: str

    def to_dict(self) -> Dict[str, Any]:
        mode = self.mode.value

        type = self.type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "mode": mode,
                "type": type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode = JourneyFilterMode(d.pop("mode"))

        type = JourneyFilterType(d.pop("type"))

        value = d.pop("value")

        journey_filter = cls(
            mode=mode,
            type=type,
            value=value,
        )

        return journey_filter
