from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.crd import Crd
from ..types import UNSET, Unset

T = TypeVar("T", bound="OptionalLocL")


@attr.s(auto_attribs=True)
class OptionalLocL:
    """
    Attributes:
        lid (Union[Unset, str]):
        type (Union[Unset, str]):
        name (Union[Unset, str]):
        ico_x (Union[Unset, float]):
        ext_id (Union[Unset, str]):
        state (Union[Unset, str]):
        crd (Union[Unset, Crd]):
        p_cls (Union[Unset, float]):
        p_ref_l (Union[Unset, List[float]]): Reference to prodL
    """

    lid: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    ico_x: Union[Unset, float] = UNSET
    ext_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    crd: Union[Unset, Crd] = UNSET
    p_cls: Union[Unset, float] = UNSET
    p_ref_l: Union[Unset, List[float]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        lid = self.lid
        type = self.type
        name = self.name
        ico_x = self.ico_x
        ext_id = self.ext_id
        state = self.state
        crd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crd, Unset):
            crd = self.crd.to_dict()

        p_cls = self.p_cls
        p_ref_l: Union[Unset, List[float]] = UNSET
        if not isinstance(self.p_ref_l, Unset):
            p_ref_l = self.p_ref_l

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if lid is not UNSET:
            field_dict["lid"] = lid
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if ico_x is not UNSET:
            field_dict["icoX"] = ico_x
        if ext_id is not UNSET:
            field_dict["extId"] = ext_id
        if state is not UNSET:
            field_dict["state"] = state
        if crd is not UNSET:
            field_dict["crd"] = crd
        if p_cls is not UNSET:
            field_dict["pCls"] = p_cls
        if p_ref_l is not UNSET:
            field_dict["pRefL"] = p_ref_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lid = d.pop("lid", UNSET)

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        ico_x = d.pop("icoX", UNSET)

        ext_id = d.pop("extId", UNSET)

        state = d.pop("state", UNSET)

        _crd = d.pop("crd", UNSET)
        crd: Union[Unset, Crd]
        if isinstance(_crd, Unset):
            crd = UNSET
        else:
            crd = Crd.from_dict(_crd)

        p_cls = d.pop("pCls", UNSET)

        p_ref_l = cast(List[float], d.pop("pRefL", UNSET))

        optional_loc_l = cls(
            lid=lid,
            type=type,
            name=name,
            ico_x=ico_x,
            ext_id=ext_id,
            state=state,
            crd=crd,
            p_cls=p_cls,
            p_ref_l=p_ref_l,
        )

        return optional_loc_l
