import datetime
from typing import Any, Dict, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.wing_info_station import WingInfoStation

T = TypeVar("T", bound="WingInfo")


@attr.s(auto_attribs=True)
class WingInfo:
    """
    Attributes:
        station (WingInfoStation):
        pt (datetime.datetime):
        fl (bool):
    """

    station: WingInfoStation
    pt: datetime.datetime
    fl: bool

    def to_dict(self) -> Dict[str, Any]:
        station = self.station.to_dict()

        pt = self.pt.isoformat()

        fl = self.fl

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "station": station,
                "pt": pt,
                "fl": fl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        station = WingInfoStation.from_dict(d.pop("station"))

        pt = isoparse(d.pop("pt"))

        fl = d.pop("fl")

        wing_info = cls(
            station=station,
            pt=pt,
            fl=fl,
        )

        return wing_info
