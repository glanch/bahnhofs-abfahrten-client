from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PickSubscrChannelchannelId")


@attr.s(auto_attribs=True)
class PickSubscrChannelchannelId:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        channel_id (str):
    """

    channel_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channelId")

        pick_subscr_channelchannel_id = cls(
            channel_id=channel_id,
        )

        pick_subscr_channelchannel_id.additional_properties = d
        return pick_subscr_channelchannel_id

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
