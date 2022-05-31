from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="RouteTarifFare")


@attr.s(auto_attribs=True)
class RouteTarifFare:
    """
    Attributes:
        price (int):
        more_expensive_available (bool):
        bookable (bool):
        upsell (bool): ???
        target_context (str): ???
    """

    price: int
    more_expensive_available: bool
    bookable: bool
    upsell: bool
    target_context: str

    def to_dict(self) -> Dict[str, Any]:
        price = self.price
        more_expensive_available = self.more_expensive_available
        bookable = self.bookable
        upsell = self.upsell
        target_context = self.target_context

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "price": price,
                "moreExpensiveAvailable": more_expensive_available,
                "bookable": bookable,
                "upsell": upsell,
                "targetContext": target_context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price")

        more_expensive_available = d.pop("moreExpensiveAvailable")

        bookable = d.pop("bookable")

        upsell = d.pop("upsell")

        target_context = d.pop("targetContext")

        route_tarif_fare = cls(
            price=price,
            more_expensive_available=more_expensive_available,
            bookable=bookable,
            upsell=upsell,
            target_context=target_context,
        )

        return route_tarif_fare
