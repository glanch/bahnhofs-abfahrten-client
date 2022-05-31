from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.stop_place_search_v1_type import StopPlaceSearchV1Type
from ...types import UNSET, Response, Unset


def _get_kwargs(
    search_term: str,
    *,
    client: Client,
    type: Union[Unset, None, StopPlaceSearchV1Type] = StopPlaceSearchV1Type.S,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/v1/stopPlace/{searchTerm}".format(client.base_url, searchTerm=search_term)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params: Dict[str, Any] = {
        "type": json_type,
        "profile": json_profile,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    search_term: str,
    *,
    client: Client,
    type: Union[Unset, None, StopPlaceSearchV1Type] = StopPlaceSearchV1Type.S,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Only uses this for non DB profiles. If you need DB stopPlace search use Operation tagged with
    StopPlace.
    Used to search for stopPlaces based on a name.

    Args:
        search_term (str):
        type (Union[Unset, None, StopPlaceSearchV1Type]):  Default: StopPlaceSearchV1Type.S.
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        search_term=search_term,
        client=client,
        type=type,
        profile=profile,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    search_term: str,
    *,
    client: Client,
    type: Union[Unset, None, StopPlaceSearchV1Type] = StopPlaceSearchV1Type.S,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Only uses this for non DB profiles. If you need DB stopPlace search use Operation tagged with
    StopPlace.
    Used to search for stopPlaces based on a name.

    Args:
        search_term (str):
        type (Union[Unset, None, StopPlaceSearchV1Type]):  Default: StopPlaceSearchV1Type.S.
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        search_term=search_term,
        client=client,
        type=type,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
