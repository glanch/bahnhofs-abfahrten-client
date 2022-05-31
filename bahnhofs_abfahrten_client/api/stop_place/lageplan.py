from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.lageplan_response import LageplanResponse
from ...types import Response


def _get_kwargs(
    stop_place_name: str,
    eva_number: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/stopPlace/v1/lageplan/{stopPlaceName}/{evaNumber}".format(
        client.base_url, stopPlaceName=stop_place_name, evaNumber=eva_number
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[LageplanResponse]:
    if response.status_code == 200:
        response_200 = LageplanResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[LageplanResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    stop_place_name: str,
    eva_number: str,
    *,
    client: Client,
) -> Response[LageplanResponse]:
    """
    Args:
        stop_place_name (str):
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[LageplanResponse]
    """

    kwargs = _get_kwargs(
        stop_place_name=stop_place_name,
        eva_number=eva_number,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    stop_place_name: str,
    eva_number: str,
    *,
    client: Client,
) -> Optional[LageplanResponse]:
    """
    Args:
        stop_place_name (str):
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[LageplanResponse]
    """

    return sync_detailed(
        stop_place_name=stop_place_name,
        eva_number=eva_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    stop_place_name: str,
    eva_number: str,
    *,
    client: Client,
) -> Response[LageplanResponse]:
    """
    Args:
        stop_place_name (str):
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[LageplanResponse]
    """

    kwargs = _get_kwargs(
        stop_place_name=stop_place_name,
        eva_number=eva_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    stop_place_name: str,
    eva_number: str,
    *,
    client: Client,
) -> Optional[LageplanResponse]:
    """
    Args:
        stop_place_name (str):
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.

    Returns:
        Response[LageplanResponse]
    """

    return (
        await asyncio_detailed(
            stop_place_name=stop_place_name,
            eva_number=eva_number,
            client=client,
        )
    ).parsed
