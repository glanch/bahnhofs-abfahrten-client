from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.txt_c import TxtC

T = TypeVar("T", bound="MsgL")


@attr.s(auto_attribs=True)
class MsgL:
    """
    Attributes:
        type (str):
        rem_x (float):
        txt_c (TxtC):
        prio (float):
        f_idx (float):
        t_idx (float):
        tag_l (List[str]):
    """

    type: str
    rem_x: float
    txt_c: TxtC
    prio: float
    f_idx: float
    t_idx: float
    tag_l: List[str]

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        rem_x = self.rem_x
        txt_c = self.txt_c.to_dict()

        prio = self.prio
        f_idx = self.f_idx
        t_idx = self.t_idx
        tag_l = self.tag_l

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "remX": rem_x,
                "txtC": txt_c,
                "prio": prio,
                "fIdx": f_idx,
                "tIdx": t_idx,
                "tagL": tag_l,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        rem_x = d.pop("remX")

        txt_c = TxtC.from_dict(d.pop("txtC"))

        prio = d.pop("prio")

        f_idx = d.pop("fIdx")

        t_idx = d.pop("tIdx")

        tag_l = cast(List[str], d.pop("tagL"))

        msg_l = cls(
            type=type,
            rem_x=rem_x,
            txt_c=txt_c,
            prio=prio,
            f_idx=f_idx,
            t_idx=t_idx,
            tag_l=tag_l,
        )

        return msg_l
