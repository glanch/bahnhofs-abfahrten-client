import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.rem_l import RemL
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonStopInfo")


@attr.s(auto_attribs=True)
class CommonStopInfo:
    """
    Attributes:
        scheduled_time (datetime.datetime): scheduled time for this stop
        time (datetime.datetime): best known time for this stop, might be identical to scheduledTime
        scheduled_platform (Union[Unset, str]): Scheduled Platform
        platform (Union[Unset, str]): Best known platform, might be identical to scheduledPlatform
        delay (Union[Unset, int]):
        reihung (Union[Unset, bool]):
        messages (Union[Unset, List[RemL]]):
        cancelled (Union[Unset, bool]):
    """

    scheduled_time: datetime.datetime
    time: datetime.datetime
    scheduled_platform: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    delay: Union[Unset, int] = UNSET
    reihung: Union[Unset, bool] = UNSET
    messages: Union[Unset, List[RemL]] = UNSET
    cancelled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        scheduled_time = self.scheduled_time.isoformat()

        time = self.time.isoformat()

        scheduled_platform = self.scheduled_platform
        platform = self.platform
        delay = self.delay
        reihung = self.reihung
        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        cancelled = self.cancelled

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "scheduledTime": scheduled_time,
                "time": time,
            }
        )
        if scheduled_platform is not UNSET:
            field_dict["scheduledPlatform"] = scheduled_platform
        if platform is not UNSET:
            field_dict["platform"] = platform
        if delay is not UNSET:
            field_dict["delay"] = delay
        if reihung is not UNSET:
            field_dict["reihung"] = reihung
        if messages is not UNSET:
            field_dict["messages"] = messages
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scheduled_time = isoparse(d.pop("scheduledTime"))

        time = isoparse(d.pop("time"))

        scheduled_platform = d.pop("scheduledPlatform", UNSET)

        platform = d.pop("platform", UNSET)

        delay = d.pop("delay", UNSET)

        reihung = d.pop("reihung", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = RemL.from_dict(messages_item_data)

            messages.append(messages_item)

        cancelled = d.pop("cancelled", UNSET)

        common_stop_info = cls(
            scheduled_time=scheduled_time,
            time=time,
            scheduled_platform=scheduled_platform,
            platform=platform,
            delay=delay,
            reihung=reihung,
            messages=messages,
            cancelled=cancelled,
        )

        return common_stop_info
