from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.him_filter import HimFilter
from ..models.optional_loc_l import OptionalLocL
from ..types import UNSET, Unset

T = TypeVar("T", bound="HimSearchRequestOptions")


@attr.s(auto_attribs=True)
class HimSearchRequestOptions:
    """
    Attributes:
        comp (Union[Unset, str]):
        daily_b (Union[Unset, str]):
        daily_e (Union[Unset, str]):
        date_b (Union[Unset, str]):
        date_e (Union[Unset, str]):
        dept (Union[Unset, str]):
        dir_loc (Union[Unset, OptionalLocL]):
        him_fltr_l (Union[Unset, List[HimFilter]]):
        max_num (Union[Unset, float]):
        only_him_id (Union[Unset, bool]):
        only_today (Union[Unset, bool]):
        st_loc (Union[Unset, OptionalLocL]):
        time_b (Union[Unset, str]):
        time_e (Union[Unset, str]):
    """

    comp: Union[Unset, str] = UNSET
    daily_b: Union[Unset, str] = UNSET
    daily_e: Union[Unset, str] = UNSET
    date_b: Union[Unset, str] = UNSET
    date_e: Union[Unset, str] = UNSET
    dept: Union[Unset, str] = UNSET
    dir_loc: Union[Unset, OptionalLocL] = UNSET
    him_fltr_l: Union[Unset, List[HimFilter]] = UNSET
    max_num: Union[Unset, float] = UNSET
    only_him_id: Union[Unset, bool] = UNSET
    only_today: Union[Unset, bool] = UNSET
    st_loc: Union[Unset, OptionalLocL] = UNSET
    time_b: Union[Unset, str] = UNSET
    time_e: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        comp = self.comp
        daily_b = self.daily_b
        daily_e = self.daily_e
        date_b = self.date_b
        date_e = self.date_e
        dept = self.dept
        dir_loc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dir_loc, Unset):
            dir_loc = self.dir_loc.to_dict()

        him_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.him_fltr_l, Unset):
            him_fltr_l = []
            for him_fltr_l_item_data in self.him_fltr_l:
                him_fltr_l_item = him_fltr_l_item_data.to_dict()

                him_fltr_l.append(him_fltr_l_item)

        max_num = self.max_num
        only_him_id = self.only_him_id
        only_today = self.only_today
        st_loc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.st_loc, Unset):
            st_loc = self.st_loc.to_dict()

        time_b = self.time_b
        time_e = self.time_e

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if comp is not UNSET:
            field_dict["comp"] = comp
        if daily_b is not UNSET:
            field_dict["dailyB"] = daily_b
        if daily_e is not UNSET:
            field_dict["dailyE"] = daily_e
        if date_b is not UNSET:
            field_dict["dateB"] = date_b
        if date_e is not UNSET:
            field_dict["dateE"] = date_e
        if dept is not UNSET:
            field_dict["dept"] = dept
        if dir_loc is not UNSET:
            field_dict["dirLoc"] = dir_loc
        if him_fltr_l is not UNSET:
            field_dict["himFltrL"] = him_fltr_l
        if max_num is not UNSET:
            field_dict["maxNum"] = max_num
        if only_him_id is not UNSET:
            field_dict["onlyHimId"] = only_him_id
        if only_today is not UNSET:
            field_dict["onlyToday"] = only_today
        if st_loc is not UNSET:
            field_dict["stLoc"] = st_loc
        if time_b is not UNSET:
            field_dict["timeB"] = time_b
        if time_e is not UNSET:
            field_dict["timeE"] = time_e

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comp = d.pop("comp", UNSET)

        daily_b = d.pop("dailyB", UNSET)

        daily_e = d.pop("dailyE", UNSET)

        date_b = d.pop("dateB", UNSET)

        date_e = d.pop("dateE", UNSET)

        dept = d.pop("dept", UNSET)

        _dir_loc = d.pop("dirLoc", UNSET)
        dir_loc: Union[Unset, OptionalLocL]
        if isinstance(_dir_loc, Unset):
            dir_loc = UNSET
        else:
            dir_loc = OptionalLocL.from_dict(_dir_loc)

        him_fltr_l = []
        _him_fltr_l = d.pop("himFltrL", UNSET)
        for him_fltr_l_item_data in _him_fltr_l or []:
            him_fltr_l_item = HimFilter.from_dict(him_fltr_l_item_data)

            him_fltr_l.append(him_fltr_l_item)

        max_num = d.pop("maxNum", UNSET)

        only_him_id = d.pop("onlyHimId", UNSET)

        only_today = d.pop("onlyToday", UNSET)

        _st_loc = d.pop("stLoc", UNSET)
        st_loc: Union[Unset, OptionalLocL]
        if isinstance(_st_loc, Unset):
            st_loc = UNSET
        else:
            st_loc = OptionalLocL.from_dict(_st_loc)

        time_b = d.pop("timeB", UNSET)

        time_e = d.pop("timeE", UNSET)

        him_search_request_options = cls(
            comp=comp,
            daily_b=daily_b,
            daily_e=daily_e,
            date_b=date_b,
            date_e=date_e,
            dept=dept,
            dir_loc=dir_loc,
            him_fltr_l=him_fltr_l,
            max_num=max_num,
            only_him_id=only_him_id,
            only_today=only_today,
            st_loc=st_loc,
            time_b=time_b,
            time_e=time_e,
        )

        return him_search_request_options
