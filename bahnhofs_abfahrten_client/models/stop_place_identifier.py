from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopPlaceIdentifier")


@attr.s(auto_attribs=True)
class StopPlaceIdentifier:
    """
    Attributes:
        eva_number (str):
        station_id (Union[Unset, str]):
        ifopt (Union[Unset, str]): also known as DHID, globalId
        ril100 (Union[Unset, str]):
        alternative_ril_100 (Union[Unset, List[str]]):
    """

    eva_number: str
    station_id: Union[Unset, str] = UNSET
    ifopt: Union[Unset, str] = UNSET
    ril100: Union[Unset, str] = UNSET
    alternative_ril_100: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        eva_number = self.eva_number
        station_id = self.station_id
        ifopt = self.ifopt
        ril100 = self.ril100
        alternative_ril_100: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alternative_ril_100, Unset):
            alternative_ril_100 = self.alternative_ril_100

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "evaNumber": eva_number,
            }
        )
        if station_id is not UNSET:
            field_dict["stationId"] = station_id
        if ifopt is not UNSET:
            field_dict["ifopt"] = ifopt
        if ril100 is not UNSET:
            field_dict["ril100"] = ril100
        if alternative_ril_100 is not UNSET:
            field_dict["alternativeRil100"] = alternative_ril_100

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eva_number = d.pop("evaNumber")

        station_id = d.pop("stationId", UNSET)

        ifopt = d.pop("ifopt", UNSET)

        ril100 = d.pop("ril100", UNSET)

        alternative_ril_100 = cast(List[str], d.pop("alternativeRil100", UNSET))

        stop_place_identifier = cls(
            eva_number=eva_number,
            station_id=station_id,
            ifopt=ifopt,
            ril100=ril100,
            alternative_ril_100=alternative_ril_100,
        )

        return stop_place_identifier
