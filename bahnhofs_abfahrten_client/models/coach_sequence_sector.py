from typing import Any, Dict, Type, TypeVar

import attr

from ..models.coach_sequence_position import CoachSequencePosition

T = TypeVar("T", bound="CoachSequenceSector")


@attr.s(auto_attribs=True)
class CoachSequenceSector:
    """
    Attributes:
        name (str):
        position (CoachSequencePosition):
    """

    name: str
    position: CoachSequencePosition

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        position = self.position.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        position = CoachSequencePosition.from_dict(d.pop("position"))

        coach_sequence_sector = cls(
            name=name,
            position=position,
        )

        return coach_sequence_sector
