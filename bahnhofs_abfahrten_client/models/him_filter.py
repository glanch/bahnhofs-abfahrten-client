from typing import Any, Dict, Type, TypeVar

import attr

from ..models.him_filter_mode import HimFilterMode
from ..models.him_filter_type import HimFilterType

T = TypeVar("T", bound="HimFilter")


@attr.s(auto_attribs=True)
class HimFilter:
    """
    Attributes:
        mode (HimFilterMode):
        type (HimFilterType):
        value (str):
    """

    mode: HimFilterMode
    type: HimFilterType
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
        mode = HimFilterMode(d.pop("mode"))

        type = HimFilterType(d.pop("type"))

        value = d.pop("value")

        him_filter = cls(
            mode=mode,
            type=type,
            value=value,
        )

        return him_filter
