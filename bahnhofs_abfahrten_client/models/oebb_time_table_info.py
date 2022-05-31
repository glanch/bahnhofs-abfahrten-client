from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.oebb_platforms import OEBBPlatforms
from ..models.oebb_portion import OEBBPortion
from ..models.oebb_sector_info import OEBBSectorInfo
from ..models.oebb_time import OEBBTime

T = TypeVar("T", bound="OEBBTimeTableInfo")


@attr.s(auto_attribs=True)
class OEBBTimeTableInfo:
    """
    Attributes:
        date (str):
        train_nr (int):
        train_name (str):
        station_name (str):
        platform (OEBBPlatforms):
        sectors (OEBBSectorInfo):
        time (OEBBTime):
        portions (List[OEBBPortion]):
    """

    date: str
    train_nr: int
    train_name: str
    station_name: str
    platform: OEBBPlatforms
    sectors: OEBBSectorInfo
    time: OEBBTime
    portions: List[OEBBPortion]

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        train_nr = self.train_nr
        train_name = self.train_name
        station_name = self.station_name
        platform = self.platform.to_dict()

        sectors = self.sectors.to_dict()

        time = self.time.to_dict()

        portions = []
        for portions_item_data in self.portions:
            portions_item = portions_item_data.to_dict()

            portions.append(portions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "date": date,
                "trainNr": train_nr,
                "trainName": train_name,
                "stationName": station_name,
                "platform": platform,
                "sectors": sectors,
                "time": time,
                "portions": portions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        train_nr = d.pop("trainNr")

        train_name = d.pop("trainName")

        station_name = d.pop("stationName")

        platform = OEBBPlatforms.from_dict(d.pop("platform"))

        sectors = OEBBSectorInfo.from_dict(d.pop("sectors"))

        time = OEBBTime.from_dict(d.pop("time"))

        portions = []
        _portions = d.pop("portions")
        for portions_item_data in _portions:
            portions_item = OEBBPortion.from_dict(portions_item_data)

            portions.append(portions_item)

        oebb_time_table_info = cls(
            date=date,
            train_nr=train_nr,
            train_name=train_name,
            station_name=station_name,
            platform=platform,
            sectors=sectors,
            time=time,
            portions=portions,
        )

        return oebb_time_table_info
