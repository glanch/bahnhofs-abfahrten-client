from typing import Any, Dict, Type, TypeVar

import attr

from ..models.subscr_channel_no_sound_option_type import SubscrChannelNoSoundOptionType
from ..models.subscr_channel_no_sound_option_value import SubscrChannelNoSoundOptionValue

T = TypeVar("T", bound="SubscrChannelNoSoundOption")


@attr.s(auto_attribs=True)
class SubscrChannelNoSoundOption:
    """
    Attributes:
        type (SubscrChannelNoSoundOptionType):
        value (SubscrChannelNoSoundOptionValue):
    """

    type: SubscrChannelNoSoundOptionType
    value: SubscrChannelNoSoundOptionValue

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SubscrChannelNoSoundOptionType(d.pop("type"))

        value = SubscrChannelNoSoundOptionValue(d.pop("value"))

        subscr_channel_no_sound_option = cls(
            type=type,
            value=value,
        )

        return subscr_channel_no_sound_option
