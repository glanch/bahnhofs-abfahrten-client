from typing import Any, Dict, Type, TypeVar

import attr

from ..models.crd import Crd

T = TypeVar("T", bound="GeoRect")


@attr.s(auto_attribs=True)
class GeoRect:
    """
    Attributes:
        ll_crd (Crd):
        ur_crd (Crd):
    """

    ll_crd: Crd
    ur_crd: Crd

    def to_dict(self) -> Dict[str, Any]:
        ll_crd = self.ll_crd.to_dict()

        ur_crd = self.ur_crd.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "llCrd": ll_crd,
                "urCrd": ur_crd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ll_crd = Crd.from_dict(d.pop("llCrd"))

        ur_crd = Crd.from_dict(d.pop("urCrd"))

        geo_rect = cls(
            ll_crd=ll_crd,
            ur_crd=ur_crd,
        )

        return geo_rect
