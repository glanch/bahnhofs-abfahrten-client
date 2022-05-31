from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_stop import CommonStop
from ..models.msg_l import MsgL
from ..types import UNSET, Unset

T = TypeVar("T", bound="JnyL")


@attr.s(auto_attribs=True)
class JnyL:
    """
    Attributes:
        jid (str):
        prod_x (float):
        dir_txt (str):
        status (str):
        is_rchbl (bool):
        subscr (str):
        stop_l (List[CommonStop]):
        is_cncl (Union[Unset, bool]):
        is_part_cncl (Union[Unset, bool]):
        msg_l (Union[Unset, List[MsgL]]):
    """

    jid: str
    prod_x: float
    dir_txt: str
    status: str
    is_rchbl: bool
    subscr: str
    stop_l: List[CommonStop]
    is_cncl: Union[Unset, bool] = UNSET
    is_part_cncl: Union[Unset, bool] = UNSET
    msg_l: Union[Unset, List[MsgL]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        jid = self.jid
        prod_x = self.prod_x
        dir_txt = self.dir_txt
        status = self.status
        is_rchbl = self.is_rchbl
        subscr = self.subscr
        stop_l = []
        for stop_l_item_data in self.stop_l:
            stop_l_item = stop_l_item_data.to_dict()

            stop_l.append(stop_l_item)

        is_cncl = self.is_cncl
        is_part_cncl = self.is_part_cncl
        msg_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.msg_l, Unset):
            msg_l = []
            for msg_l_item_data in self.msg_l:
                msg_l_item = msg_l_item_data.to_dict()

                msg_l.append(msg_l_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "jid": jid,
                "prodX": prod_x,
                "dirTxt": dir_txt,
                "status": status,
                "isRchbl": is_rchbl,
                "subscr": subscr,
                "stopL": stop_l,
            }
        )
        if is_cncl is not UNSET:
            field_dict["isCncl"] = is_cncl
        if is_part_cncl is not UNSET:
            field_dict["isPartCncl"] = is_part_cncl
        if msg_l is not UNSET:
            field_dict["msgL"] = msg_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        jid = d.pop("jid")

        prod_x = d.pop("prodX")

        dir_txt = d.pop("dirTxt")

        status = d.pop("status")

        is_rchbl = d.pop("isRchbl")

        subscr = d.pop("subscr")

        stop_l = []
        _stop_l = d.pop("stopL")
        for stop_l_item_data in _stop_l:
            stop_l_item = CommonStop.from_dict(stop_l_item_data)

            stop_l.append(stop_l_item)

        is_cncl = d.pop("isCncl", UNSET)

        is_part_cncl = d.pop("isPartCncl", UNSET)

        msg_l = []
        _msg_l = d.pop("msgL", UNSET)
        for msg_l_item_data in _msg_l or []:
            msg_l_item = MsgL.from_dict(msg_l_item_data)

            msg_l.append(msg_l_item)

        jny_l = cls(
            jid=jid,
            prod_x=prod_x,
            dir_txt=dir_txt,
            status=status,
            is_rchbl=is_rchbl,
            subscr=subscr,
            stop_l=stop_l,
            is_cncl=is_cncl,
            is_part_cncl=is_part_cncl,
            msg_l=msg_l,
        )

        return jny_l
