from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PickGroupedStopPlacenameOrEvaNumber")


@attr.s(auto_attribs=True)
class PickGroupedStopPlacenameOrEvaNumber:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        eva_number (str):
    """

    name: str
    eva_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        eva_number = self.eva_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "evaNumber": eva_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        eva_number = d.pop("evaNumber")

        pick_grouped_stop_placename_or_eva_number = cls(
            name=name,
            eva_number=eva_number,
        )

        pick_grouped_stop_placename_or_eva_number.additional_properties = d
        return pick_grouped_stop_placename_or_eva_number

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