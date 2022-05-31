from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.prod_ctx import ProdCtx
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProdL")


@attr.s(auto_attribs=True)
class ProdL:
    """
    Attributes:
        name (str):
        ico_x (float):
        cls (float):
        number (Union[Unset, str]):
        opr_x (Union[Unset, float]):
        prod_ctx (Union[Unset, ProdCtx]):
        add_name (Union[Unset, str]):
        name_s (Union[Unset, str]):
        match_id (Union[Unset, str]):
    """

    name: str
    ico_x: float
    cls: float
    number: Union[Unset, str] = UNSET
    opr_x: Union[Unset, float] = UNSET
    prod_ctx: Union[Unset, ProdCtx] = UNSET
    add_name: Union[Unset, str] = UNSET
    name_s: Union[Unset, str] = UNSET
    match_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        ico_x = self.ico_x
        cls = self.cls
        number = self.number
        opr_x = self.opr_x
        prod_ctx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prod_ctx, Unset):
            prod_ctx = self.prod_ctx.to_dict()

        add_name = self.add_name
        name_s = self.name_s
        match_id = self.match_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "icoX": ico_x,
                "cls": cls,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if opr_x is not UNSET:
            field_dict["oprX"] = opr_x
        if prod_ctx is not UNSET:
            field_dict["prodCtx"] = prod_ctx
        if add_name is not UNSET:
            field_dict["addName"] = add_name
        if name_s is not UNSET:
            field_dict["nameS"] = name_s
        if match_id is not UNSET:
            field_dict["matchId"] = match_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        ico_x = d.pop("icoX")

        cls = d.pop("cls")

        number = d.pop("number", UNSET)

        opr_x = d.pop("oprX", UNSET)

        _prod_ctx = d.pop("prodCtx", UNSET)
        prod_ctx: Union[Unset, ProdCtx]
        if isinstance(_prod_ctx, Unset):
            prod_ctx = UNSET
        else:
            prod_ctx = ProdCtx.from_dict(_prod_ctx)

        add_name = d.pop("addName", UNSET)

        name_s = d.pop("nameS", UNSET)

        match_id = d.pop("matchId", UNSET)

        prod_l = cls(
            name=name,
            ico_x=ico_x,
            cls=cls,
            number=number,
            opr_x=opr_x,
            prod_ctx=prod_ctx,
            add_name=add_name,
            name_s=name_s,
            match_id=match_id,
        )

        return prod_l
