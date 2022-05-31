from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_stop import CommonStop
from ..models.freq import Freq
from ..models.msg_l import MsgL
from ..models.trn_cmp_sx import TrnCmpSX
from ..types import UNSET, Unset

T = TypeVar("T", bound="Jny")


@attr.s(auto_attribs=True)
class Jny:
    """
    Attributes:
        jid (str):
        prod_x (float):
        dir_txt (str):
        status (str):
        is_rchbl (bool):
        subscr (str):
        ctx_recon (str):
        d_trn_cmp_s_xmsg_l (List[MsgL]):
        freq (Freq):
        is_cncl (Union[Unset, bool]):
        is_part_cncl (Union[Unset, bool]):
        stop_l (Union[Unset, List[CommonStop]]):
        msg_l (Union[Unset, List[MsgL]]):
        chg_dur_r (Union[Unset, float]):
        d_trn_cmp_sx (Union[Unset, TrnCmpSX]):
    """

    jid: str
    prod_x: float
    dir_txt: str
    status: str
    is_rchbl: bool
    subscr: str
    ctx_recon: str
    d_trn_cmp_s_xmsg_l: List[MsgL]
    freq: Freq
    is_cncl: Union[Unset, bool] = UNSET
    is_part_cncl: Union[Unset, bool] = UNSET
    stop_l: Union[Unset, List[CommonStop]] = UNSET
    msg_l: Union[Unset, List[MsgL]] = UNSET
    chg_dur_r: Union[Unset, float] = UNSET
    d_trn_cmp_sx: Union[Unset, TrnCmpSX] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        jid = self.jid
        prod_x = self.prod_x
        dir_txt = self.dir_txt
        status = self.status
        is_rchbl = self.is_rchbl
        subscr = self.subscr
        ctx_recon = self.ctx_recon
        d_trn_cmp_s_xmsg_l = []
        for d_trn_cmp_s_xmsg_l_item_data in self.d_trn_cmp_s_xmsg_l:
            d_trn_cmp_s_xmsg_l_item = d_trn_cmp_s_xmsg_l_item_data.to_dict()

            d_trn_cmp_s_xmsg_l.append(d_trn_cmp_s_xmsg_l_item)

        freq = self.freq.to_dict()

        is_cncl = self.is_cncl
        is_part_cncl = self.is_part_cncl
        stop_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stop_l, Unset):
            stop_l = []
            for stop_l_item_data in self.stop_l:
                stop_l_item = stop_l_item_data.to_dict()

                stop_l.append(stop_l_item)

        msg_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.msg_l, Unset):
            msg_l = []
            for msg_l_item_data in self.msg_l:
                msg_l_item = msg_l_item_data.to_dict()

                msg_l.append(msg_l_item)

        chg_dur_r = self.chg_dur_r
        d_trn_cmp_sx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.d_trn_cmp_sx, Unset):
            d_trn_cmp_sx = self.d_trn_cmp_sx.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "jid": jid,
                "prodX": prod_x,
                "dirTxt": dir_txt,
                "status": status,
                "isRchbl": is_rchbl,
                "subscr": subscr,
                "ctxRecon": ctx_recon,
                "dTrnCmpSXmsgL": d_trn_cmp_s_xmsg_l,
                "freq": freq,
            }
        )
        if is_cncl is not UNSET:
            field_dict["isCncl"] = is_cncl
        if is_part_cncl is not UNSET:
            field_dict["isPartCncl"] = is_part_cncl
        if stop_l is not UNSET:
            field_dict["stopL"] = stop_l
        if msg_l is not UNSET:
            field_dict["msgL"] = msg_l
        if chg_dur_r is not UNSET:
            field_dict["chgDurR"] = chg_dur_r
        if d_trn_cmp_sx is not UNSET:
            field_dict["dTrnCmpSX"] = d_trn_cmp_sx

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

        ctx_recon = d.pop("ctxRecon")

        d_trn_cmp_s_xmsg_l = []
        _d_trn_cmp_s_xmsg_l = d.pop("dTrnCmpSXmsgL")
        for d_trn_cmp_s_xmsg_l_item_data in _d_trn_cmp_s_xmsg_l:
            d_trn_cmp_s_xmsg_l_item = MsgL.from_dict(d_trn_cmp_s_xmsg_l_item_data)

            d_trn_cmp_s_xmsg_l.append(d_trn_cmp_s_xmsg_l_item)

        freq = Freq.from_dict(d.pop("freq"))

        is_cncl = d.pop("isCncl", UNSET)

        is_part_cncl = d.pop("isPartCncl", UNSET)

        stop_l = []
        _stop_l = d.pop("stopL", UNSET)
        for stop_l_item_data in _stop_l or []:
            stop_l_item = CommonStop.from_dict(stop_l_item_data)

            stop_l.append(stop_l_item)

        msg_l = []
        _msg_l = d.pop("msgL", UNSET)
        for msg_l_item_data in _msg_l or []:
            msg_l_item = MsgL.from_dict(msg_l_item_data)

            msg_l.append(msg_l_item)

        chg_dur_r = d.pop("chgDurR", UNSET)

        _d_trn_cmp_sx = d.pop("dTrnCmpSX", UNSET)
        d_trn_cmp_sx: Union[Unset, TrnCmpSX]
        if isinstance(_d_trn_cmp_sx, Unset):
            d_trn_cmp_sx = UNSET
        else:
            d_trn_cmp_sx = TrnCmpSX.from_dict(_d_trn_cmp_sx)

        jny = cls(
            jid=jid,
            prod_x=prod_x,
            dir_txt=dir_txt,
            status=status,
            is_rchbl=is_rchbl,
            subscr=subscr,
            ctx_recon=ctx_recon,
            d_trn_cmp_s_xmsg_l=d_trn_cmp_s_xmsg_l,
            freq=freq,
            is_cncl=is_cncl,
            is_part_cncl=is_part_cncl,
            stop_l=stop_l,
            msg_l=msg_l,
            chg_dur_r=chg_dur_r,
            d_trn_cmp_sx=d_trn_cmp_sx,
        )

        return jny
