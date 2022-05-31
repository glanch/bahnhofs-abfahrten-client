from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    lat: float,
    lng: float,
    max_dist: Union[Unset, None, float] = 1000.0,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/v1/geoStation".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params: Dict[str, Any] = {
        "lat": lat,
        "lng": lng,
        "maxDist": max_dist,
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
    *,
    client: Client,
    lat: float,
    lng: float,
    max_dist: Union[Unset, None, float] = 1000.0,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Can be used to find all stopPlaces within a radius around a specific geo location

    Args:
        lat (float):
        lng (float):
        max_dist (Union[Unset, None, float]):  Default: 1000.0.
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        lat=lat,
        lng=lng,
        max_dist=max_dist,
        profile=profile,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    lat: float,
    lng: float,
    max_dist: Union[Unset, None, float] = 1000.0,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Can be used to find all stopPlaces within a radius around a specific geo location

    Args:
        lat (float):
        lng (float):
        max_dist (Union[Unset, None, float]):  Default: 1000.0.
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        lat=lat,
        lng=lng,
        max_dist=max_dist,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
