from typing import Any, Dict, Type, TypeVar

import attr

from ..models.subscr_user_delete_response_result import SubscrUserDeleteResponseResult

T = TypeVar("T", bound="SubscrUserDeleteResponse")


@attr.s(auto_attribs=True)
class SubscrUserDeleteResponse:
    """
    Attributes:
        result (SubscrUserDeleteResponseResult):
        user_id (str):
    """

    result: SubscrUserDeleteResponseResult
    user_id: str

    def to_dict(self) -> Dict[str, Any]:
        result = self.result.to_dict()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "result": result,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result = SubscrUserDeleteResponseResult.from_dict(d.pop("result"))

        user_id = d.pop("userId")

        subscr_user_delete_response = cls(
            result=result,
            user_id=user_id,
        )

        return subscr_user_delete_response
