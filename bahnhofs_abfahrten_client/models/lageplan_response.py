from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LageplanResponse")


@attr.s(auto_attribs=True)
class LageplanResponse:
    """
    Attributes:
        lageplan (Union[Unset, str]):
    """

    lageplan: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        lageplan = self.lageplan

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if lageplan is not UNSET:
            field_dict["lageplan"] = lageplan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lageplan = d.pop("lageplan", UNSET)

        lageplan_response = cls(
            lageplan=lageplan,
        )

        return lageplan_response
