from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProdCtx")


@attr.s(auto_attribs=True)
class ProdCtx:
    """
    Attributes:
        name (str):
        cls (float):
        ico_x (float):
        num (Union[Unset, str]):
        match_id (Union[Unset, str]):
        cat_out (Union[Unset, str]):
        cat_out_s (Union[Unset, str]):
        cat_out_l (Union[Unset, str]):
        cat_in (Union[Unset, str]):
        cat_code (Union[Unset, str]):
        admin (Union[Unset, str]):
        line_id (Union[Unset, str]):
        line (Union[Unset, str]):
    """

    name: str
    cls: float
    ico_x: float
    num: Union[Unset, str] = UNSET
    match_id: Union[Unset, str] = UNSET
    cat_out: Union[Unset, str] = UNSET
    cat_out_s: Union[Unset, str] = UNSET
    cat_out_l: Union[Unset, str] = UNSET
    cat_in: Union[Unset, str] = UNSET
    cat_code: Union[Unset, str] = UNSET
    admin: Union[Unset, str] = UNSET
    line_id: Union[Unset, str] = UNSET
    line: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        cls = self.cls
        ico_x = self.ico_x
        num = self.num
        match_id = self.match_id
        cat_out = self.cat_out
        cat_out_s = self.cat_out_s
        cat_out_l = self.cat_out_l
        cat_in = self.cat_in
        cat_code = self.cat_code
        admin = self.admin
        line_id = self.line_id
        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "cls": cls,
                "icoX": ico_x,
            }
        )
        if num is not UNSET:
            field_dict["num"] = num
        if match_id is not UNSET:
            field_dict["matchId"] = match_id
        if cat_out is not UNSET:
            field_dict["catOut"] = cat_out
        if cat_out_s is not UNSET:
            field_dict["catOutS"] = cat_out_s
        if cat_out_l is not UNSET:
            field_dict["catOutL"] = cat_out_l
        if cat_in is not UNSET:
            field_dict["catIn"] = cat_in
        if cat_code is not UNSET:
            field_dict["catCode"] = cat_code
        if admin is not UNSET:
            field_dict["admin"] = admin
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        cls = d.pop("cls")

        ico_x = d.pop("icoX")

        num = d.pop("num", UNSET)

        match_id = d.pop("matchId", UNSET)

        cat_out = d.pop("catOut", UNSET)

        cat_out_s = d.pop("catOutS", UNSET)

        cat_out_l = d.pop("catOutL", UNSET)

        cat_in = d.pop("catIn", UNSET)

        cat_code = d.pop("catCode", UNSET)

        admin = d.pop("admin", UNSET)

        line_id = d.pop("lineId", UNSET)

        line = d.pop("line", UNSET)

        prod_ctx = cls(
            name=name,
            cls=cls,
            ico_x=ico_x,
            num=num,
            match_id=match_id,
            cat_out=cat_out,
            cat_out_s=cat_out_s,
            cat_out_l=cat_out_l,
            cat_in=cat_in,
            cat_code=cat_code,
            admin=admin,
            line_id=line_id,
            line=line,
        )

        return prod_ctx
