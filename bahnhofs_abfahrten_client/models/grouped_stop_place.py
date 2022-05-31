from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.coordinate_2d import Coordinate2D
from ..models.stop_place_identifier import StopPlaceIdentifier
from ..models.transport_type import TransportType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupedStopPlace")


@attr.s(auto_attribs=True)
class GroupedStopPlace:
    """
    Attributes:
        eva_number (str):
        name (str):
        available_transports (List[TransportType]):
        position (Union[Unset, Coordinate2D]): 2D coordinate within geo reference system.
        identifier (Union[Unset, StopPlaceIdentifier]):
    """

    eva_number: str
    name: str
    available_transports: List[TransportType]
    position: Union[Unset, Coordinate2D] = UNSET
    identifier: Union[Unset, StopPlaceIdentifier] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        eva_number = self.eva_number
        name = self.name
        available_transports = []
        for available_transports_item_data in self.available_transports:
            available_transports_item = available_transports_item_data.value

            available_transports.append(available_transports_item)

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "evaNumber": eva_number,
                "name": name,
                "availableTransports": available_transports,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eva_number = d.pop("evaNumber")

        name = d.pop("name")

        available_transports = []
        _available_transports = d.pop("availableTransports")
        for available_transports_item_data in _available_transports:
            available_transports_item = TransportType(available_transports_item_data)

            available_transports.append(available_transports_item)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Coordinate2D]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Coordinate2D.from_dict(_position)

        _identifier = d.pop("identifier", UNSET)
        identifier: Union[Unset, StopPlaceIdentifier]
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = StopPlaceIdentifier.from_dict(_identifier)

        grouped_stop_place = cls(
            eva_number=eva_number,
            name=name,
            available_transports=available_transports,
            position=position,
            identifier=identifier,
        )

        return grouped_stop_place
