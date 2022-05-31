from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OpL")


@attr.s(auto_attribs=True)
class OpL:
    """
    Attributes:
        name (str):
        ico_x (float):
    """

    name: str
    ico_x: float

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        ico_x = self.ico_x

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "icoX": ico_x,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        ico_x = d.pop("icoX")

        op_l = cls(
            name=name,
            ico_x=ico_x,
        )

        return op_l
