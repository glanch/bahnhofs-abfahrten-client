import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.coach_sequence_baureihe import CoachSequenceBaureihe
from ..models.coach_sequence_product import CoachSequenceProduct
from ..models.train_run_stop import TrainRunStop
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainRunWithBR")


@attr.s(auto_attribs=True)
class TrainRunWithBR:
    """
    Attributes:
        product (CoachSequenceProduct):
        origin (TrainRunStop):
        destination (TrainRunStop):
        via (List[TrainRunStop]):
        dates (List[datetime.datetime]):
        br (Union[Unset, CoachSequenceBaureihe]):
    """

    product: CoachSequenceProduct
    origin: TrainRunStop
    destination: TrainRunStop
    via: List[TrainRunStop]
    dates: List[datetime.datetime]
    br: Union[Unset, CoachSequenceBaureihe] = UNSET

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

        br: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.br, Unset):
            br = self.br.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "product": product,
                "origin": origin,
                "destination": destination,
                "via": via,
                "dates": dates,
            }
        )
        if br is not UNSET:
            field_dict["br"] = br

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

        _br = d.pop("br", UNSET)
        br: Union[Unset, CoachSequenceBaureihe]
        if isinstance(_br, Unset):
            br = UNSET
        else:
            br = CoachSequenceBaureihe.from_dict(_br)

        train_run_with_br = cls(
            product=product,
            origin=origin,
            destination=destination,
            via=via,
            dates=dates,
            br=br,
        )

        return train_run_with_br
