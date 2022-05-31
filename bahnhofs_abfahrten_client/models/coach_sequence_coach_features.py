from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoachSequenceCoachFeatures")


@attr.s(auto_attribs=True)
class CoachSequenceCoachFeatures:
    """
    Attributes:
        dining (Union[Unset, bool]):
        wheelchair (Union[Unset, bool]):
        bike (Union[Unset, bool]):
        disabled (Union[Unset, bool]):
        quiet (Union[Unset, bool]):
        info (Union[Unset, bool]):
        family (Union[Unset, bool]):
        toddler (Union[Unset, bool]):
        wifi (Union[Unset, bool]):
        comfort (Union[Unset, bool]):
    """

    dining: Union[Unset, bool] = UNSET
    wheelchair: Union[Unset, bool] = UNSET
    bike: Union[Unset, bool] = UNSET
    disabled: Union[Unset, bool] = UNSET
    quiet: Union[Unset, bool] = UNSET
    info: Union[Unset, bool] = UNSET
    family: Union[Unset, bool] = UNSET
    toddler: Union[Unset, bool] = UNSET
    wifi: Union[Unset, bool] = UNSET
    comfort: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        dining = self.dining
        wheelchair = self.wheelchair
        bike = self.bike
        disabled = self.disabled
        quiet = self.quiet
        info = self.info
        family = self.family
        toddler = self.toddler
        wifi = self.wifi
        comfort = self.comfort

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if dining is not UNSET:
            field_dict["dining"] = dining
        if wheelchair is not UNSET:
            field_dict["wheelchair"] = wheelchair
        if bike is not UNSET:
            field_dict["bike"] = bike
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if quiet is not UNSET:
            field_dict["quiet"] = quiet
        if info is not UNSET:
            field_dict["info"] = info
        if family is not UNSET:
            field_dict["family"] = family
        if toddler is not UNSET:
            field_dict["toddler"] = toddler
        if wifi is not UNSET:
            field_dict["wifi"] = wifi
        if comfort is not UNSET:
            field_dict["comfort"] = comfort

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dining = d.pop("dining", UNSET)

        wheelchair = d.pop("wheelchair", UNSET)

        bike = d.pop("bike", UNSET)

        disabled = d.pop("disabled", UNSET)

        quiet = d.pop("quiet", UNSET)

        info = d.pop("info", UNSET)

        family = d.pop("family", UNSET)

        toddler = d.pop("toddler", UNSET)

        wifi = d.pop("wifi", UNSET)

        comfort = d.pop("comfort", UNSET)

        coach_sequence_coach_features = cls(
            dining=dining,
            wheelchair=wheelchair,
            bike=bike,
            disabled=disabled,
            quiet=quiet,
            info=info,
            family=family,
            toddler=toddler,
            wifi=wifi,
            comfort=comfort,
        )

        return coach_sequence_coach_features
