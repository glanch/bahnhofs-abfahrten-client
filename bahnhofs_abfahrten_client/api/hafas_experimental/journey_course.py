from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.allowed_hafas_profile import AllowedHafasProfile
from ...models.journey_course_request_options import JourneyCourseRequestOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: JourneyCourseRequestOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hafas/experimental/JourneyCourse".format(client.base_url)

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
    json_body: JourneyCourseRequestOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (JourneyCourseRequestOptions):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    *,
    client: Client,
    json_body: JourneyCourseRequestOptions,
    profile: Union[Unset, None, AllowedHafasProfile] = UNSET,
) -> Response[Any]:
    """
    Args:
        profile (Union[Unset, None, AllowedHafasProfile]):
        json_body (JourneyCourseRequestOptions):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        profile=profile,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
