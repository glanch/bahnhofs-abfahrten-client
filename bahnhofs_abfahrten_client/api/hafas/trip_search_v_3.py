from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.trip_search_options_v3 import TripSearchOptionsV3
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: TripSearchOptionsV3,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/v3/tripSearch".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params: Dict[str, Any] = {
        "profile": json_profile,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: TripSearchOptionsV3,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Used to find trips [Verbindungssuche]
    A lot of the request options are raw HAFAS and not documented.

    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (TripSearchOptionsV3):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        profile=profile,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: TripSearchOptionsV3,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Used to find trips [Verbindungssuche]
    A lot of the request options are raw HAFAS and not documented.

    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (TripSearchOptionsV3):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)