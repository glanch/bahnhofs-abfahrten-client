from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.subscr_him_event import SubscrHIMEvent
from ..models.subscr_rt_event import SubscrRTEvent

T = TypeVar("T", bound="SubscrEventHistory")


@attr.s(auto_attribs=True)
class SubscrEventHistory:
    """
    Attributes:
        rt_events (List[SubscrRTEvent]):
        him_events (List[SubscrHIMEvent]):
    """

    rt_events: List[SubscrRTEvent]
    him_events: List[SubscrHIMEvent]

    def to_dict(self) -> Dict[str, Any]:
        rt_events = []
        for rt_events_item_data in self.rt_events:
            rt_events_item = rt_events_item_data.to_dict()

            rt_events.append(rt_events_item)

        him_events = []
        for him_events_item_data in self.him_events:
            him_events_item = him_events_item_data.to_dict()

            him_events.append(him_events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "rtEvents": rt_events,
                "himEvents": him_events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rt_events = []
        _rt_events = d.pop("rtEvents")
        for rt_events_item_data in _rt_events:
            rt_events_item = SubscrRTEvent.from_dict(rt_events_item_data)

            rt_events.append(rt_events_item)

        him_events = []
        _him_events = d.pop("himEvents")
        for him_events_item_data in _him_events:
            him_events_item = SubscrHIMEvent.from_dict(him_events_item_data)

            him_events.append(him_events_item)

        subscr_event_history = cls(
            rt_events=rt_events,
            him_events=him_events,
        )

        return subscr_event_history
