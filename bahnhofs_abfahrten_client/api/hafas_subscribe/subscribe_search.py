from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.subscr_search_response import SubscrSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    user_id: str,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/subscribe/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["userId"] = user_id

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


def _parse_response(*, response: httpx.Response) -> Optional[SubscrSearchResponse]:
    if response.status_code == 200:
        response_200 = SubscrSearchResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SubscrSearchResponse]:
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
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[SubscrSearchResponse]:
    """
    Args:
        user_id (str):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrSearchResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        profile=profile,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    user_id: str,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[SubscrSearchResponse]:
    """
    Args:
        user_id (str):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrSearchResponse]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        profile=profile,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: str,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[SubscrSearchResponse]:
    """
    Args:
        user_id (str):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrSearchResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: str,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[SubscrSearchResponse]:
    """
    Args:
        user_id (str):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[SubscrSearchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            profile=profile,
        )
    ).parsed
