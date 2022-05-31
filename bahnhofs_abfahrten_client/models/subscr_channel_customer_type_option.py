from typing import Any, Dict, Type, TypeVar

import attr

from ..models.subscr_channel_customer_type_option_type import SubscrChannelCustomerTypeOptionType

T = TypeVar("T", bound="SubscrChannelCustomerTypeOption")


@attr.s(auto_attribs=True)
class SubscrChannelCustomerTypeOption:
    """
    Attributes:
        type (SubscrChannelCustomerTypeOptionType):
        value (str):
    """

    type: SubscrChannelCustomerTypeOptionType
    value: str

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        value = self.value

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
        type = SubscrChannelCustomerTypeOptionType(d.pop("type"))

        value = d.pop("value")

        subscr_channel_customer_type_option = cls(
            type=type,
            value=value,
        )

        return subscr_channel_customer_type_option
