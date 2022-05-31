from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.journey_filter import JourneyFilter
from ..models.optional_loc_l import OptionalLocL
from ..models.subscr_service_days import SubscrServiceDays
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscrInterval")


@attr.s(auto_attribs=True)
class SubscrInterval:
    """
    Attributes:
        period (float):
        time (str): HHmmSS
        dep_loc (OptionalLocL):
        arr_loc (OptionalLocL):
        monitor_flags (List[str]): ["FTF"] rest unknown
        service_days (SubscrServiceDays):
        jny_fltr_l (Union[Unset, List[JourneyFilter]]):
    """

    period: float
    time: str
    dep_loc: OptionalLocL
    arr_loc: OptionalLocL
    monitor_flags: List[str]
    service_days: SubscrServiceDays
    jny_fltr_l: Union[Unset, List[JourneyFilter]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        period = self.period
        time = self.time
        dep_loc = self.dep_loc.to_dict()

        arr_loc = self.arr_loc.to_dict()

        monitor_flags = self.monitor_flags

        service_days = self.service_days.to_dict()

        jny_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jny_fltr_l, Unset):
            jny_fltr_l = []
            for jny_fltr_l_item_data in self.jny_fltr_l:
                jny_fltr_l_item = jny_fltr_l_item_data.to_dict()

                jny_fltr_l.append(jny_fltr_l_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "period": period,
                "time": time,
                "depLoc": dep_loc,
                "arrLoc": arr_loc,
                "monitorFlags": monitor_flags,
                "serviceDays": service_days,
            }
        )
        if jny_fltr_l is not UNSET:
            field_dict["jnyFltrL"] = jny_fltr_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        period = d.pop("period")

        time = d.pop("time")

        dep_loc = OptionalLocL.from_dict(d.pop("depLoc"))

        arr_loc = OptionalLocL.from_dict(d.pop("arrLoc"))

        monitor_flags = cast(List[str], d.pop("monitorFlags"))

        service_days = SubscrServiceDays.from_dict(d.pop("serviceDays"))

        jny_fltr_l = []
        _jny_fltr_l = d.pop("jnyFltrL", UNSET)
        for jny_fltr_l_item_data in _jny_fltr_l or []:
            jny_fltr_l_item = JourneyFilter.from_dict(jny_fltr_l_item_data)

            jny_fltr_l.append(jny_fltr_l_item)

        subscr_interval = cls(
            period=period,
            time=time,
            dep_loc=dep_loc,
            arr_loc=arr_loc,
            monitor_flags=monitor_flags,
            service_days=service_days,
            jny_fltr_l=jny_fltr_l,
        )

        return subscr_interval
