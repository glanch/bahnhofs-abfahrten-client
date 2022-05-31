from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.auslastungs_value import AuslastungsValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteAuslastung")


@attr.s(auto_attribs=True)
class RouteAuslastung:
    """
    Attributes:
        first (Union[Unset, AuslastungsValue]): 1: Gering
            2: Hoch
            3: Sehr Hoch
            4: Ausgebucht
        second (Union[Unset, AuslastungsValue]): 1: Gering
            2: Hoch
            3: Sehr Hoch
            4: Ausgebucht
    """

    first: Union[Unset, AuslastungsValue] = UNSET
    second: Union[Unset, AuslastungsValue] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first: Union[Unset, int] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.value

        second: Union[Unset, int] = UNSET
        if not isinstance(self.second, Unset):
            second = self.second.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if second is not UNSET:
            field_dict["second"] = second

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _first = d.pop("first", UNSET)
        first: Union[Unset, AuslastungsValue]
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = AuslastungsValue(_first)

        _second = d.pop("second", UNSET)
        second: Union[Unset, AuslastungsValue]
        if isinstance(_second, Unset):
            second = UNSET
        else:
            second = AuslastungsValue(_second)

        route_auslastung = cls(
            first=first,
            second=second,
        )

        return route_auslastung
