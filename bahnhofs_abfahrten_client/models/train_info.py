from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.op_l import OpL
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainInfo")


@attr.s(auto_attribs=True)
class TrainInfo:
    """
    Attributes:
        name (str):
        number (str):
        type (str):
        line (Union[Unset, str]):
        operator (Union[Unset, OpL]):
        admin (Union[Unset, str]):
        long_distance (Union[Unset, bool]):
    """

    name: str
    number: str
    type: str
    line: Union[Unset, str] = UNSET
    operator: Union[Unset, OpL] = UNSET
    admin: Union[Unset, str] = UNSET
    long_distance: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        number = self.number
        type = self.type
        line = self.line
        operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        admin = self.admin
        long_distance = self.long_distance

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "number": number,
                "type": type,
            }
        )
        if line is not UNSET:
            field_dict["line"] = line
        if operator is not UNSET:
            field_dict["operator"] = operator
        if admin is not UNSET:
            field_dict["admin"] = admin
        if long_distance is not UNSET:
            field_dict["longDistance"] = long_distance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        number = d.pop("number")

        type = d.pop("type")

        line = d.pop("line", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, OpL]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = OpL.from_dict(_operator)

        admin = d.pop("admin", UNSET)

        long_distance = d.pop("longDistance", UNSET)

        train_info = cls(
            name=name,
            number=number,
            type=type,
            line=line,
            operator=operator,
            admin=admin,
            long_distance=long_distance,
        )

        return train_info
