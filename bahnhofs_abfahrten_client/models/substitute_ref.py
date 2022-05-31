from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="SubstituteRef")


@attr.s(auto_attribs=True)
class SubstituteRef:
    """
    Attributes:
        train_number (str):
        train_type (str):
        train (str):
    """

    train_number: str
    train_type: str
    train: str

    def to_dict(self) -> Dict[str, Any]:
        train_number = self.train_number
        train_type = self.train_type
        train = self.train

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "trainNumber": train_number,
                "trainType": train_type,
                "train": train,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        train_number = d.pop("trainNumber")

        train_type = d.pop("trainType")

        train = d.pop("train")

        substitute_ref = cls(
            train_number=train_number,
            train_type=train_type,
            train=train,
        )

        return substitute_ref
