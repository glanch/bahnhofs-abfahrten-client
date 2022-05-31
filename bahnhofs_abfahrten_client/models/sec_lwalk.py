from typing import Any, Dict, Type, TypeVar

import attr

from ..models.common_arrival import CommonArrival
from ..models.common_departure import CommonDeparture
from ..models.gis import Gis
from ..models.sec_lwalk_type import SecLWALKType

T = TypeVar("T", bound="SecLWALK")


@attr.s(auto_attribs=True)
class SecLWALK:
    """
    Attributes:
        type (SecLWALKType):
        ico_x (float):
        dep (CommonDeparture):
        arr (CommonArrival):
        gis (Gis):
    """

    type: SecLWALKType
    ico_x: float
    dep: CommonDeparture
    arr: CommonArrival
    gis: Gis

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        ico_x = self.ico_x
        dep = self.dep.to_dict()

        arr = self.arr.to_dict()

        gis = self.gis.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "icoX": ico_x,
                "dep": dep,
                "arr": arr,
                "gis": gis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SecLWALKType(d.pop("type"))

        ico_x = d.pop("icoX")

        dep = CommonDeparture.from_dict(d.pop("dep"))

        arr = CommonArrival.from_dict(d.pop("arr"))

        gis = Gis.from_dict(d.pop("gis"))

        sec_lwalk = cls(
            type=type,
            ico_x=ico_x,
            dep=dep,
            arr=arr,
            gis=gis,
        )

        return sec_lwalk
