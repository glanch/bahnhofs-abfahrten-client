from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.oebb_access import OEBBAccess
from ..models.oebb_platform_info import OEBBPlatformInfo
from ..models.oebb_time_table_info import OEBBTimeTableInfo
from ..models.oebb_train_info import OEBBTrainInfo
from ..models.oebb_train_on_platform import OEBBTrainOnPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="OEBBInfo")


@attr.s(auto_attribs=True)
class OEBBInfo:
    """
    Attributes:
        time_table_info (OEBBTimeTableInfo):
        accessess (List[OEBBAccess]):
        train (Union[Unset, OEBBTrainInfo]):
        train_on_platform (Union[Unset, OEBBTrainOnPlatform]):
        platform (Union[Unset, OEBBPlatformInfo]):
    """

    time_table_info: OEBBTimeTableInfo
    accessess: List[OEBBAccess]
    train: Union[Unset, OEBBTrainInfo] = UNSET
    train_on_platform: Union[Unset, OEBBTrainOnPlatform] = UNSET
    platform: Union[Unset, OEBBPlatformInfo] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        time_table_info = self.time_table_info.to_dict()

        accessess = []
        for accessess_item_data in self.accessess:
            accessess_item = accessess_item_data.to_dict()

            accessess.append(accessess_item)

        train: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.train, Unset):
            train = self.train.to_dict()

        train_on_platform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.train_on_platform, Unset):
            train_on_platform = self.train_on_platform.to_dict()

        platform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "timeTableInfo": time_table_info,
                "accessess": accessess,
            }
        )
        if train is not UNSET:
            field_dict["train"] = train
        if train_on_platform is not UNSET:
            field_dict["trainOnPlatform"] = train_on_platform
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_table_info = OEBBTimeTableInfo.from_dict(d.pop("timeTableInfo"))

        accessess = []
        _accessess = d.pop("accessess")
        for accessess_item_data in _accessess:
            accessess_item = OEBBAccess.from_dict(accessess_item_data)

            accessess.append(accessess_item)

        _train = d.pop("train", UNSET)
        train: Union[Unset, OEBBTrainInfo]
        if isinstance(_train, Unset):
            train = UNSET
        else:
            train = OEBBTrainInfo.from_dict(_train)

        _train_on_platform = d.pop("trainOnPlatform", UNSET)
        train_on_platform: Union[Unset, OEBBTrainOnPlatform]
        if isinstance(_train_on_platform, Unset):
            train_on_platform = UNSET
        else:
            train_on_platform = OEBBTrainOnPlatform.from_dict(_train_on_platform)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, OEBBPlatformInfo]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = OEBBPlatformInfo.from_dict(_platform)

        oebb_info = cls(
            time_table_info=time_table_info,
            accessess=accessess,
            train=train,
            train_on_platform=train_on_platform,
            platform=platform,
        )

        return oebb_info
