import requests
import json

BASE_URL = "https://poe.ninja/api/data/"
CURRENCY_HISTORY_URL = BASE_URL + "currencyhistory"
CURRENCY_OVERVIEW_URL = BASE_URL + "currencyoverview"
ITEM_OVERVIEW_URL = BASE_URL + "itemoverview"
ITEM_HISTORY_URL = BASE_URL + "itemhistory"

HEADERS = {
    "sec-ch-ua": '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "Referer": "https://poe.ninja/economy/necropolis/currency",
    "DNT": "1",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
}


def tc(func):
    """
    A decorator function that wraps another function to catch any exceptions that may occur during its execution.
    """

    def wrapper(*args, **kwds):
        try:
            return func(*args, **kwds)
        except Exception as e:
            print(e)

    return wrapper


@tc
def get_currency_history(league, type, currency_id):
    """
    A function that retrieves currency history from PoeNinja API
    by making a GET request to CURRENCY_HISTORY_URL endpoint
    with the following parameters:
        league: a league to get currency history for
        type: the type of currency to get history for (e.g. 'Currency', 'Fragment')
        currencyId: the id of the currency to get history for
    The function returns a dictionary with currency history data
    """
    response = requests.get(
        CURRENCY_HISTORY_URL,
        params={"league": league, "type": type, "currencyId": currency_id},
        headers=HEADERS,
    )
    return response.json()


def get_item_history(league, item_type, item_id):
    response = requests.get(
        ITEM_HISTORY_URL,
        params={"league": league, "type": item_type, "itemId": item_id},
        headers=HEADERS,
    )
    return response.json()


def get_currency_overview(league, currency_type):
    response = requests.get(
        CURRENCY_OVERVIEW_URL,
        params={"league": league, "type": currency_type},
        headers=HEADERS,
    )
    return response.json()


def get_items_overview(league, item_type):
    response = requests.get(
        ITEM_OVERVIEW_URL, params={"league": league, "type": item_type}, headers=HEADERS
    )
    return response.json()


def get_currency_history_by_id(league, currency_id):
    """Fetch currency history by league and currency id"""
    return get_currency_history(league, "Currency", currency_id)


def get_currency_overview_by_type(league, currency_type):
    """Fetch currency overview by league and currency type"""
    return get_currency_overview(league, currency_type)


def get_currency_overview_currency(league):
    """Fetch currency overview for given league by currency type"""
    return get_currency_overview_by_type(league, "Currency")


def get_currency_overview_fragment(league):
    """Fetch currency overview for given league by fragment type"""
    return get_currency_overview_by_type(league, "Fragment")


def get_currency_name_by_id(id):
    """
    Retrieves currency name by its id from PoeNinja API currency overview

    Parameters:
        id (int): id of the currency to retrieve name for

    Returns:
        str: name of the currency with given id
    """
    data = get_currency_overview("Necropolis", "Currency")
    for currency in data["currencyDetails"]:
        if currency["id"] == id:
            return currency["name"]
