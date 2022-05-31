from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Crd")


@attr.s(auto_attribs=True)
class Crd:
    """
    Attributes:
        x (float):
        y (float):
        z (Union[Unset, float]):
        layer_x (Union[Unset, float]):
        crd_sys_x (Union[Unset, float]):
    """

    x: float
    y: float
    z: Union[Unset, float] = UNSET
    layer_x: Union[Unset, float] = UNSET
    crd_sys_x: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        x = self.x
        y = self.y
        z = self.z
        layer_x = self.layer_x
        crd_sys_x = self.crd_sys_x

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "x": x,
                "y": y,
            }
        )
        if z is not UNSET:
            field_dict["z"] = z
        if layer_x is not UNSET:
            field_dict["layerX"] = layer_x
        if crd_sys_x is not UNSET:
            field_dict["crdSysX"] = crd_sys_x

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x = d.pop("x")

        y = d.pop("y")

        z = d.pop("z", UNSET)

        layer_x = d.pop("layerX", UNSET)

        crd_sys_x = d.pop("crdSysX", UNSET)

        crd = cls(
            x=x,
            y=y,
            z=z,
            layer_x=layer_x,
            crd_sys_x=crd_sys_x,
        )

        return crd
