from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemL")


@attr.s(auto_attribs=True)
class RemL:
    """
    Attributes:
        type (str):
        code (str):
        ico_x (float):
        txt_n (str):
        txt_s (Union[Unset, str]):
        prio (Union[Unset, float]):
        s_idx (Union[Unset, float]):
    """

    type: str
    code: str
    ico_x: float
    txt_n: str
    txt_s: Union[Unset, str] = UNSET
    prio: Union[Unset, float] = UNSET
    s_idx: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        code = self.code
        ico_x = self.ico_x
        txt_n = self.txt_n
        txt_s = self.txt_s
        prio = self.prio
        s_idx = self.s_idx

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "code": code,
                "icoX": ico_x,
                "txtN": txt_n,
            }
        )
        if txt_s is not UNSET:
            field_dict["txtS"] = txt_s
        if prio is not UNSET:
            field_dict["prio"] = prio
        if s_idx is not UNSET:
            field_dict["sIdx"] = s_idx

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        code = d.pop("code")

        ico_x = d.pop("icoX")

        txt_n = d.pop("txtN")

        txt_s = d.pop("txtS", UNSET)

        prio = d.pop("prio", UNSET)

        s_idx = d.pop("sIdx", UNSET)

        rem_l = cls(
            type=type,
            code=code,
            ico_x=ico_x,
            txt_n=txt_n,
            txt_s=txt_s,
            prio=prio,
            s_idx=s_idx,
        )

        return rem_l
