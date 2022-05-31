from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.stop_place_identifier import StopPlaceIdentifier
from ...types import Response


def _get_kwargs(
    eva_number: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/stopPlace/v1/{evaNumber}/identifier".format(client.base_url, evaNumber=eva_number)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StopPlaceIdentifier]]:
    if response.status_code == 200:
        response_200 = StopPlaceIdentifier.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StopPlaceIdentifier]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    eva_number: str,
    *,
    client: Client,
) -> Response[Union[Any, StopPlaceIdentifier]]:
    """
    Args:
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[Union[Any, StopPlaceIdentifier]]
    """

    kwargs = _get_kwargs(
        eva_number=eva_number,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    eva_number: str,
    *,
    client: Client,
) -> Optional[Union[Any, StopPlaceIdentifier]]:
    """
    Args:
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[Union[Any, StopPlaceIdentifier]]
    """

    return sync_detailed(
        eva_number=eva_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    eva_number: str,
    *,
    client: Client,
) -> Response[Union[Any, StopPlaceIdentifier]]:
    """
    Args:
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[Union[Any, StopPlaceIdentifier]]
    """

    kwargs = _get_kwargs(
        eva_number=eva_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    eva_number: str,
    *,
    client: Client,
) -> Optional[Union[Any, StopPlaceIdentifier]]:
    """
    Args:
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[Union[Any, StopPlaceIdentifier]]
    """

    return (
        await asyncio_detailed(
            eva_number=eva_number,
            client=client,
        )
    ).parsed
