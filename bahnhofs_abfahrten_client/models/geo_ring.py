from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.crd import Crd
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoRing")


@attr.s(auto_attribs=True)
class GeoRing:
    """
    Attributes:
        c_crd (Crd):
        max_dist (float):
        min_dist (Union[Unset, float]):
    """

    c_crd: Crd
    max_dist: float
    min_dist: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        c_crd = self.c_crd.to_dict()

        max_dist = self.max_dist
        min_dist = self.min_dist

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "cCrd": c_crd,
                "maxDist": max_dist,
            }
        )
        if min_dist is not UNSET:
            field_dict["minDist"] = min_dist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        c_crd = Crd.from_dict(d.pop("cCrd"))

        max_dist = d.pop("maxDist")

        min_dist = d.pop("minDist", UNSET)

        geo_ring = cls(
            c_crd=c_crd,
            max_dist=max_dist,
            min_dist=min_dist,
        )

        return geo_ring
