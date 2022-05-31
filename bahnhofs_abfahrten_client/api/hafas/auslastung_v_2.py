import datetime
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.route_auslastung import RouteAuslastung
from ...types import Response


def _get_kwargs(
    start: str,
    destination: str,
    train_number: str,
    planned_departure_time: datetime.datetime,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/hafas/v2/auslastung/{start}/{destination}/{trainNumber}/{plannedDepartureTime}".format(
        client.base_url,
        start=start,
        destination=destination,
        trainNumber=train_number,
        plannedDepartureTime=planned_departure_time,
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RouteAuslastung]:
    if response.status_code == 200:
        response_200 = RouteAuslastung.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RouteAuslastung]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    start: str,
    destination: str,
    train_number: str,
    planned_departure_time: datetime.datetime,
    *,
    client: Client,
) -> Response[RouteAuslastung]:
    """Provides Auslstaung based on DB Vertrieb HAFAS (DB Navigator).
    Based on a rough estimate, handles first and second class.

    Args:
        start (str):
        destination (str):
        train_number (str):
        planned_departure_time (datetime.datetime):

    Returns:
        Response[RouteAuslastung]
    """

    kwargs = _get_kwargs(
        start=start,
        destination=destination,
        train_number=train_number,
        planned_departure_time=planned_departure_time,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    start: str,
    destination: str,
    train_number: str,
    planned_departure_time: datetime.datetime,
    *,
    client: Client,
) -> Optional[RouteAuslastung]:
    """Provides Auslstaung based on DB Vertrieb HAFAS (DB Navigator).
    Based on a rough estimate, handles first and second class.

    Args:
        start (str):
        destination (str):
        train_number (str):
        planned_departure_time (datetime.datetime):

    Returns:
        Response[RouteAuslastung]
    """

    return sync_detailed(
        start=start,
        destination=destination,
        train_number=train_number,
        planned_departure_time=planned_departure_time,
        client=client,
    ).parsed


async def asyncio_detailed(
    start: str,
    destination: str,
    train_number: str,
    planned_departure_time: datetime.datetime,
    *,
    client: Client,
) -> Response[RouteAuslastung]:
    """Provides Auslstaung based on DB Vertrieb HAFAS (DB Navigator).
    Based on a rough estimate, handles first and second class.

    Args:
        start (str):
        destination (str):
        train_number (str):
        planned_departure_time (datetime.datetime):

    Returns:
        Response[RouteAuslastung]
    """

    kwargs = _get_kwargs(
        start=start,
        destination=destination,
        train_number=train_number,
        planned_departure_time=planned_departure_time,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    start: str,
    destination: str,
    train_number: str,
    planned_departure_time: datetime.datetime,
    *,
    client: Client,
) -> Optional[RouteAuslastung]:
    """Provides Auslstaung based on DB Vertrieb HAFAS (DB Navigator).
    Based on a rough estimate, handles first and second class.

    Args:
        start (str):
        destination (str):
        train_number (str):
        planned_departure_time (datetime.datetime):

    Returns:
        Response[RouteAuslastung]
    """

    return (
        await asyncio_detailed(
            start=start,
            destination=destination,
            train_number=train_number,
            planned_departure_time=planned_departure_time,
            client=client,
        )
    ).parsed
