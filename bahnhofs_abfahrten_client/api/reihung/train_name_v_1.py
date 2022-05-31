from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    tz: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/reihung/v1/trainName/{tz}".format(client.base_url, tz=tz)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    tz: str,
    *,
    client: Client,
) -> Response[Union[Any, str]]:
    """
    Args:
        tz (str):

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        tz=tz,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    tz: str,
    *,
    client: Client,
) -> Optional[Union[Any, str]]:
    """
    Args:
        tz (str):

    Returns:
        Response[Union[Any, str]]
    """

    return sync_detailed(
        tz=tz,
        client=client,
    ).parsed


async def asyncio_detailed(
    tz: str,
    *,
    client: Client,
) -> Response[Union[Any, str]]:
    """
    Args:
        tz (str):

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        tz=tz,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    tz: str,
    *,
    client: Client,
) -> Optional[Union[Any, str]]:
    """
    Args:
        tz (str):

    Returns:
        Response[Union[Any, str]]
    """

    return (
        await asyncio_detailed(
            tz=tz,
            client=client,
        )
    ).parsed
