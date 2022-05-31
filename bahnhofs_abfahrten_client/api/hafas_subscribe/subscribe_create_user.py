from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.parsed_subscr_user_response import ParsedSubscrUserResponse
from ...models.subscr_user_create_options import SubscrUserCreateOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SubscrUserCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/subscribe/createUser".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_profile: Union[Unset, None, str] = UNSET
    if not isinstance(profile, Unset):
        json_profile = profile.value if profile else None

    params["profile"] = json_profile

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ParsedSubscrUserResponse]:
    if response.status_code == 200:
        response_200 = ParsedSubscrUserResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ParsedSubscrUserResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SubscrUserCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[ParsedSubscrUserResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserCreateOptions):

    Returns:
        Response[ParsedSubscrUserResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: SubscrUserCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[ParsedSubscrUserResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserCreateOptions):

    Returns:
        Response[ParsedSubscrUserResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        profile=profile,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SubscrUserCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[ParsedSubscrUserResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserCreateOptions):

    Returns:
        Response[ParsedSubscrUserResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SubscrUserCreateOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Optional[ParsedSubscrUserResponse]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (SubscrUserCreateOptions):

    Returns:
        Response[ParsedSubscrUserResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            profile=profile,
        )
    ).parsed
