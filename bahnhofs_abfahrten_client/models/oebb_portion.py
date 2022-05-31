from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="OEBBPortion")


@attr.s(auto_attribs=True)
class OEBBPortion:
    """
    Attributes:
        train_nr (int):
        train_name (str): `${type} ${number}`
    """

    train_nr: int
    train_name: str

    def to_dict(self) -> Dict[str, Any]:
        train_nr = self.train_nr
        train_name = self.train_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "trainNr": train_nr,
                "trainName": train_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        train_nr = d.pop("trainNr")

        train_name = d.pop("trainName")

        oebb_portion = cls(
            train_nr=train_nr,
            train_name=train_name,
        )

        return oebb_portion
