from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TripSearchVia")


@attr.s(auto_attribs=True)
class TripSearchVia:
    """
    Attributes:
        eva_id (str):
        min_change_time (Union[Unset, float]):
    """

    eva_id: str
    min_change_time: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        eva_id = self.eva_id
        min_change_time = self.min_change_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "evaId": eva_id,
            }
        )
        if min_change_time is not UNSET:
            field_dict["minChangeTime"] = min_change_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eva_id = d.pop("evaId")

        min_change_time = d.pop("minChangeTime", UNSET)

        trip_search_via = cls(
            eva_id=eva_id,
            min_change_time=min_change_time,
        )

        return trip_search_via
