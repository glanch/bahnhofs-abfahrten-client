from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.parsed_subscr_create_response import ParsedSubscrCreateResponse
from ...models.subscr_create_options import SubscrCreateOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SubscrCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/subscribe/create".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ParsedSubscrCreateResponse]:
    if response.status_code == 200:
        response_200 = ParsedSubscrCreateResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ParsedSubscrCreateResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SubscrCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[ParsedSubscrCreateResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrCreateOptions):

    Returns:
        Response[ParsedSubscrCreateResponse]
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
    json_body: SubscrCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[ParsedSubscrCreateResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrCreateOptions):

    Returns:
        Response[ParsedSubscrCreateResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        profile=profile,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SubscrCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[ParsedSubscrCreateResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrCreateOptions):

    Returns:
        Response[ParsedSubscrCreateResponse]
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
    json_body: SubscrCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[ParsedSubscrCreateResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrCreateOptions):

    Returns:
        Response[ParsedSubscrCreateResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            profile=profile,
        )
    ).parsed
