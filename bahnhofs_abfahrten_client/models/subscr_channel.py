from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.subscr_channel_customer_type_option import SubscrChannelCustomerTypeOption
from ..models.subscr_channel_no_sound_option import SubscrChannelNoSoundOption

T = TypeVar("T", bound="SubscrChannel")


@attr.s(auto_attribs=True)
class SubscrChannel:
    """
    Attributes:
        channel_id (str):
        address (str):
        type (str): IPHONE
        options (List[Union[SubscrChannelCustomerTypeOption, SubscrChannelNoSoundOption]]):
        name (str): PUSH_IPHONE
    """

    channel_id: str
    address: str
    type: str
    options: List[Union[SubscrChannelCustomerTypeOption, SubscrChannelNoSoundOption]]
    name: str

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id
        address = self.address
        type = self.type
        options = []
        for options_item_data in self.options:
            if isinstance(options_item_data, SubscrChannelNoSoundOption):
                options_item = options_item_data.to_dict()

            else:
                options_item = options_item_data.to_dict()

            options.append(options_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "channelId": channel_id,
                "address": address,
                "type": type,
                "options": options,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channelId")

        address = d.pop("address")

        type = d.pop("type")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:

            def _parse_options_item(data: object) -> Union[SubscrChannelCustomerTypeOption, SubscrChannelNoSoundOption]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_subscr_channel_option_type_0 = SubscrChannelNoSoundOption.from_dict(data)

                    return componentsschemas_subscr_channel_option_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_subscr_channel_option_type_1 = SubscrChannelCustomerTypeOption.from_dict(data)

                return componentsschemas_subscr_channel_option_type_1

            options_item = _parse_options_item(options_item_data)

            options.append(options_item)

        name = d.pop("name")

        subscr_channel = cls(
            channel_id=channel_id,
            address=address,
            type=type,
            options=options,
            name=name,
        )

        return subscr_channel
