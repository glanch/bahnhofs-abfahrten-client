from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.available_br import AvailableBR
from ..models.available_identifier_only import AvailableIdentifierOnly
from ..types import UNSET, Unset

T = TypeVar("T", bound="CoachSequenceBaureihe")


@attr.s(auto_attribs=True)
class CoachSequenceBaureihe:
    """
    Attributes:
        name (str):
        identifier (Union[AvailableBR, AvailableIdentifierOnly]):
        baureihe (Union[Unset, AvailableBR]):
    """

    name: str
    identifier: Union[AvailableBR, AvailableIdentifierOnly]
    baureihe: Union[Unset, AvailableBR] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        if isinstance(self.identifier, AvailableIdentifierOnly):
            identifier = self.identifier.value

        else:
            identifier = self.identifier.value

        baureihe: Union[Unset, str] = UNSET
        if not isinstance(self.baureihe, Unset):
            baureihe = self.baureihe.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "identifier": identifier,
            }
        )
        if baureihe is not UNSET:
            field_dict["baureihe"] = baureihe

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_identifier(data: object) -> Union[AvailableBR, AvailableIdentifierOnly]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_available_identifier_type_0 = AvailableIdentifierOnly(data)

                return componentsschemas_available_identifier_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_available_identifier_type_1 = AvailableBR(data)

            return componentsschemas_available_identifier_type_1

        identifier = _parse_identifier(d.pop("identifier"))

        _baureihe = d.pop("baureihe", UNSET)
        baureihe: Union[Unset, AvailableBR]
        if isinstance(_baureihe, Unset):
            baureihe = UNSET
        else:
            baureihe = AvailableBR(_baureihe)

        coach_sequence_baureihe = cls(
            name=name,
            identifier=identifier,
            baureihe=baureihe,
        )

        return coach_sequence_baureihe
