from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.msg_l import MsgL
from ..models.trn_cmp_sx import TrnCmpSX
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonStop")


@attr.s(auto_attribs=True)
class CommonStop:
    """
    Attributes:
        loc_x (float):
        a_out_r (bool):
        a_time_s (str):
        d_in_s (bool):
        d_in_r (bool):
        d_time_s (str):
        idx (Union[Unset, float]):
        a_cncl (Union[Unset, bool]):
        a_prod_x (Union[Unset, float]):
        a_time_r (Union[Unset, str]):
        a_platf_s (Union[Unset, str]):
        a_platf_r (Union[Unset, str]):
        a_prog_type (Union[Unset, str]):
        type (Union[Unset, str]):
        a_tz_offset (Union[Unset, float]):
        a_trn_cmp_sx (Union[Unset, TrnCmpSX]):
        msg_l (Union[Unset, List[MsgL]]):
        d_cncl (Union[Unset, bool]):
        d_prod_x (Union[Unset, float]):
        d_time_r (Union[Unset, str]):
        d_platf_s (Union[Unset, str]):
        d_platf_r (Union[Unset, str]):
        d_prog_type (Union[Unset, str]):
        d_tz_offset (Union[Unset, float]):
        d_trn_cmp_sx (Union[Unset, TrnCmpSX]):
        is_add (Union[Unset, bool]):
    """

    loc_x: float
    a_out_r: bool
    a_time_s: str
    d_in_s: bool
    d_in_r: bool
    d_time_s: str
    idx: Union[Unset, float] = UNSET
    a_cncl: Union[Unset, bool] = UNSET
    a_prod_x: Union[Unset, float] = UNSET
    a_time_r: Union[Unset, str] = UNSET
    a_platf_s: Union[Unset, str] = UNSET
    a_platf_r: Union[Unset, str] = UNSET
    a_prog_type: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    a_tz_offset: Union[Unset, float] = UNSET
    a_trn_cmp_sx: Union[Unset, TrnCmpSX] = UNSET
    msg_l: Union[Unset, List[MsgL]] = UNSET
    d_cncl: Union[Unset, bool] = UNSET
    d_prod_x: Union[Unset, float] = UNSET
    d_time_r: Union[Unset, str] = UNSET
    d_platf_s: Union[Unset, str] = UNSET
    d_platf_r: Union[Unset, str] = UNSET
    d_prog_type: Union[Unset, str] = UNSET
    d_tz_offset: Union[Unset, float] = UNSET
    d_trn_cmp_sx: Union[Unset, TrnCmpSX] = UNSET
    is_add: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        loc_x = self.loc_x
        a_out_r = self.a_out_r
        a_time_s = self.a_time_s
        d_in_s = self.d_in_s
        d_in_r = self.d_in_r
        d_time_s = self.d_time_s
        idx = self.idx
        a_cncl = self.a_cncl
        a_prod_x = self.a_prod_x
        a_time_r = self.a_time_r
        a_platf_s = self.a_platf_s
        a_platf_r = self.a_platf_r
        a_prog_type = self.a_prog_type
        type = self.type
        a_tz_offset = self.a_tz_offset
        a_trn_cmp_sx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.a_trn_cmp_sx, Unset):
            a_trn_cmp_sx = self.a_trn_cmp_sx.to_dict()

        msg_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.msg_l, Unset):
            msg_l = []
            for msg_l_item_data in self.msg_l:
                msg_l_item = msg_l_item_data.to_dict()

                msg_l.append(msg_l_item)

        d_cncl = self.d_cncl
        d_prod_x = self.d_prod_x
        d_time_r = self.d_time_r
        d_platf_s = self.d_platf_s
        d_platf_r = self.d_platf_r
        d_prog_type = self.d_prog_type
        d_tz_offset = self.d_tz_offset
        d_trn_cmp_sx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.d_trn_cmp_sx, Unset):
            d_trn_cmp_sx = self.d_trn_cmp_sx.to_dict()

        is_add = self.is_add

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "locX": loc_x,
                "aOutR": a_out_r,
                "aTimeS": a_time_s,
                "dInS": d_in_s,
                "dInR": d_in_r,
                "dTimeS": d_time_s,
            }
        )
        if idx is not UNSET:
            field_dict["idx"] = idx
        if a_cncl is not UNSET:
            field_dict["aCncl"] = a_cncl
        if a_prod_x is not UNSET:
            field_dict["aProdX"] = a_prod_x
        if a_time_r is not UNSET:
            field_dict["aTimeR"] = a_time_r
        if a_platf_s is not UNSET:
            field_dict["aPlatfS"] = a_platf_s
        if a_platf_r is not UNSET:
            field_dict["aPlatfR"] = a_platf_r
        if a_prog_type is not UNSET:
            field_dict["aProgType"] = a_prog_type
        if type is not UNSET:
            field_dict["type"] = type
        if a_tz_offset is not UNSET:
            field_dict["aTZOffset"] = a_tz_offset
        if a_trn_cmp_sx is not UNSET:
            field_dict["aTrnCmpSX"] = a_trn_cmp_sx
        if msg_l is not UNSET:
            field_dict["msgL"] = msg_l
        if d_cncl is not UNSET:
            field_dict["dCncl"] = d_cncl
        if d_prod_x is not UNSET:
            field_dict["dProdX"] = d_prod_x
        if d_time_r is not UNSET:
            field_dict["dTimeR"] = d_time_r
        if d_platf_s is not UNSET:
            field_dict["dPlatfS"] = d_platf_s
        if d_platf_r is not UNSET:
            field_dict["dPlatfR"] = d_platf_r
        if d_prog_type is not UNSET:
            field_dict["dProgType"] = d_prog_type
        if d_tz_offset is not UNSET:
            field_dict["dTZOffset"] = d_tz_offset
        if d_trn_cmp_sx is not UNSET:
            field_dict["dTrnCmpSX"] = d_trn_cmp_sx
        if is_add is not UNSET:
            field_dict["isAdd"] = is_add

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        loc_x = d.pop("locX")

        a_out_r = d.pop("aOutR")

        a_time_s = d.pop("aTimeS")

        d_in_s = d.pop("dInS")

        d_in_r = d.pop("dInR")

        d_time_s = d.pop("dTimeS")

        idx = d.pop("idx", UNSET)

        a_cncl = d.pop("aCncl", UNSET)

        a_prod_x = d.pop("aProdX", UNSET)

        a_time_r = d.pop("aTimeR", UNSET)

        a_platf_s = d.pop("aPlatfS", UNSET)

        a_platf_r = d.pop("aPlatfR", UNSET)

        a_prog_type = d.pop("aProgType", UNSET)

        type = d.pop("type", UNSET)

        a_tz_offset = d.pop("aTZOffset", UNSET)

        _a_trn_cmp_sx = d.pop("aTrnCmpSX", UNSET)
        a_trn_cmp_sx: Union[Unset, TrnCmpSX]
        if isinstance(_a_trn_cmp_sx, Unset):
            a_trn_cmp_sx = UNSET
        else:
            a_trn_cmp_sx = TrnCmpSX.from_dict(_a_trn_cmp_sx)

        msg_l = []
        _msg_l = d.pop("msgL", UNSET)
        for msg_l_item_data in _msg_l or []:
            msg_l_item = MsgL.from_dict(msg_l_item_data)

            msg_l.append(msg_l_item)

        d_cncl = d.pop("dCncl", UNSET)

        d_prod_x = d.pop("dProdX", UNSET)

        d_time_r = d.pop("dTimeR", UNSET)

        d_platf_s = d.pop("dPlatfS", UNSET)

        d_platf_r = d.pop("dPlatfR", UNSET)

        d_prog_type = d.pop("dProgType", UNSET)

        d_tz_offset = d.pop("dTZOffset", UNSET)

        _d_trn_cmp_sx = d.pop("dTrnCmpSX", UNSET)
        d_trn_cmp_sx: Union[Unset, TrnCmpSX]
        if isinstance(_d_trn_cmp_sx, Unset):
            d_trn_cmp_sx = UNSET
        else:
            d_trn_cmp_sx = TrnCmpSX.from_dict(_d_trn_cmp_sx)

        is_add = d.pop("isAdd", UNSET)

        common_stop = cls(
            loc_x=loc_x,
            a_out_r=a_out_r,
            a_time_s=a_time_s,
            d_in_s=d_in_s,
            d_in_r=d_in_r,
            d_time_s=d_time_s,
            idx=idx,
            a_cncl=a_cncl,
            a_prod_x=a_prod_x,
            a_time_r=a_time_r,
            a_platf_s=a_platf_s,
            a_platf_r=a_platf_r,
            a_prog_type=a_prog_type,
            type=type,
            a_tz_offset=a_tz_offset,
            a_trn_cmp_sx=a_trn_cmp_sx,
            msg_l=msg_l,
            d_cncl=d_cncl,
            d_prod_x=d_prod_x,
            d_time_r=d_time_r,
            d_platf_s=d_platf_s,
            d_platf_r=d_platf_r,
            d_prog_type=d_prog_type,
            d_tz_offset=d_tz_offset,
            d_trn_cmp_sx=d_trn_cmp_sx,
            is_add=is_add,
        )

        return common_stop
