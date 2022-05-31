from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.oebb_coach_sequence_wagon_seasoning import OEBBCoachSequenceWagonSeasoning
from ..types import UNSET, Unset

T = TypeVar("T", bound="OEBBCoachSequenceWagon")


@attr.s(auto_attribs=True)
class OEBBCoachSequenceWagon:
    """
    Attributes:
        origin (str): example: WBF (Wien Hbf)
        destination (str): example: WBF (Wien Hbf)
        ranking (float):
        capacity_business_class (float):
        capacity_first_class (float):
        capacity_second_class (float):
        capacity_couchette (float):
        capacity_sleeper (float):
        capacity_wheel_chair (float):
        capacity_bicycle (float):
        is_bicycle_allowed (bool):
        is_wheel_chair_accessible (bool):
        has_wifi (bool):
        is_info_point (bool):
        is_play_zone (bool):
        is_child_cinema (bool):
        is_dining (bool):
        is_quiet_zone (bool):
        is_locked (bool):
        destination_name (str):
        length_over_buffers (float):
        origin_time (str):
        destination_time (str):
        uic_number (Union[Unset, str]):
        kind (Union[Unset, str]):
        seasoning (Union[Unset, OEBBCoachSequenceWagonSeasoning]):
    """

    origin: str
    destination: str
    ranking: float
    capacity_business_class: float
    capacity_first_class: float
    capacity_second_class: float
    capacity_couchette: float
    capacity_sleeper: float
    capacity_wheel_chair: float
    capacity_bicycle: float
    is_bicycle_allowed: bool
    is_wheel_chair_accessible: bool
    has_wifi: bool
    is_info_point: bool
    is_play_zone: bool
    is_child_cinema: bool
    is_dining: bool
    is_quiet_zone: bool
    is_locked: bool
    destination_name: str
    length_over_buffers: float
    origin_time: str
    destination_time: str
    uic_number: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    seasoning: Union[Unset, OEBBCoachSequenceWagonSeasoning] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin
        destination = self.destination
        ranking = self.ranking
        capacity_business_class = self.capacity_business_class
        capacity_first_class = self.capacity_first_class
        capacity_second_class = self.capacity_second_class
        capacity_couchette = self.capacity_couchette
        capacity_sleeper = self.capacity_sleeper
        capacity_wheel_chair = self.capacity_wheel_chair
        capacity_bicycle = self.capacity_bicycle
        is_bicycle_allowed = self.is_bicycle_allowed
        is_wheel_chair_accessible = self.is_wheel_chair_accessible
        has_wifi = self.has_wifi
        is_info_point = self.is_info_point
        is_play_zone = self.is_play_zone
        is_child_cinema = self.is_child_cinema
        is_dining = self.is_dining
        is_quiet_zone = self.is_quiet_zone
        is_locked = self.is_locked
        destination_name = self.destination_name
        length_over_buffers = self.length_over_buffers
        origin_time = self.origin_time
        destination_time = self.destination_time
        uic_number = self.uic_number
        kind = self.kind
        seasoning: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seasoning, Unset):
            seasoning = self.seasoning.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "origin": origin,
                "destination": destination,
                "ranking": ranking,
                "capacityBusinessClass": capacity_business_class,
                "capacityFirstClass": capacity_first_class,
                "capacitySecondClass": capacity_second_class,
                "capacityCouchette": capacity_couchette,
                "capacitySleeper": capacity_sleeper,
                "capacityWheelChair": capacity_wheel_chair,
                "capacityBicycle": capacity_bicycle,
                "isBicycleAllowed": is_bicycle_allowed,
                "isWheelChairAccessible": is_wheel_chair_accessible,
                "hasWifi": has_wifi,
                "isInfoPoint": is_info_point,
                "isPlayZone": is_play_zone,
                "isChildCinema": is_child_cinema,
                "isDining": is_dining,
                "isQuietZone": is_quiet_zone,
                "isLocked": is_locked,
                "destinationName": destination_name,
                "lengthOverBuffers": length_over_buffers,
                "originTime": origin_time,
                "destinationTime": destination_time,
            }
        )
        if uic_number is not UNSET:
            field_dict["uicNumber"] = uic_number
        if kind is not UNSET:
            field_dict["kind"] = kind
        if seasoning is not UNSET:
            field_dict["seasoning"] = seasoning

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        origin = d.pop("origin")

        destination = d.pop("destination")

        ranking = d.pop("ranking")

        capacity_business_class = d.pop("capacityBusinessClass")

        capacity_first_class = d.pop("capacityFirstClass")

        capacity_second_class = d.pop("capacitySecondClass")

        capacity_couchette = d.pop("capacityCouchette")

        capacity_sleeper = d.pop("capacitySleeper")

        capacity_wheel_chair = d.pop("capacityWheelChair")

        capacity_bicycle = d.pop("capacityBicycle")

        is_bicycle_allowed = d.pop("isBicycleAllowed")

        is_wheel_chair_accessible = d.pop("isWheelChairAccessible")

        has_wifi = d.pop("hasWifi")

        is_info_point = d.pop("isInfoPoint")

        is_play_zone = d.pop("isPlayZone")

        is_child_cinema = d.pop("isChildCinema")

        is_dining = d.pop("isDining")

        is_quiet_zone = d.pop("isQuietZone")

        is_locked = d.pop("isLocked")

        destination_name = d.pop("destinationName")

        length_over_buffers = d.pop("lengthOverBuffers")

        origin_time = d.pop("originTime")

        destination_time = d.pop("destinationTime")

        uic_number = d.pop("uicNumber", UNSET)

        kind = d.pop("kind", UNSET)

        _seasoning = d.pop("seasoning", UNSET)
        seasoning: Union[Unset, OEBBCoachSequenceWagonSeasoning]
        if isinstance(_seasoning, Unset):
            seasoning = UNSET
        else:
            seasoning = OEBBCoachSequenceWagonSeasoning.from_dict(_seasoning)

        oebb_coach_sequence_wagon = cls(
            origin=origin,
            destination=destination,
            ranking=ranking,
            capacity_business_class=capacity_business_class,
            capacity_first_class=capacity_first_class,
            capacity_second_class=capacity_second_class,
            capacity_couchette=capacity_couchette,
            capacity_sleeper=capacity_sleeper,
            capacity_wheel_chair=capacity_wheel_chair,
            capacity_bicycle=capacity_bicycle,
            is_bicycle_allowed=is_bicycle_allowed,
            is_wheel_chair_accessible=is_wheel_chair_accessible,
            has_wifi=has_wifi,
            is_info_point=is_info_point,
            is_play_zone=is_play_zone,
            is_child_cinema=is_child_cinema,
            is_dining=is_dining,
            is_quiet_zone=is_quiet_zone,
            is_locked=is_locked,
            destination_name=destination_name,
            length_over_buffers=length_over_buffers,
            origin_time=origin_time,
            destination_time=destination_time,
            uic_number=uic_number,
            kind=kind,
            seasoning=seasoning,
        )

        return oebb_coach_sequence_wagon
