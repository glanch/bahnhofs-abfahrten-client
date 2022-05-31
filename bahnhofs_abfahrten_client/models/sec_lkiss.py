from typing import Any, Dict, Type, TypeVar

import attr

from ..models.sec_lkiss_type import SecLKISSType

T = TypeVar("T", bound="SecLKISS")


@attr.s(auto_attribs=True)
class SecLKISS:
    """
    Attributes:
        type (SecLKISSType):
    """

    type: SecLKISSType

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SecLKISSType(d.pop("type"))

        sec_lkiss = cls(
            type=type,
        )

        return sec_lkiss
