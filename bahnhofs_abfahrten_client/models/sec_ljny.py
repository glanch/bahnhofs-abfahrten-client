from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_arrival import CommonArrival
from ..models.common_departure import CommonDeparture
from ..models.jny import Jny
from ..models.sec_ljny_res_state import SecLJNYResState
from ..models.sec_ljny_type import SecLJNYType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecLJNY")


@attr.s(auto_attribs=True)
class SecLJNY:
    """
    Attributes:
        type (SecLJNYType):
        ico_x (float):
        dep (CommonDeparture):
        arr (CommonArrival):
        jny (Jny):
        res_state (SecLJNYResState):
        res_recommendation (str):
        par_jny_l (Union[Unset, List[Jny]]):
    """

    type: SecLJNYType
    ico_x: float
    dep: CommonDeparture
    arr: CommonArrival
    jny: Jny
    res_state: SecLJNYResState
    res_recommendation: str
    par_jny_l: Union[Unset, List[Jny]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        ico_x = self.ico_x
        dep = self.dep.to_dict()

        arr = self.arr.to_dict()

        jny = self.jny.to_dict()

        res_state = self.res_state.value

        res_recommendation = self.res_recommendation
        par_jny_l: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.par_jny_l, Unset):
            par_jny_l = []
            for par_jny_l_item_data in self.par_jny_l:
                par_jny_l_item = par_jny_l_item_data.to_dict()

                par_jny_l.append(par_jny_l_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "icoX": ico_x,
                "dep": dep,
                "arr": arr,
                "jny": jny,
                "resState": res_state,
                "resRecommendation": res_recommendation,
            }
        )
        if par_jny_l is not UNSET:
            field_dict["parJnyL"] = par_jny_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SecLJNYType(d.pop("type"))

        ico_x = d.pop("icoX")

        dep = CommonDeparture.from_dict(d.pop("dep"))

        arr = CommonArrival.from_dict(d.pop("arr"))

        jny = Jny.from_dict(d.pop("jny"))

        res_state = SecLJNYResState(d.pop("resState"))

        res_recommendation = d.pop("resRecommendation")

        par_jny_l = []
        _par_jny_l = d.pop("parJnyL", UNSET)
        for par_jny_l_item_data in _par_jny_l or []:
            par_jny_l_item = Jny.from_dict(par_jny_l_item_data)

            par_jny_l.append(par_jny_l_item)

        sec_ljny = cls(
            type=type,
            ico_x=ico_x,
            dep=dep,
            arr=arr,
            jny=jny,
            res_state=res_state,
            res_recommendation=res_recommendation,
            par_jny_l=par_jny_l,
        )

        return sec_ljny
