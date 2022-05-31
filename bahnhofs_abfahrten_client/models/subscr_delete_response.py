from typing import Any, Dict, Type, TypeVar

import attr

from ..models.subscr_delete_response_result import SubscrDeleteResponseResult

T = TypeVar("T", bound="SubscrDeleteResponse")


@attr.s(auto_attribs=True)
class SubscrDeleteResponse:
    """
    Attributes:
        result (SubscrDeleteResponseResult):
        user_id (str):
        subscr_id (str):
    """

    result: SubscrDeleteResponseResult
    user_id: str
    subscr_id: str

    def to_dict(self) -> Dict[str, Any]:
        result = self.result.to_dict()

        user_id = self.user_id
        subscr_id = self.subscr_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "result": result,
                "userId": user_id,
                "subscrId": subscr_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result = SubscrDeleteResponseResult.from_dict(d.pop("result"))

        user_id = d.pop("userId")

        subscr_id = d.pop("subscrId")

        subscr_delete_response = cls(
            result=result,
            user_id=user_id,
            subscr_id=subscr_id,
        )

        return subscr_delete_response
