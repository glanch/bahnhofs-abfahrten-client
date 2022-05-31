from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="TxtC")


@attr.s(auto_attribs=True)
class TxtC:
    """
    Attributes:
        r (float):
        g (float):
        b (float):
    """

    r: float
    g: float
    b: float

    def to_dict(self) -> Dict[str, Any]:
        r = self.r
        g = self.g
        b = self.b

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "r": r,
                "g": g,
                "b": b,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        r = d.pop("r")

        g = d.pop("g")

        b = d.pop("b")

        txt_c = cls(
            r=r,
            g=g,
            b=b,
        )

        return txt_c
