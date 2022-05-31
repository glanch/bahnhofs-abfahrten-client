from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.wing_definition import WingDefinition
from ...types import Response


def _get_kwargs(
    raw_id_1: str,
    raw_id_2: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/iris/v2/wings/{rawId1}/{rawId2}".format(client.base_url, rawId1=raw_id_1, rawId2=raw_id_2)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[WingDefinition]:
    if response.status_code == 200:
        response_200 = WingDefinition.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[WingDefinition]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    raw_id_1: str,
    raw_id_2: str,
    *,
    client: Client,
) -> Response[WingDefinition]:
    """
    Args:
        raw_id_1 (str):
        raw_id_2 (str):

    Returns:
        Response[WingDefinition]
    """

    kwargs = _get_kwargs(
        raw_id_1=raw_id_1,
        raw_id_2=raw_id_2,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    raw_id_1: str,
    raw_id_2: str,
    *,
    client: Client,
) -> Optional[WingDefinition]:
    """
    Args:
        raw_id_1 (str):
        raw_id_2 (str):

    Returns:
        Response[WingDefinition]
    """

    return sync_detailed(
        raw_id_1=raw_id_1,
        raw_id_2=raw_id_2,
        client=client,
    ).parsed


async def asyncio_detailed(
    raw_id_1: str,
    raw_id_2: str,
    *,
    client: Client,
) -> Response[WingDefinition]:
    """
    Args:
        raw_id_1 (str):
        raw_id_2 (str):

    Returns:
        Response[WingDefinition]
    """

    kwargs = _get_kwargs(
        raw_id_1=raw_id_1,
        raw_id_2=raw_id_2,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    raw_id_1: str,
    raw_id_2: str,
    *,
    client: Client,
) -> Optional[WingDefinition]:
    """
    Args:
        raw_id_1 (str):
        raw_id_2 (str):

    Returns:
        Response[WingDefinition]
    """

    return (
        await asyncio_detailed(
            raw_id_1=raw_id_1,
            raw_id_2=raw_id_2,
            client=client,
        )
    ).parsed
