import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.message_prio import MessagePrio
from ..types import UNSET, Unset

T = TypeVar("T", bound="IrisMessage")


@attr.s(auto_attribs=True)
class IrisMessage:
    """
    Attributes:
        text (str):
        value (float):
        timestamp (Union[Unset, datetime.datetime]):
        superseded (Union[Unset, bool]):
        priority (Union[Unset, MessagePrio]): 1: High; 2: Medium; 3: Low; 4: Done
    """

    text: str
    value: float
    timestamp: Union[Unset, datetime.datetime] = UNSET
    superseded: Union[Unset, bool] = UNSET
    priority: Union[Unset, MessagePrio] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        value = self.value
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        superseded = self.superseded
        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
                "value": value,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if superseded is not UNSET:
            field_dict["superseded"] = superseded
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        value = d.pop("value")

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        superseded = d.pop("superseded", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, MessagePrio]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = MessagePrio(_priority)

        iris_message = cls(
            text=text,
            value=value,
            timestamp=timestamp,
            superseded=superseded,
            priority=priority,
        )

        return iris_message
