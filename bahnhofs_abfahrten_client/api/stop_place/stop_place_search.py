from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.grouped_stop_place import GroupedStopPlace
from ...types import UNSET, Response, Unset


def _get_kwargs(
    search_term: str,
    *,
    client: Client,
    max_: Union[Unset, None, int] = UNSET,
    filter_for_iris: Union[Unset, None, bool] = False,
    grouped_by_sales: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/stopPlace/v1/search/{searchTerm}".format(client.base_url, searchTerm=search_term)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "max": max_,
        "filterForIris": filter_for_iris,
        "groupedBySales": grouped_by_sales,
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
    search_term: str,
    *,
    client: Client,
    max_: Union[Unset, None, int] = UNSET,
    filter_for_iris: Union[Unset, None, bool] = False,
    grouped_by_sales: Union[Unset, None, bool] = False,
) -> Response[List[GroupedStopPlace]]:
    """This might fall back to use HAFAS

    Args:
        search_term (str):
        max_ (Union[Unset, None, int]):
        filter_for_iris (Union[Unset, None, bool]):
        grouped_by_sales (Union[Unset, None, bool]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    kwargs = _get_kwargs(
        search_term=search_term,
        client=client,
        max_=max_,
        filter_for_iris=filter_for_iris,
        grouped_by_sales=grouped_by_sales,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    search_term: str,
    *,
    client: Client,
    max_: Union[Unset, None, int] = UNSET,
    filter_for_iris: Union[Unset, None, bool] = False,
    grouped_by_sales: Union[Unset, None, bool] = False,
) -> Optional[List[GroupedStopPlace]]:
    """This might fall back to use HAFAS

    Args:
        search_term (str):
        max_ (Union[Unset, None, int]):
        filter_for_iris (Union[Unset, None, bool]):
        grouped_by_sales (Union[Unset, None, bool]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    return sync_detailed(
        search_term=search_term,
        client=client,
        max_=max_,
        filter_for_iris=filter_for_iris,
        grouped_by_sales=grouped_by_sales,
    ).parsed


async def asyncio_detailed(
    search_term: str,
    *,
    client: Client,
    max_: Union[Unset, None, int] = UNSET,
    filter_for_iris: Union[Unset, None, bool] = False,
    grouped_by_sales: Union[Unset, None, bool] = False,
) -> Response[List[GroupedStopPlace]]:
    """This might fall back to use HAFAS

    Args:
        search_term (str):
        max_ (Union[Unset, None, int]):
        filter_for_iris (Union[Unset, None, bool]):
        grouped_by_sales (Union[Unset, None, bool]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    kwargs = _get_kwargs(
        search_term=search_term,
        client=client,
        max_=max_,
        filter_for_iris=filter_for_iris,
        grouped_by_sales=grouped_by_sales,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    search_term: str,
    *,
    client: Client,
    max_: Union[Unset, None, int] = UNSET,
    filter_for_iris: Union[Unset, None, bool] = False,
    grouped_by_sales: Union[Unset, None, bool] = False,
) -> Optional[List[GroupedStopPlace]]:
    """This might fall back to use HAFAS

    Args:
        search_term (str):
        max_ (Union[Unset, None, int]):
        filter_for_iris (Union[Unset, None, bool]):
        grouped_by_sales (Union[Unset, None, bool]):

    Returns:
        Response[List[GroupedStopPlace]]
    """

    return (
        await asyncio_detailed(
            search_term=search_term,
            client=client,
            max_=max_,
            filter_for_iris=filter_for_iris,
            grouped_by_sales=grouped_by_sales,
        )
    ).parsed
