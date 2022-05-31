from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="OEBBCoachSequenceWagonSeasoning")


@attr.s(auto_attribs=True)
class OEBBCoachSequenceWagonSeasoning:
    """
    Attributes:
        seasoning_string (str):
        start_date (str):
    """

    seasoning_string: str
    start_date: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seasoning_string = self.seasoning_string
        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seasoningString": seasoning_string,
                "startDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seasoning_string = d.pop("seasoningString")

        start_date = d.pop("startDate")

        oebb_coach_sequence_wagon_seasoning = cls(
            seasoning_string=seasoning_string,
            start_date=start_date,
        )

        oebb_coach_sequence_wagon_seasoning.additional_properties = d
        return oebb_coach_sequence_wagon_seasoning

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
