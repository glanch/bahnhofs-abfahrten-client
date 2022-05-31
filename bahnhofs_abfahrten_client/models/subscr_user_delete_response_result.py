from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SubscrUserDeleteResponseResult")


@attr.s(auto_attribs=True)
class SubscrUserDeleteResponseResult:
    """
    Attributes:
        result_code (str):
    """

    result_code: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_code = self.result_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resultCode": result_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result_code = d.pop("resultCode")

        subscr_user_delete_response_result = cls(
            result_code=result_code,
        )

        subscr_user_delete_response_result.additional_properties = d
        return subscr_user_delete_response_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
