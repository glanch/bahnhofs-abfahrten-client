from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pick_subscr_channelchannel_id import PickSubscrChannelchannelId
from ..models.subscr_interval import SubscrInterval

T = TypeVar("T", bound="SubscrCreateOptions")


@attr.s(auto_attribs=True)
class SubscrCreateOptions:
    """
    Attributes:
        user_id (str):
        channels (List[PickSubscrChannelchannelId]):
        intvl_subscr (SubscrInterval):
    """

    user_id: str
    channels: List[PickSubscrChannelchannelId]
    intvl_subscr: SubscrInterval

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()

            channels.append(channels_item)

        intvl_subscr = self.intvl_subscr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userId": user_id,
                "channels": channels,
                "intvlSubscr": intvl_subscr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = PickSubscrChannelchannelId.from_dict(channels_item_data)

            channels.append(channels_item)

        intvl_subscr = SubscrInterval.from_dict(d.pop("intvlSubscr"))

        subscr_create_options = cls(
            user_id=user_id,
            channels=channels,
            intvl_subscr=intvl_subscr,
        )

        return subscr_create_options
