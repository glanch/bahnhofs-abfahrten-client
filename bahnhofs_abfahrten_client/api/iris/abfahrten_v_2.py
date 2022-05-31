from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    eva_number: str,
    *,
    client: Client,
    lookahead: Union[Unset, None, int] = 150,
    lookbehind: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/iris/v2/abfahrten/{evaNumber}".format(client.base_url, evaNumber=eva_number)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "lookahead": lookahead,
        "lookbehind": lookbehind,
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
    eva_number: str,
    *,
    client: Client,
    lookahead: Union[Unset, None, int] = 150,
    lookbehind: Union[Unset, None, int] = 0,
) -> Response[Any]:
    """
    Args:
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        lookahead (Union[Unset, None, int]):  Default: 150.
        lookbehind (Union[Unset, None, int]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        eva_number=eva_number,
        client=client,
        lookahead=lookahead,
        lookbehind=lookbehind,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    eva_number: str,
    *,
    client: Client,
    lookahead: Union[Unset, None, int] = 150,
    lookbehind: Union[Unset, None, int] = 0,
) -> Response[Any]:
    """
    Args:
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        lookahead (Union[Unset, None, int]):  Default: 150.
        lookbehind (Union[Unset, None, int]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        eva_number=eva_number,
        client=client,
        lookahead=lookahead,
        lookbehind=lookbehind,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
