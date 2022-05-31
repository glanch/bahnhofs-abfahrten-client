from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.geo_rect import GeoRect
from ..models.geo_ring import GeoRing
from ..models.in_out_mode import InOutMode
from ..models.journey_filter import JourneyFilter
from ..models.journey_train_pos_mode import JourneyTrainPosMode
from ..models.optional_loc_l import OptionalLocL
from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneyGeoPosRequestOptions")


@attr.s(auto_attribs=True)
class JourneyGeoPosRequestOptions:
    """
    Attributes:
        age_of_report (Union[Unset, bool]):
        date (Union[Unset, str]):
        time (Union[Unset, str]):
        get_simple_train_composition (Union[Unset, bool]):
        get_unmatched (Union[Unset, bool]):
        in_out (Union[Unset, InOutMode]):
        jny_fltr_l (Union[Unset, List[JourneyFilter]]):
        loc_l (Union[Unset, List[OptionalLocL]]):
        max_jny (Union[Unset, bool]):
        only_rt (Union[Unset, bool]):
        per_size (Union[Unset, float]):
        per_step (Union[Unset, float]):
        rect (Union[Unset, GeoRect]):
        ring (Union[Unset, GeoRing]):
        rt_msg_status (Union[Unset, bool]):
        train_pos_mode (Union[Unset, JourneyTrainPosMode]):
        zoom (Union[Unset, float]):
    """

    age_of_report: Union[Unset, bool] = UNSET
    date: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    get_simple_train_composition: Union[Unset, bool] = UNSET
    get_unmatched: Union[Unset, bool] = UNSET
    in_out: Union[Unset, InOutMode] = UNSET
    jny_fltr_l: Union[Unset, List[JourneyFilter]] = UNSET
    loc_l: Union[Unset, List[OptionalLocL]] = UNSET
    max_jny: Union[Unset, bool] = UNSET
    only_rt: Union[Unset, bool] = UNSET
    per_size: Union[Unset, float] = UNSET
    per_step: Union[Unset, float] = UNSET
    rect: Union[Unset, GeoRect] = UNSET
    ring: Union[Unset, GeoRing] = UNSET
    rt_msg_status: Union[Unset, bool] = UNSET
    train_pos_mode: Union[Unset, JourneyTrainPosMode] = UNSET
    zoom: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        age_of_report = self.age_of_report
        date = self.date
        time = self.time
        get_simple_train_composition = self.get_simple_train_composition
        get_unmatched = self.get_unmatched
        in_out: Union[Unset, str] = UNSET
        if not isinstance(self.in_out, Unset):
            in_out = self.in_out.value

        jny_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jny_fltr_l, Unset):
            jny_fltr_l = []
            for jny_fltr_l_item_data in self.jny_fltr_l:
                jny_fltr_l_item = jny_fltr_l_item_data.to_dict()

                jny_fltr_l.append(jny_fltr_l_item)

        loc_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.loc_l, Unset):
            loc_l = []
            for loc_l_item_data in self.loc_l:
                loc_l_item = loc_l_item_data.to_dict()

                loc_l.append(loc_l_item)

        max_jny = self.max_jny
        only_rt = self.only_rt
        per_size = self.per_size
        per_step = self.per_step
        rect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rect, Unset):
            rect = self.rect.to_dict()

        ring: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ring, Unset):
            ring = self.ring.to_dict()

        rt_msg_status = self.rt_msg_status
        train_pos_mode: Union[Unset, str] = UNSET
        if not isinstance(self.train_pos_mode, Unset):
            train_pos_mode = self.train_pos_mode.value

        zoom = self.zoom

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if age_of_report is not UNSET:
            field_dict["ageOfReport"] = age_of_report
        if date is not UNSET:
            field_dict["date"] = date
        if time is not UNSET:
            field_dict["time"] = time
        if get_simple_train_composition is not UNSET:
            field_dict["getSimpleTrainComposition"] = get_simple_train_composition
        if get_unmatched is not UNSET:
            field_dict["getUnmatched"] = get_unmatched
        if in_out is not UNSET:
            field_dict["inOut"] = in_out
        if jny_fltr_l is not UNSET:
            field_dict["jnyFltrL"] = jny_fltr_l
        if loc_l is not UNSET:
            field_dict["locL"] = loc_l
        if max_jny is not UNSET:
            field_dict["maxJny"] = max_jny
        if only_rt is not UNSET:
            field_dict["onlyRT"] = only_rt
        if per_size is not UNSET:
            field_dict["perSize"] = per_size
        if per_step is not UNSET:
            field_dict["perStep"] = per_step
        if rect is not UNSET:
            field_dict["rect"] = rect
        if ring is not UNSET:
            field_dict["ring"] = ring
        if rt_msg_status is not UNSET:
            field_dict["rtMsgStatus"] = rt_msg_status
        if train_pos_mode is not UNSET:
            field_dict["trainPosMode"] = train_pos_mode
        if zoom is not UNSET:
            field_dict["zoom"] = zoom

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        age_of_report = d.pop("ageOfReport", UNSET)

        date = d.pop("date", UNSET)

        time = d.pop("time", UNSET)

        get_simple_train_composition = d.pop("getSimpleTrainComposition", UNSET)

        get_unmatched = d.pop("getUnmatched", UNSET)

        _in_out = d.pop("inOut", UNSET)
        in_out: Union[Unset, InOutMode]
        if isinstance(_in_out, Unset):
            in_out = UNSET
        else:
            in_out = InOutMode(_in_out)

        jny_fltr_l = []
        _jny_fltr_l = d.pop("jnyFltrL", UNSET)
        for jny_fltr_l_item_data in _jny_fltr_l or []:
            jny_fltr_l_item = JourneyFilter.from_dict(jny_fltr_l_item_data)

            jny_fltr_l.append(jny_fltr_l_item)

        loc_l = []
        _loc_l = d.pop("locL", UNSET)
        for loc_l_item_data in _loc_l or []:
            loc_l_item = OptionalLocL.from_dict(loc_l_item_data)

            loc_l.append(loc_l_item)

        max_jny = d.pop("maxJny", UNSET)

        only_rt = d.pop("onlyRT", UNSET)

        per_size = d.pop("perSize", UNSET)

        per_step = d.pop("perStep", UNSET)

        _rect = d.pop("rect", UNSET)
        rect: Union[Unset, GeoRect]
        if isinstance(_rect, Unset):
            rect = UNSET
        else:
            rect = GeoRect.from_dict(_rect)

        _ring = d.pop("ring", UNSET)
        ring: Union[Unset, GeoRing]
        if isinstance(_ring, Unset):
            ring = UNSET
        else:
            ring = GeoRing.from_dict(_ring)

        rt_msg_status = d.pop("rtMsgStatus", UNSET)

        _train_pos_mode = d.pop("trainPosMode", UNSET)
        train_pos_mode: Union[Unset, JourneyTrainPosMode]
        if isinstance(_train_pos_mode, Unset):
            train_pos_mode = UNSET
        else:
            train_pos_mode = JourneyTrainPosMode(_train_pos_mode)

        zoom = d.pop("zoom", UNSET)

        journey_geo_pos_request_options = cls(
            age_of_report=age_of_report,
            date=date,
            time=time,
            get_simple_train_composition=get_simple_train_composition,
            get_unmatched=get_unmatched,
            in_out=in_out,
            jny_fltr_l=jny_fltr_l,
            loc_l=loc_l,
            max_jny=max_jny,
            only_rt=only_rt,
            per_size=per_size,
            per_step=per_step,
            rect=rect,
            ring=ring,
            rt_msg_status=rt_msg_status,
            train_pos_mode=train_pos_mode,
            zoom=zoom,
        )

        return journey_geo_pos_request_options
