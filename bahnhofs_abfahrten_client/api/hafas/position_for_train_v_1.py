from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    train_name: str,
    *,
    client: Client,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/v1/positionForTrain/{trainName}".format(client.base_url, trainName=train_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
    train_name: str,
    *,
    client: Client,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Used to find the position of a specific journey. Based on predictions, not GPS.

    Args:
        train_name (str):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_name=train_name,
        client=client,
        profile=profile,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    train_name: str,
    *,
    client: Client,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """Used to find the position of a specific journey. Based on predictions, not GPS.

    Args:
        train_name (str):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_name=train_name,
        client=client,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
