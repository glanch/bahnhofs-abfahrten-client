from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stop")


@attr.s(auto_attribs=True)
class Stop:
    """
    Attributes:
        name (str):
        additional (Union[Unset, bool]):
        cancelled (Union[Unset, bool]):
        show_via (Union[Unset, bool]):
    """

    name: str
    additional: Union[Unset, bool] = UNSET
    cancelled: Union[Unset, bool] = UNSET
    show_via: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        additional = self.additional
        cancelled = self.cancelled
        show_via = self.show_via

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if additional is not UNSET:
            field_dict["additional"] = additional
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if show_via is not UNSET:
            field_dict["showVia"] = show_via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        additional = d.pop("additional", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        show_via = d.pop("showVia", UNSET)

        stop = cls(
            name=name,
            additional=additional,
            cancelled=cancelled,
            show_via=show_via,
        )

        return stop
