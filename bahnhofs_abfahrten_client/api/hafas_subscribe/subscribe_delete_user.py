from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.subscr_user_delete_options import SubscrUserDeleteOptions
from ...models.subscr_user_delete_response import SubscrUserDeleteResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SubscrUserDeleteOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/subscribe/deleteUser".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[SubscrUserDeleteResponse]:
    if response.status_code == 200:
        response_200 = SubscrUserDeleteResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SubscrUserDeleteResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SubscrUserDeleteOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[SubscrUserDeleteResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserDeleteOptions):

    Returns:
        Response[SubscrUserDeleteResponse]
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


def sync(
    *,
    client: Client,
    json_body: SubscrUserDeleteOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[SubscrUserDeleteResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserDeleteOptions):

    Returns:
        Response[SubscrUserDeleteResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        profile=profile,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SubscrUserDeleteOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[SubscrUserDeleteResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserDeleteOptions):

    Returns:
        Response[SubscrUserDeleteResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SubscrUserDeleteOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[SubscrUserDeleteResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserDeleteOptions):

    Returns:
        Response[SubscrUserDeleteResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            profile=profile,
        )
    ).parsed
