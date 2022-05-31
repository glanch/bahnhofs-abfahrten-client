from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.optional_loc_l import OptionalLocL
from ..models.subscr_channel import SubscrChannel
from ..models.subscr_search_response_intvl_subscr_l_item_status import SubscrSearchResponseIntvlSubscrLItemStatus

T = TypeVar("T", bound="SubscrSearchResponseIntvlSubscrLItem")


@attr.s(auto_attribs=True)
class SubscrSearchResponseIntvlSubscrLItem:
    """
    Attributes:
        arr_loc (OptionalLocL):
        dep_loc (OptionalLocL):
        time (str): HHmmSS
        period (float):
        channels (List[SubscrChannel]):
        status (SubscrSearchResponseIntvlSubscrLItemStatus):
    """

    arr_loc: OptionalLocL
    dep_loc: OptionalLocL
    time: str
    period: float
    channels: List[SubscrChannel]
    status: SubscrSearchResponseIntvlSubscrLItemStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arr_loc = self.arr_loc.to_dict()

        dep_loc = self.dep_loc.to_dict()

        time = self.time
        period = self.period
        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()

            channels.append(channels_item)

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arrLoc": arr_loc,
                "depLoc": dep_loc,
                "time": time,
                "period": period,
                "channels": channels,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        arr_loc = OptionalLocL.from_dict(d.pop("arrLoc"))

        dep_loc = OptionalLocL.from_dict(d.pop("depLoc"))

        time = d.pop("time")

        period = d.pop("period")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = SubscrChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        status = SubscrSearchResponseIntvlSubscrLItemStatus(d.pop("status"))

        subscr_search_response_intvl_subscr_l_item = cls(
            arr_loc=arr_loc,
            dep_loc=dep_loc,
            time=time,
            period=period,
            channels=channels,
            status=status,
        )

        subscr_search_response_intvl_subscr_l_item.additional_properties = d
        return subscr_search_response_intvl_subscr_l_item

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
