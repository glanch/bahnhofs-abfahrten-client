from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Gis")


@attr.s(auto_attribs=True)
class Gis:
    """
    Attributes:
        dist (float):
        dur_s (str):
        dir_geo (float):
        ctx (str):
        gis_prvr (str):
        get_descr (bool):
        get_poly (bool):
    """

    dist: float
    dur_s: str
    dir_geo: float
    ctx: str
    gis_prvr: str
    get_descr: bool
    get_poly: bool

    def to_dict(self) -> Dict[str, Any]:
        dist = self.dist
        dur_s = self.dur_s
        dir_geo = self.dir_geo
        ctx = self.ctx
        gis_prvr = self.gis_prvr
        get_descr = self.get_descr
        get_poly = self.get_poly

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "dist": dist,
                "durS": dur_s,
                "dirGeo": dir_geo,
                "ctx": ctx,
                "gisPrvr": gis_prvr,
                "getDescr": get_descr,
                "getPoly": get_poly,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dist = d.pop("dist")

        dur_s = d.pop("durS")

        dir_geo = d.pop("dirGeo")

        ctx = d.pop("ctx")

        gis_prvr = d.pop("gisPrvr")

        get_descr = d.pop("getDescr")

        get_poly = d.pop("getPoly")

        gis = cls(
            dist=dist,
            dur_s=dur_s,
            dir_geo=dir_geo,
            ctx=ctx,
            gis_prvr=gis_prvr,
            get_descr=get_descr,
            get_poly=get_poly,
        )

        return gis
