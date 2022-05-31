from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.journey_filter import JourneyFilter
from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneyGraphRequestOptions")


@attr.s(auto_attribs=True)
class JourneyGraphRequestOptions:
    """
    Attributes:
        date (Union[Unset, str]): yyyyMMdd
        get_passlist (Union[Unset, bool]):
        get_product_start_end_info (Union[Unset, bool]):
        jny_fltr_l (Union[Unset, List[JourneyFilter]]):
    """

    date: Union[Unset, str] = UNSET
    get_passlist: Union[Unset, bool] = UNSET
    get_product_start_end_info: Union[Unset, bool] = UNSET
    jny_fltr_l: Union[Unset, List[JourneyFilter]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        get_passlist = self.get_passlist
        get_product_start_end_info = self.get_product_start_end_info
        jny_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jny_fltr_l, Unset):
            jny_fltr_l = []
            for jny_fltr_l_item_data in self.jny_fltr_l:
                jny_fltr_l_item = jny_fltr_l_item_data.to_dict()

                jny_fltr_l.append(jny_fltr_l_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if get_passlist is not UNSET:
            field_dict["getPasslist"] = get_passlist
        if get_product_start_end_info is not UNSET:
            field_dict["getProductStartEndInfo"] = get_product_start_end_info
        if jny_fltr_l is not UNSET:
            field_dict["jnyFltrL"] = jny_fltr_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        get_passlist = d.pop("getPasslist", UNSET)

        get_product_start_end_info = d.pop("getProductStartEndInfo", UNSET)

        jny_fltr_l = []
        _jny_fltr_l = d.pop("jnyFltrL", UNSET)
        for jny_fltr_l_item_data in _jny_fltr_l or []:
            jny_fltr_l_item = JourneyFilter.from_dict(jny_fltr_l_item_data)

            jny_fltr_l.append(jny_fltr_l_item)

        journey_graph_request_options = cls(
            date=date,
            get_passlist=get_passlist,
            get_product_start_end_info=get_product_start_end_info,
            jny_fltr_l=jny_fltr_l,
        )

        return journey_graph_request_options
