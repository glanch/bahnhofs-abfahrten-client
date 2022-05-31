from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.geo_rect import GeoRect
from ..models.geo_ring import GeoRing
from ..models.him_filter import HimFilter
from ..models.journey_filter import JourneyFilter
from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneyTreeRequestOptions")


@attr.s(auto_attribs=True)
class JourneyTreeRequestOptions:
    """
    Attributes:
        get_childs (Union[Unset, float]):
        get_him (Union[Unset, bool]):
        get_parent (Union[Unset, bool]):
        get_status (Union[Unset, bool]):
        him_fltr_l (Union[Unset, List[HimFilter]]):
        jny_fltr_l (Union[Unset, List[JourneyFilter]]):
        pid (Union[Unset, str]):
        rect (Union[Unset, GeoRect]):
        ring (Union[Unset, GeoRing]):
    """

    get_childs: Union[Unset, float] = UNSET
    get_him: Union[Unset, bool] = UNSET
    get_parent: Union[Unset, bool] = UNSET
    get_status: Union[Unset, bool] = UNSET
    him_fltr_l: Union[Unset, List[HimFilter]] = UNSET
    jny_fltr_l: Union[Unset, List[JourneyFilter]] = UNSET
    pid: Union[Unset, str] = UNSET
    rect: Union[Unset, GeoRect] = UNSET
    ring: Union[Unset, GeoRing] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        get_childs = self.get_childs
        get_him = self.get_him
        get_parent = self.get_parent
        get_status = self.get_status
        him_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.him_fltr_l, Unset):
            him_fltr_l = []
            for him_fltr_l_item_data in self.him_fltr_l:
                him_fltr_l_item = him_fltr_l_item_data.to_dict()

                him_fltr_l.append(him_fltr_l_item)

        jny_fltr_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jny_fltr_l, Unset):
            jny_fltr_l = []
            for jny_fltr_l_item_data in self.jny_fltr_l:
                jny_fltr_l_item = jny_fltr_l_item_data.to_dict()

                jny_fltr_l.append(jny_fltr_l_item)

        pid = self.pid
        rect: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rect, Unset):
            rect = self.rect.to_dict()

        ring: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ring, Unset):
            ring = self.ring.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if get_childs is not UNSET:
            field_dict["getChilds"] = get_childs
        if get_him is not UNSET:
            field_dict["getHIM"] = get_him
        if get_parent is not UNSET:
            field_dict["getParent"] = get_parent
        if get_status is not UNSET:
            field_dict["getStatus"] = get_status
        if him_fltr_l is not UNSET:
            field_dict["himFltrL"] = him_fltr_l
        if jny_fltr_l is not UNSET:
            field_dict["jnyFltrL"] = jny_fltr_l
        if pid is not UNSET:
            field_dict["pid"] = pid
        if rect is not UNSET:
            field_dict["rect"] = rect
        if ring is not UNSET:
            field_dict["ring"] = ring

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_childs = d.pop("getChilds", UNSET)

        get_him = d.pop("getHIM", UNSET)

        get_parent = d.pop("getParent", UNSET)

        get_status = d.pop("getStatus", UNSET)

        him_fltr_l = []
        _him_fltr_l = d.pop("himFltrL", UNSET)
        for him_fltr_l_item_data in _him_fltr_l or []:
            him_fltr_l_item = HimFilter.from_dict(him_fltr_l_item_data)

            him_fltr_l.append(him_fltr_l_item)

        jny_fltr_l = []
        _jny_fltr_l = d.pop("jnyFltrL", UNSET)
        for jny_fltr_l_item_data in _jny_fltr_l or []:
            jny_fltr_l_item = JourneyFilter.from_dict(jny_fltr_l_item_data)

            jny_fltr_l.append(jny_fltr_l_item)

        pid = d.pop("pid", UNSET)

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

        journey_tree_request_options = cls(
            get_childs=get_childs,
            get_him=get_him,
            get_parent=get_parent,
            get_status=get_status,
            him_fltr_l=him_fltr_l,
            jny_fltr_l=jny_fltr_l,
            pid=pid,
            rect=rect,
            ring=ring,
        )

        return journey_tree_request_options
