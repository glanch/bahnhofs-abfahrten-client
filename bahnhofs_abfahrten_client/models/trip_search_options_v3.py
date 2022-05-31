import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.trip_search_tarif_request import TripSearchTarifRequest
from ..models.trip_search_via import TripSearchVia
from ..types import UNSET, Unset

T = TypeVar("T", bound="TripSearchOptionsV3")


@attr.s(auto_attribs=True)
class TripSearchOptionsV3:
    """
    Attributes:
        start (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        destination (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        economic (Union[Unset, bool]): true = not only fastest route
        get_iv (Union[Unset, bool]): Unknown flag
        get_passlist (Union[Unset, bool]): Get Stop inbetween
        get_polyline (Union[Unset, bool]): Polylines - unknown format
        num_f (Union[Unset, float]):
        ctx_scr (Union[Unset, str]):
        ushrp (Union[Unset, bool]): Is a station nearby enough for routing?
        time (Union[Unset, datetime.datetime]):
        transfer_time (Union[Unset, float]):
        max_changes (Union[Unset, float]):
        search_for_departure (Union[Unset, bool]):
        only_regional (Union[Unset, bool]):
        tarif (Union[Unset, TripSearchTarifRequest]):
        via (Union[Unset, List[TripSearchVia]]):
    """

    start: str
    destination: str
    economic: Union[Unset, bool] = UNSET
    get_iv: Union[Unset, bool] = UNSET
    get_passlist: Union[Unset, bool] = UNSET
    get_polyline: Union[Unset, bool] = UNSET
    num_f: Union[Unset, float] = UNSET
    ctx_scr: Union[Unset, str] = UNSET
    ushrp: Union[Unset, bool] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    transfer_time: Union[Unset, float] = UNSET
    max_changes: Union[Unset, float] = UNSET
    search_for_departure: Union[Unset, bool] = UNSET
    only_regional: Union[Unset, bool] = UNSET
    tarif: Union[Unset, TripSearchTarifRequest] = UNSET
    via: Union[Unset, List[TripSearchVia]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start = self.start
        destination = self.destination
        economic = self.economic
        get_iv = self.get_iv
        get_passlist = self.get_passlist
        get_polyline = self.get_polyline
        num_f = self.num_f
        ctx_scr = self.ctx_scr
        ushrp = self.ushrp
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        transfer_time = self.transfer_time
        max_changes = self.max_changes
        search_for_departure = self.search_for_departure
        only_regional = self.only_regional
        tarif: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tarif, Unset):
            tarif = self.tarif.to_dict()

        via: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.via, Unset):
            via = []
            for via_item_data in self.via:
                via_item = via_item_data.to_dict()

                via.append(via_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "start": start,
                "destination": destination,
            }
        )
        if economic is not UNSET:
            field_dict["economic"] = economic
        if get_iv is not UNSET:
            field_dict["getIV"] = get_iv
        if get_passlist is not UNSET:
            field_dict["getPasslist"] = get_passlist
        if get_polyline is not UNSET:
            field_dict["getPolyline"] = get_polyline
        if num_f is not UNSET:
            field_dict["numF"] = num_f
        if ctx_scr is not UNSET:
            field_dict["ctxScr"] = ctx_scr
        if ushrp is not UNSET:
            field_dict["ushrp"] = ushrp
        if time is not UNSET:
            field_dict["time"] = time
        if transfer_time is not UNSET:
            field_dict["transferTime"] = transfer_time
        if max_changes is not UNSET:
            field_dict["maxChanges"] = max_changes
        if search_for_departure is not UNSET:
            field_dict["searchForDeparture"] = search_for_departure
        if only_regional is not UNSET:
            field_dict["onlyRegional"] = only_regional
        if tarif is not UNSET:
            field_dict["tarif"] = tarif
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = d.pop("start")

        destination = d.pop("destination")

        economic = d.pop("economic", UNSET)

        get_iv = d.pop("getIV", UNSET)

        get_passlist = d.pop("getPasslist", UNSET)

        get_polyline = d.pop("getPolyline", UNSET)

        num_f = d.pop("numF", UNSET)

        ctx_scr = d.pop("ctxScr", UNSET)

        ushrp = d.pop("ushrp", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        transfer_time = d.pop("transferTime", UNSET)

        max_changes = d.pop("maxChanges", UNSET)

        search_for_departure = d.pop("searchForDeparture", UNSET)

        only_regional = d.pop("onlyRegional", UNSET)

        _tarif = d.pop("tarif", UNSET)
        tarif: Union[Unset, TripSearchTarifRequest]
        if isinstance(_tarif, Unset):
            tarif = UNSET
        else:
            tarif = TripSearchTarifRequest.from_dict(_tarif)

        via = []
        _via = d.pop("via", UNSET)
        for via_item_data in _via or []:
            via_item = TripSearchVia.from_dict(via_item_data)

            via.append(via_item)

        trip_search_options_v3 = cls(
            start=start,
            destination=destination,
            economic=economic,
            get_iv=get_iv,
            get_passlist=get_passlist,
            get_polyline=get_polyline,
            num_f=num_f,
            ctx_scr=ctx_scr,
            ushrp=ushrp,
            time=time,
            transfer_time=transfer_time,
            max_changes=max_changes,
            search_for_departure=search_for_departure,
            only_regional=only_regional,
            tarif=tarif,
            via=via,
        )

        return trip_search_options_v3
