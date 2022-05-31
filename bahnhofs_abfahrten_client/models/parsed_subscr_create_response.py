from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ParsedSubscrCreateResponse")


@attr.s(auto_attribs=True)
class ParsedSubscrCreateResponse:
    """
    Attributes:
        subscription_id (float):
    """

    subscription_id: float

    def to_dict(self) -> Dict[str, Any]:
        subscription_id = self.subscription_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "subscriptionId": subscription_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_id = d.pop("subscriptionId")

        parsed_subscr_create_response = cls(
            subscription_id=subscription_id,
        )

        return parsed_subscr_create_response
