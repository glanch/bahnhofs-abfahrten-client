import datetime
from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    train_number: int,
    eva_number: str,
    departure_date: datetime.datetime,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/oebb/experimental/trainInfo/{trainNumber}/{evaNumber}/{departureDate}".format(
        client.base_url, trainNumber=train_number, evaNumber=eva_number, departureDate=departure_date
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    train_number: int,
    eva_number: str,
    departure_date: datetime.datetime,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        train_number (int):
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        departure_date (datetime.datetime):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_number=train_number,
        eva_number=eva_number,
        departure_date=departure_date,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    train_number: int,
    eva_number: str,
    departure_date: datetime.datetime,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        train_number (int):
        eva_number (str): Usually 7 digits, leading zeros can be omitted Example: 8000105.
        departure_date (datetime.datetime):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_number=train_number,
        eva_number=eva_number,
        departure_date=departure_date,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
