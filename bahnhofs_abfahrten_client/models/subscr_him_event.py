from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscrHIMEvent")


@attr.s(auto_attribs=True)
class SubscrHIMEvent:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        subscr_him_event = cls()

        return subscr_him_event
