from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.oebb_coach_sequence_wagon import OEBBCoachSequenceWagon

T = TypeVar("T", bound="OEBBTrainInfo")


@attr.s(auto_attribs=True)
class OEBBTrainInfo:
    """
    Attributes:
        train_nr (float):
        date (str): ISO Date
        version (float):
        is_reported (bool):
        assembly_station (str):
        source (str):
        stations (List[str]):
        wagons (List[OEBBCoachSequenceWagon]):
    """

    train_nr: float
    date: str
    version: float
    is_reported: bool
    assembly_station: str
    source: str
    stations: List[str]
    wagons: List[OEBBCoachSequenceWagon]

    def to_dict(self) -> Dict[str, Any]:
        train_nr = self.train_nr
        date = self.date
        version = self.version
        is_reported = self.is_reported
        assembly_station = self.assembly_station
        source = self.source
        stations = self.stations

        wagons = []
        for wagons_item_data in self.wagons:
            wagons_item = wagons_item_data.to_dict()

            wagons.append(wagons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "trainNr": train_nr,
                "date": date,
                "version": version,
                "isReported": is_reported,
                "assemblyStation": assembly_station,
                "source": source,
                "stations": stations,
                "wagons": wagons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        train_nr = d.pop("trainNr")

        date = d.pop("date")

        version = d.pop("version")

        is_reported = d.pop("isReported")

        assembly_station = d.pop("assemblyStation")

        source = d.pop("source")

        stations = cast(List[str], d.pop("stations"))

        wagons = []
        _wagons = d.pop("wagons")
        for wagons_item_data in _wagons:
            wagons_item = OEBBCoachSequenceWagon.from_dict(wagons_item_data)

            wagons.append(wagons_item)

        oebb_train_info = cls(
            train_nr=train_nr,
            date=date,
            version=version,
            is_reported=is_reported,
            assembly_station=assembly_station,
            source=source,
            stations=stations,
            wagons=wagons,
        )

        return oebb_train_info
