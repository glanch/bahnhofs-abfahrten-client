import datetime
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    station: str,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/v2/arrivalStationBoard".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["station"] = station

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params["profile"] = json_profile

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
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
    station: str,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Used to get all arrivals at a specific stopPlace

    Args:
        station (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        date (Union[Unset, None, datetime.datetime]):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        station=station,
        date=date,
        profile=profile,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    station: str,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Used to get all arrivals at a specific stopPlace

    Args:
        station (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        date (Union[Unset, None, datetime.datetime]):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        station=station,
        date=date,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
