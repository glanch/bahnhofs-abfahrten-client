from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.jny_l import JnyL

T = TypeVar("T", bound="Freq")


@attr.s(auto_attribs=True)
class Freq:
    """
    Attributes:
        min_c (float):
        max_c (float):
        num_c (float):
        jny_l (List[JnyL]):
    """

    min_c: float
    max_c: float
    num_c: float
    jny_l: List[JnyL]

    def to_dict(self) -> Dict[str, Any]:
        min_c = self.min_c
        max_c = self.max_c
        num_c = self.num_c
        jny_l = []
        for jny_l_item_data in self.jny_l:
            jny_l_item = jny_l_item_data.to_dict()

            jny_l.append(jny_l_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "minC": min_c,
                "maxC": max_c,
                "numC": num_c,
                "jnyL": jny_l,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_c = d.pop("minC")

        max_c = d.pop("maxC")

        num_c = d.pop("numC")

        jny_l = []
        _jny_l = d.pop("jnyL")
        for jny_l_item_data in _jny_l:
            jny_l_item = JnyL.from_dict(jny_l_item_data)

            jny_l.append(jny_l_item)

        freq = cls(
            min_c=min_c,
            max_c=max_c,
            num_c=num_c,
            jny_l=jny_l,
        )

        return freq
