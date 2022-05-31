from typing import Any, Dict, List, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    him_ids: List[str],
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/experimental/himMessages".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_him_ids = him_ids

    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params: Dict[str, Any] = {
        "himIds": json_him_ids,
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
    him_ids: List[str],
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """
    Args:
        him_ids (List[str]):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        him_ids=him_ids,
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
    him_ids: List[str],
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """
    Args:
        him_ids (List[str]):
        profile (Union[Unset, None, AllowedHafasProfile]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        him_ids=him_ids,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)