import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.available_br import AvailableBR
from ...models.available_identifier_only import AvailableIdentifierOnly
from ...models.train_run_with_br import TrainRunWithBR
from ...types import UNSET, Response, Unset


def _get_kwargs(
    date: datetime.datetime,
    *,
    client: Client,
    baureihen: Union[Unset, None, List[AvailableBR]] = UNSET,
    identifier: Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]] = UNSET,
    stops_at: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/reihung/v4/runsPerDate/{date}".format(client.base_url, date=date)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_baureihen: Union[Unset, None, List[str]] = UNSET
    if not isinstance(baureihen, Unset):
        if baureihen is None:
            json_baureihen = None
        else:
            json_baureihen = []
            for baureihen_item_data in baureihen:
                baureihen_item = baureihen_item_data.value

                json_baureihen.append(baureihen_item)

    params["baureihen"] = json_baureihen

    json_identifier: Union[Unset, None, List[str]] = UNSET
    if not isinstance(identifier, Unset):
        if identifier is None:
            json_identifier = None
        else:
            json_identifier = []
            for identifier_item_data in identifier:

                if isinstance(identifier_item_data, AvailableIdentifierOnly):
                    identifier_item = identifier_item_data.value

                else:
                    identifier_item = identifier_item_data.value

                json_identifier.append(identifier_item)

    params["identifier"] = json_identifier

    json_stops_at: Union[Unset, None, List[str]] = UNSET
    if not isinstance(stops_at, Unset):
        if stops_at is None:
            json_stops_at = None
        else:
            json_stops_at = stops_at

    params["stopsAt"] = json_stops_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[TrainRunWithBR]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TrainRunWithBR.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[TrainRunWithBR]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    date: datetime.datetime,
    *,
    client: Client,
    baureihen: Union[Unset, None, List[AvailableBR]] = UNSET,
    identifier: Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]] = UNSET,
    stops_at: Union[Unset, None, List[str]] = UNSET,
) -> Response[List[TrainRunWithBR]]:
    """Returns all journeys that run on a specific date. Only works for DB Fernverkehr

    Args:
        date (datetime.datetime):
        baureihen (Union[Unset, None, List[AvailableBR]]):
        identifier (Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]]):
        stops_at (Union[Unset, None, List[str]]):

    Returns:
        Response[List[TrainRunWithBR]]
    """

    kwargs = _get_kwargs(
        date=date,
        client=client,
        baureihen=baureihen,
        identifier=identifier,
        stops_at=stops_at,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    date: datetime.datetime,
    *,
    client: Client,
    baureihen: Union[Unset, None, List[AvailableBR]] = UNSET,
    identifier: Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]] = UNSET,
    stops_at: Union[Unset, None, List[str]] = UNSET,
) -> Optional[List[TrainRunWithBR]]:
    """Returns all journeys that run on a specific date. Only works for DB Fernverkehr

    Args:
        date (datetime.datetime):
        baureihen (Union[Unset, None, List[AvailableBR]]):
        identifier (Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]]):
        stops_at (Union[Unset, None, List[str]]):

    Returns:
        Response[List[TrainRunWithBR]]
    """

    return sync_detailed(
        date=date,
        client=client,
        baureihen=baureihen,
        identifier=identifier,
        stops_at=stops_at,
    ).parsed


async def asyncio_detailed(
    date: datetime.datetime,
    *,
    client: Client,
    baureihen: Union[Unset, None, List[AvailableBR]] = UNSET,
    identifier: Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]] = UNSET,
    stops_at: Union[Unset, None, List[str]] = UNSET,
) -> Response[List[TrainRunWithBR]]:
    """Returns all journeys that run on a specific date. Only works for DB Fernverkehr

    Args:
        date (datetime.datetime):
        baureihen (Union[Unset, None, List[AvailableBR]]):
        identifier (Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]]):
        stops_at (Union[Unset, None, List[str]]):

    Returns:
        Response[List[TrainRunWithBR]]
    """

    kwargs = _get_kwargs(
        date=date,
        client=client,
        baureihen=baureihen,
        identifier=identifier,
        stops_at=stops_at,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    date: datetime.datetime,
    *,
    client: Client,
    baureihen: Union[Unset, None, List[AvailableBR]] = UNSET,
    identifier: Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]] = UNSET,
    stops_at: Union[Unset, None, List[str]] = UNSET,
) -> Optional[List[TrainRunWithBR]]:
    """Returns all journeys that run on a specific date. Only works for DB Fernverkehr

    Args:
        date (datetime.datetime):
        baureihen (Union[Unset, None, List[AvailableBR]]):
        identifier (Union[Unset, None, List[Union[AvailableBR, AvailableIdentifierOnly]]]):
        stops_at (Union[Unset, None, List[str]]):

    Returns:
        Response[List[TrainRunWithBR]]
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
            baureihen=baureihen,
            identifier=identifier,
            stops_at=stops_at,
        )
    ).parsed
