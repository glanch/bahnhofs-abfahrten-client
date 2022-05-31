import datetime
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    train_name: str,
    *,
    client: Client,
    stop: Union[Unset, None, str] = UNSET,
    station: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/v2/details/{trainName}".format(client.base_url, trainName=train_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params: Dict[str, Any] = {
        "stop": stop,
        "station": station,
        "date": json_date,
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
    train_name: str,
    *,
    client: Client,
    stop: Union[Unset, None, str] = UNSET,
    station: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """This combines several HAFAS endpoint as well as IRIS data to get the best possible information for a
    specific journey.

    Args:
        train_name (str):
        stop (Union[Unset, None, str]):
        station (Union[Unset, None, str]): Usually 7 digits, leading zeros can be omitted Example:
            8000105.
        date (Union[Unset, None, datetime.datetime]):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_name=train_name,
        client=client,
        stop=stop,
        station=station,
        date=date,
        profile=profile,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    train_name: str,
    *,
    client: Client,
    stop: Union[Unset, None, str] = UNSET,
    station: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.datetime] = UNSET,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """This combines several HAFAS endpoint as well as IRIS data to get the best possible information for a
    specific journey.

    Args:
        train_name (str):
        stop (Union[Unset, None, str]):
        station (Union[Unset, None, str]): Usually 7 digits, leading zeros can be omitted Example:
            8000105.
        date (Union[Unset, None, datetime.datetime]):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_name=train_name,
        client=client,
        stop=stop,
        station=station,
        date=date,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
