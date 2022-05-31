from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.subscr_channel import SubscrChannel
from ..models.subscr_details_response_result import SubscrDetailsResponseResult
from ..models.subscr_details_response_status import SubscrDetailsResponseStatus
from ..models.subscr_event_history import SubscrEventHistory
from ..models.subscr_interval import SubscrInterval

T = TypeVar("T", bound="SubscrDetailsResponse")


@attr.s(auto_attribs=True)
class SubscrDetailsResponse:
    """
    Attributes:
        result (SubscrDetailsResponseResult):
        user_id (str):
        subscr_id (float):
        status (SubscrDetailsResponseStatus):
        channels (List[SubscrChannel]):
        intvl_subscr (SubscrInterval):
        event_hisotry (SubscrEventHistory):
    """

    result: SubscrDetailsResponseResult
    user_id: str
    subscr_id: float
    status: SubscrDetailsResponseStatus
    channels: List[SubscrChannel]
    intvl_subscr: SubscrInterval
    event_hisotry: SubscrEventHistory

    def to_dict(self) -> Dict[str, Any]:
        result = self.result.to_dict()

        user_id = self.user_id
        subscr_id = self.subscr_id
        status = self.status.value

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()

            channels.append(channels_item)

        intvl_subscr = self.intvl_subscr.to_dict()

        event_hisotry = self.event_hisotry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "result": result,
                "userId": user_id,
                "subscrId": subscr_id,
                "status": status,
                "channels": channels,
                "intvlSubscr": intvl_subscr,
                "eventHisotry": event_hisotry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result = SubscrDetailsResponseResult.from_dict(d.pop("result"))

        user_id = d.pop("userId")

        subscr_id = d.pop("subscrId")

        status = SubscrDetailsResponseStatus(d.pop("status"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = SubscrChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        intvl_subscr = SubscrInterval.from_dict(d.pop("intvlSubscr"))

        event_hisotry = SubscrEventHistory.from_dict(d.pop("eventHisotry"))

        subscr_details_response = cls(
            result=result,
            user_id=user_id,
            subscr_id=subscr_id,
            status=status,
            channels=channels,
            intvl_subscr=intvl_subscr,
            event_hisotry=event_hisotry,
        )

        return subscr_details_response
