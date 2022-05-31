from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.route_auslastung import RouteAuslastung

T = TypeVar("T", bound="TrainOccupancyList")


@attr.s(auto_attribs=True)
class TrainOccupancyList:
    """ """

    additional_properties: Dict[str, Optional[RouteAuslastung]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict() if prop else None

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        train_occupancy_list = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            _additional_property = prop_dict
            additional_property: Optional[RouteAuslastung]
            if _additional_property is None:
                additional_property = None
            else:
                additional_property = RouteAuslastung.from_dict(_additional_property)

            additional_properties[prop_name] = additional_property

        train_occupancy_list.additional_properties = additional_properties
        return train_occupancy_list

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Optional[RouteAuslastung]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Optional[RouteAuslastung]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
