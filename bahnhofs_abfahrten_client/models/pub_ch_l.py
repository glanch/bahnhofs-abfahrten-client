from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="PubChL")


@attr.s(auto_attribs=True)
class PubChL:
    """
    Attributes:
        name (str):
        f_date (str):
        f_time (str):
        t_date (str):
        t_time (str):
    """

    name: str
    f_date: str
    f_time: str
    t_date: str
    t_time: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        f_date = self.f_date
        f_time = self.f_time
        t_date = self.t_date
        t_time = self.t_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "fDate": f_date,
                "fTime": f_time,
                "tDate": t_date,
                "tTime": t_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        f_date = d.pop("fDate")

        f_time = d.pop("fTime")

        t_date = d.pop("tDate")

        t_time = d.pop("tTime")

        pub_ch_l = cls(
            name=name,
            f_date=f_date,
            f_time=f_time,
            t_date=t_date,
            t_time=t_time,
        )

        return pub_ch_l
