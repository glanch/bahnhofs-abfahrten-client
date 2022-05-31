from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrnCmpSX")


@attr.s(auto_attribs=True)
class TrnCmpSX:
    """
    Attributes:
        tcoc_x (Union[Unset, List[float]]):
        tc_m (Union[Unset, float]):
    """

    tcoc_x: Union[Unset, List[float]] = UNSET
    tc_m: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tcoc_x: Union[Unset, List[float]] = UNSET
        if not isinstance(self.tcoc_x, Unset):
            tcoc_x = self.tcoc_x

        tc_m = self.tc_m

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tcoc_x is not UNSET:
            field_dict["tcocX"] = tcoc_x
        if tc_m is not UNSET:
            field_dict["tcM"] = tc_m

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tcoc_x = cast(List[float], d.pop("tcocX", UNSET))

        tc_m = d.pop("tcM", UNSET)

        trn_cmp_sx = cls(
            tcoc_x=tcoc_x,
            tc_m=tc_m,
        )

        return trn_cmp_sx
