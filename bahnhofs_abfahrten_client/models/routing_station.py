from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="RoutingStation")


@attr.s(auto_attribs=True)
class RoutingStation:
    """
    Attributes:
        title (str):
        id (str):
    """

    title: str
    id: str

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        id = d.pop("id")

        routing_station = cls(
            title=title,
            id=id,
        )

        return routing_station
