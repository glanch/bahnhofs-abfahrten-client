from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.grouped_stop_place import GroupedStopPlace
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    lat: float,
    lng: float,
    radius: Union[Unset, None, int] = 5000,
    filter_for_iris: Union[Unset, None, bool] = False,
    max_: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/stopPlace/v1/geoSearch".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "lat": lat,
        "lng": lng,
        "radius": radius,
        "filterForIris": filter_for_iris,
        "max": max_,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[GroupedStopPlace]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GroupedStopPlace.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[GroupedStopPlace]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    lat: float,
    lng: float,
    radius: Union[Unset, None, int] = 5000,
    filter_for_iris: Union[Unset, None, bool] = False,
    max_: Union[Unset, None, int] = UNSET,
) -> Response[List[GroupedStopPlace]]:
    """
    Args:
        lat (float):
        lng (float):
        radius (Union[Unset, None, int]):  Default: 5000.
        filter_for_iris (Union[Unset, None, bool]):
        max_ (Union[Unset, None, int]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    kwargs = _get_kwargs(
        client=client,
        lat=lat,
        lng=lng,
        radius=radius,
        filter_for_iris=filter_for_iris,
        max_=max_,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    lat: float,
    lng: float,
    radius: Union[Unset, None, int] = 5000,
    filter_for_iris: Union[Unset, None, bool] = False,
    max_: Union[Unset, None, int] = UNSET,
) -> Optional[List[GroupedStopPlace]]:
    """
    Args:
        lat (float):
        lng (float):
        radius (Union[Unset, None, int]):  Default: 5000.
        filter_for_iris (Union[Unset, None, bool]):
        max_ (Union[Unset, None, int]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    return sync_detailed(
        client=client,
        lat=lat,
        lng=lng,
        radius=radius,
        filter_for_iris=filter_for_iris,
        max_=max_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    lat: float,
    lng: float,
    radius: Union[Unset, None, int] = 5000,
    filter_for_iris: Union[Unset, None, bool] = False,
    max_: Union[Unset, None, int] = UNSET,
) -> Response[List[GroupedStopPlace]]:
    """
    Args:
        lat (float):
        lng (float):
        radius (Union[Unset, None, int]):  Default: 5000.
        filter_for_iris (Union[Unset, None, bool]):
        max_ (Union[Unset, None, int]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    kwargs = _get_kwargs(
        client=client,
        lat=lat,
        lng=lng,
        radius=radius,
        filter_for_iris=filter_for_iris,
        max_=max_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    lat: float,
    lng: float,
    radius: Union[Unset, None, int] = 5000,
    filter_for_iris: Union[Unset, None, bool] = False,
    max_: Union[Unset, None, int] = UNSET,
) -> Optional[List[GroupedStopPlace]]:
    """
    Args:
        lat (float):
        lng (float):
        radius (Union[Unset, None, int]):  Default: 5000.
        filter_for_iris (Union[Unset, None, bool]):
        max_ (Union[Unset, None, int]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            lng=lng,
            radius=radius,
            filter_for_iris=filter_for_iris,
            max_=max_,
        )
    ).parsed
