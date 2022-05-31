import datetime
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    train_number: int,
    *,
    client: Client,
    departure: datetime.datetime,
    eva_number: Union[Unset, None, str] = UNSET,
    initial_departure: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/reihung/v4/wagen/{trainNumber}".format(client.base_url, trainNumber=train_number)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_departure = departure.isoformat()

    params["departure"] = json_departure

    params["evaNumber"] = eva_number

    json_initial_departure: Union[Unset, None, str] = UNSET
    if not isinstance(initial_departure, Unset):
        json_initial_departure = initial_departure.isoformat() if initial_departure else None

    params["initialDeparture"] = json_initial_departure

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
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
    train_number: int,
    *,
    client: Client,
    departure: datetime.datetime,
    eva_number: Union[Unset, None, str] = UNSET,
    initial_departure: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """Returns the coachSequence at a specific stop for a specific train.
    Works for OEBB stops and DB stops.

    Returns plannedSequence if no real time information is available

    Args:
        train_number (int):
        departure (datetime.datetime):
        eva_number (Union[Unset, None, str]): Usually 7 digits, leading zeros can be omitted
            Example: 8000105.
        initial_departure (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_number=train_number,
        client=client,
        departure=departure,
        eva_number=eva_number,
        initial_departure=initial_departure,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    train_number: int,
    *,
    client: Client,
    departure: datetime.datetime,
    eva_number: Union[Unset, None, str] = UNSET,
    initial_departure: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Any]:
    """Returns the coachSequence at a specific stop for a specific train.
    Works for OEBB stops and DB stops.

    Returns plannedSequence if no real time information is available

    Args:
        train_number (int):
        departure (datetime.datetime):
        eva_number (Union[Unset, None, str]): Usually 7 digits, leading zeros can be omitted
            Example: 8000105.
        initial_departure (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        train_number=train_number,
        client=client,
        departure=departure,
        eva_number=eva_number,
        initial_departure=initial_departure,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
