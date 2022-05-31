from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.op_l import OpL
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonProductInfo")


@attr.s(auto_attribs=True)
class CommonProductInfo:
    """
    Attributes:
        name (str):
        line (Union[Unset, str]):
        number (Union[Unset, str]):
        type (Union[Unset, str]):
        operator (Union[Unset, OpL]):
        admin (Union[Unset, str]):
    """

    name: str
    line: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    operator: Union[Unset, OpL] = UNSET
    admin: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        line = self.line
        number = self.number
        type = self.type
        operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        admin = self.admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if line is not UNSET:
            field_dict["line"] = line
        if number is not UNSET:
            field_dict["number"] = number
        if type is not UNSET:
            field_dict["type"] = type
        if operator is not UNSET:
            field_dict["operator"] = operator
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        line = d.pop("line", UNSET)

        number = d.pop("number", UNSET)

        type = d.pop("type", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, OpL]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = OpL.from_dict(_operator)

        admin = d.pop("admin", UNSET)

        common_product_info = cls(
            name=name,
            line=line,
            number=number,
            type=type,
            operator=operator,
            admin=admin,
        )

        return common_product_info
