from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.subscr_details_response import SubscrDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: str,
    subscribe_id: float,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/subscribe/details".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params: Dict[str, Any] = {
        "userId": user_id,
        "subscribeId": subscribe_id,
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


def _parse_response(*, response: httpx.Response) -> Optional[SubscrDetailsResponse]:
    if response.status_code == 200:
        response_200 = SubscrDetailsResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SubscrDetailsResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    user_id: str,
    subscribe_id: float,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[SubscrDetailsResponse]:
    """
    Args:
        user_id (str):
        subscribe_id (float):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrDetailsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        subscribe_id=subscribe_id,
        profile=profile,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    user_id: str,
    subscribe_id: float,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[SubscrDetailsResponse]:
    """
    Args:
        user_id (str):
        subscribe_id (float):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrDetailsResponse]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        subscribe_id=subscribe_id,
        profile=profile,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: str,
    subscribe_id: float,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[SubscrDetailsResponse]:
    """
    Args:
        user_id (str):
        subscribe_id (float):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrDetailsResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        subscribe_id=subscribe_id,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: str,
    subscribe_id: float,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[SubscrDetailsResponse]:
    """
    Args:
        user_id (str):
        subscribe_id (float):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrDetailsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            subscribe_id=subscribe_id,
            profile=profile,
        )
    ).parsed
