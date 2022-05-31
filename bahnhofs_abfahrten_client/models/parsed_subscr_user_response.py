from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ParsedSubscrUserResponse")


@attr.s(auto_attribs=True)
class ParsedSubscrUserResponse:
    """
    Attributes:
        user_id (str):
    """

    user_id: str

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        parsed_subscr_user_response = cls(
            user_id=user_id,
        )

        return parsed_subscr_user_response
