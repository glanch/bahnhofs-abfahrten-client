from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscrServiceDays")


@attr.s(auto_attribs=True)
class SubscrServiceDays:
    """
    Attributes:
        end_date (str):
        begin_date (str):
        selected_weekdays (str): 1 or 0 for each day, starts at monday
            example: 1001001
            Monday, Thursday, Sunday selected
    """

    end_date: str
    begin_date: str
    selected_weekdays: str

    def to_dict(self) -> Dict[str, Any]:
        end_date = self.end_date
        begin_date = self.begin_date
        selected_weekdays = self.selected_weekdays

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "endDate": end_date,
                "beginDate": begin_date,
                "selectedWeekdays": selected_weekdays,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_date = d.pop("endDate")

        begin_date = d.pop("beginDate")

        selected_weekdays = d.pop("selectedWeekdays")

        subscr_service_days = cls(
            end_date=end_date,
            begin_date=begin_date,
            selected_weekdays=selected_weekdays,
        )

        return subscr_service_days
