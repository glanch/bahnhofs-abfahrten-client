from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscrDeleteOptions")


@attr.s(auto_attribs=True)
class SubscrDeleteOptions:
    """
    Attributes:
        user_id (str):
        subscr_id (float):
    """

    user_id: str
    subscr_id: float

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        subscr_id = self.subscr_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userId": user_id,
                "subscrId": subscr_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        subscr_id = d.pop("subscrId")

        subscr_delete_options = cls(
            user_id=user_id,
            subscr_id=subscr_id,
        )

        return subscr_delete_options
