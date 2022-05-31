import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WalkStopInfo")


@attr.s(auto_attribs=True)
class WalkStopInfo:
    """
    Attributes:
        time (datetime.datetime):
        delay (Union[Unset, float]):
    """

    time: datetime.datetime
    delay: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time.isoformat()

        delay = self.delay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = isoparse(d.pop("time"))

        delay = d.pop("delay", UNSET)

        walk_stop_info = cls(
            time=time,
            delay=delay,
        )

        walk_stop_info.additional_properties = d
        return walk_stop_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
