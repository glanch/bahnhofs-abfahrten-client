import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainRunStop")


@attr.s(auto_attribs=True)
class TrainRunStop:
    """
    Attributes:
        name (str):
        eva_number (str):
        arrival_time (Union[Unset, datetime.datetime]):
        departure_time (Union[Unset, datetime.datetime]):
    """

    name: str
    eva_number: str
    arrival_time: Union[Unset, datetime.datetime] = UNSET
    departure_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        eva_number = self.eva_number
        arrival_time: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_time, Unset):
            arrival_time = self.arrival_time.isoformat()

        departure_time: Union[Unset, str] = UNSET
        if not isinstance(self.departure_time, Unset):
            departure_time = self.departure_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "evaNumber": eva_number,
            }
        )
        if arrival_time is not UNSET:
            field_dict["arrivalTime"] = arrival_time
        if departure_time is not UNSET:
            field_dict["departureTime"] = departure_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        eva_number = d.pop("evaNumber")

        _arrival_time = d.pop("arrivalTime", UNSET)
        arrival_time: Union[Unset, datetime.datetime]
        if isinstance(_arrival_time, Unset):
            arrival_time = UNSET
        else:
            arrival_time = isoparse(_arrival_time)

        _departure_time = d.pop("departureTime", UNSET)
        departure_time: Union[Unset, datetime.datetime]
        if isinstance(_departure_time, Unset):
            departure_time = UNSET
        else:
            departure_time = isoparse(_departure_time)

        train_run_stop = cls(
            name=name,
            eva_number=eva_number,
            arrival_time=arrival_time,
            departure_time=departure_time,
        )

        return train_run_stop
