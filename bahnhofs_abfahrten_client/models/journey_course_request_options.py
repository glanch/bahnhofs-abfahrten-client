from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.hafas_direction import HafasDirection
from ..models.journey_filter import JourneyFilter
from ..models.optional_loc_l import OptionalLocL
from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneyCourseRequestOptions")


@attr.s(auto_attribs=True)
class JourneyCourseRequestOptions:
    """
    Attributes:
        date (str): yyyyMMdd
        jid (str):
        arr_loc (Union[Unset, OptionalLocL]):
        dep_loc (Union[Unset, OptionalLocL]):
        dir_ (Union[Unset, HafasDirection]):
        get_edge_ani (Union[Unset, bool]):
        get_edge_course (Union[Unset, bool]):
        get_ist (Union[Unset, bool]):
        get_main_ani (Union[Unset, bool]):
        get_main_course (Union[Unset, bool]):
        get_pass_loc (Union[Unset, bool]):
        get_polyline (Union[Unset, bool]):
        jny_fltr_l (Union[Unset, List[JourneyFilter]]):
        per_size (Union[Unset, float]):
        per_step (Union[Unset, float]):
        time (Union[Unset, str]): HHmm
    """

    date: str
    jid: str
    arr_loc: Union[Unset, OptionalLocL] = UNSET
    dep_loc: Union[Unset, OptionalLocL] = UNSET
    dir_: Union[Unset, HafasDirection] = UNSET
    get_edge_ani: Union[Unset, bool] = UNSET
    get_edge_course: Union[Unset, bool] = UNSET
    get_ist: Union[Unset, bool] = UNSET
    get_main_ani: Union[Unset, bool] = UNSET
    get_main_course: Union[Unset, bool] = UNSET
    get_pass_loc: Union[Unset, bool] = UNSET
    get_polyline: Union[Unset, bool] = UNSET
    jny_fltr_l: Union[Unset, List[JourneyFilter]] = UNSET
    per_size: Union[Unset, float] = UNSET
    per_step: Union[Unset, float] = UNSET
    time: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        jid = self.jid
        arr_loc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arr_loc, Unset):
            arr_loc = self.arr_loc.to_dict()

        dep_loc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dep_loc, Unset):
            dep_loc = self.dep_loc.to_dict()

        dir_: Union[Unset, str] = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_.value

        get_edge_ani = self.get_edge_ani
        get_edge_course = self.get_edge_course
        get_ist = self.get_ist
        get_main_ani = self.get_main_ani
        get_main_course = self.get_main_course
        get_pass_loc = self.get_pass_loc
        get_polyline = self.get_polyline
        jny_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jny_fltr_l, Unset):
            jny_fltr_l = []
            for jny_fltr_l_item_data in self.jny_fltr_l:
                jny_fltr_l_item = jny_fltr_l_item_data.to_dict()

                jny_fltr_l.append(jny_fltr_l_item)

        per_size = self.per_size
        per_step = self.per_step
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "date": date,
                "jid": jid,
            }
        )
        if arr_loc is not UNSET:
            field_dict["arrLoc"] = arr_loc
        if dep_loc is not UNSET:
            field_dict["depLoc"] = dep_loc
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if get_edge_ani is not UNSET:
            field_dict["getEdgeAni"] = get_edge_ani
        if get_edge_course is not UNSET:
            field_dict["getEdgeCourse"] = get_edge_course
        if get_ist is not UNSET:
            field_dict["getIST"] = get_ist
        if get_main_ani is not UNSET:
            field_dict["getMainAni"] = get_main_ani
        if get_main_course is not UNSET:
            field_dict["getMainCourse"] = get_main_course
        if get_pass_loc is not UNSET:
            field_dict["getPassLoc"] = get_pass_loc
        if get_polyline is not UNSET:
            field_dict["getPolyline"] = get_polyline
        if jny_fltr_l is not UNSET:
            field_dict["jnyFltrL"] = jny_fltr_l
        if per_size is not UNSET:
            field_dict["perSize"] = per_size
        if per_step is not UNSET:
            field_dict["perStep"] = per_step
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        jid = d.pop("jid")

        _arr_loc = d.pop("arrLoc", UNSET)
        arr_loc: Union[Unset, OptionalLocL]
        if isinstance(_arr_loc, Unset):
            arr_loc = UNSET
        else:
            arr_loc = OptionalLocL.from_dict(_arr_loc)

        _dep_loc = d.pop("depLoc", UNSET)
        dep_loc: Union[Unset, OptionalLocL]
        if isinstance(_dep_loc, Unset):
            dep_loc = UNSET
        else:
            dep_loc = OptionalLocL.from_dict(_dep_loc)

        _dir_ = d.pop("dir", UNSET)
        dir_: Union[Unset, HafasDirection]
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = HafasDirection(_dir_)

        get_edge_ani = d.pop("getEdgeAni", UNSET)

        get_edge_course = d.pop("getEdgeCourse", UNSET)

        get_ist = d.pop("getIST", UNSET)

        get_main_ani = d.pop("getMainAni", UNSET)

        get_main_course = d.pop("getMainCourse", UNSET)

        get_pass_loc = d.pop("getPassLoc", UNSET)

        get_polyline = d.pop("getPolyline", UNSET)

        jny_fltr_l = []
        _jny_fltr_l = d.pop("jnyFltrL", UNSET)
        for jny_fltr_l_item_data in _jny_fltr_l or []:
            jny_fltr_l_item = JourneyFilter.from_dict(jny_fltr_l_item_data)

            jny_fltr_l.append(jny_fltr_l_item)

        per_size = d.pop("perSize", UNSET)

        per_step = d.pop("perStep", UNSET)

        time = d.pop("time", UNSET)

        journey_course_request_options = cls(
            date=date,
            jid=jid,
            arr_loc=arr_loc,
            dep_loc=dep_loc,
            dir_=dir_,
            get_edge_ani=get_edge_ani,
            get_edge_course=get_edge_course,
            get_ist=get_ist,
            get_main_ani=get_main_ani,
            get_main_course=get_main_course,
            get_pass_loc=get_pass_loc,
            get_polyline=get_polyline,
            jny_fltr_l=jny_fltr_l,
            per_size=per_size,
            per_step=per_step,
            time=time,
        )

        return journey_course_request_options
