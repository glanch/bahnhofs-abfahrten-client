from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.subscr_channel import SubscrChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscrUserCreateOptions")


@attr.s(auto_attribs=True)
class SubscrUserCreateOptions:
    """
    Attributes:
        user_id (str):
        channels (List[SubscrChannel]):
        language (Union[Unset, str]): de
    """

    user_id: str
    channels: List[SubscrChannel]
    language: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()

            channels.append(channels_item)

        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userId": user_id,
                "channels": channels,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = SubscrChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        language = d.pop("language", UNSET)

        subscr_user_create_options = cls(
            user_id=user_id,
            channels=channels,
            language=language,
        )

        return subscr_user_create_options
