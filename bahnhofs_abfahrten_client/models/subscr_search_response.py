from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.subscr_search_response_intvl_subscr_l_item import SubscrSearchResponseIntvlSubscrLItem
from ..models.subscr_search_response_result import SubscrSearchResponseResult

T = TypeVar("T", bound="SubscrSearchResponse")


@attr.s(auto_attribs=True)
class SubscrSearchResponse:
    """
    Attributes:
        result (SubscrSearchResponseResult):
        user_id (str):
        intvl_subscr_l (List[SubscrSearchResponseIntvlSubscrLItem]):
    """

    result: SubscrSearchResponseResult
    user_id: str
    intvl_subscr_l: List[SubscrSearchResponseIntvlSubscrLItem]

    def to_dict(self) -> Dict[str, Any]:
        result = self.result.to_dict()

        user_id = self.user_id
        intvl_subscr_l = []
        for intvl_subscr_l_item_data in self.intvl_subscr_l:
            intvl_subscr_l_item = intvl_subscr_l_item_data.to_dict()

            intvl_subscr_l.append(intvl_subscr_l_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "result": result,
                "userId": user_id,
                "intvlSubscrL": intvl_subscr_l,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result = SubscrSearchResponseResult.from_dict(d.pop("result"))

        user_id = d.pop("userId")

        intvl_subscr_l = []
        _intvl_subscr_l = d.pop("intvlSubscrL")
        for intvl_subscr_l_item_data in _intvl_subscr_l:
            intvl_subscr_l_item = SubscrSearchResponseIntvlSubscrLItem.from_dict(intvl_subscr_l_item_data)

            intvl_subscr_l.append(intvl_subscr_l_item)

        subscr_search_response = cls(
            result=result,
            user_id=user_id,
            intvl_subscr_l=intvl_subscr_l,
        )

        return subscr_search_response
