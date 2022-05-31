from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.coach_sequence_group import CoachSequenceGroup

T = TypeVar("T", bound="CoachSequence")


@attr.s(auto_attribs=True)
class CoachSequence:
    """
    Attributes:
        groups (List[CoachSequenceGroup]):
    """

    groups: List[CoachSequenceGroup]

    def to_dict(self) -> Dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()

            groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = CoachSequenceGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        coach_sequence = cls(
            groups=groups,
        )

        return coach_sequence
