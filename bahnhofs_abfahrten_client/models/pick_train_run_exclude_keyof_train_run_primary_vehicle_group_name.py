import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.coach_sequence_product import CoachSequenceProduct
from ..models.train_run_stop import TrainRunStop

T = TypeVar("T", bound="PickTrainRunExcludeKeyofTrainRunPrimaryVehicleGroupName")


@attr.s(auto_attribs=True)
class PickTrainRunExcludeKeyofTrainRunPrimaryVehicleGroupName:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        product (CoachSequenceProduct):
        origin (TrainRunStop):
        destination (TrainRunStop):
        via (List[TrainRunStop]):
        dates (List[datetime.datetime]):
    """

    product: CoachSequenceProduct
    origin: TrainRunStop
    destination: TrainRunStop
    via: List[TrainRunStop]
    dates: List[datetime.datetime]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product = self.product.to_dict()

        origin = self.origin.to_dict()

        destination = self.destination.to_dict()

        via = []
        for via_item_data in self.via:
            via_item = via_item_data.to_dict()

            via.append(via_item)

        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.isoformat()

            dates.append(dates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product": product,
                "origin": origin,
                "destination": destination,
                "via": via,
                "dates": dates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product = CoachSequenceProduct.from_dict(d.pop("product"))

        origin = TrainRunStop.from_dict(d.pop("origin"))

        destination = TrainRunStop.from_dict(d.pop("destination"))

        via = []
        _via = d.pop("via")
        for via_item_data in _via:
            via_item = TrainRunStop.from_dict(via_item_data)

            via.append(via_item)

        dates = []
        _dates = d.pop("dates")
        for dates_item_data in _dates:
            dates_item = isoparse(dates_item_data)

            dates.append(dates_item)

        pick_train_run_exclude_keyof_train_run_primary_vehicle_group_name = cls(
            product=product,
            origin=origin,
            destination=destination,
            via=via,
            dates=dates,
        )

        pick_train_run_exclude_keyof_train_run_primary_vehicle_group_name.additional_properties = d
        return pick_train_run_exclude_keyof_train_run_primary_vehicle_group_name

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
