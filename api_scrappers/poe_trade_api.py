from typing import Any, Dict, List
import requests, json, os

BASE_URL = "https://www.pathofexile.com/api/trade/exchange/Necropolis"
HEADERS = {
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "content-type": "application/json",
    "cookie": "_ga=GA1.1.791790225.1680504239; POESESSID=0493cf67f73b1abdba63d0e90b970b2c; _ga_R6TM1WQ9DW=GS1.1.1714337133.6.1.1714337164.0.0.0",
    "dnt": "1",
    "origin": "https//www.pathofexile.com",
    "priority": "u=1, i",
    "referer": "https//www.pathofexile.com/trade/exchange/Necropolis",
    "sec-ch-ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "x-requested-with": "XMLHttpRequest",
}
COOKIES = {
    "_ga": "GA1.1.791790225.1680504239",
    "POESESSID": "0493cf67f73b1abdba63d0e90b970b2c",
    "_ga_R6TM1WQ9DW": "GS1.1.1714337133.6.1.1714337164.0.0.0",
}


json_payload_template = {
    "query": {  #
        "status": {"option": "online"},  #
        "have": ["divine"],  #
        "want": ["mirror"],
    },  #
    "sort": {"have": "asc"},
    "engine": "new",
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
def get_exchange_trade_search_result(
    have: List[str],  
    want: List[str],  
    status: Dict[str, str],  
    sort: Dict[str, str],  
    engine: str,  
) -> dict:  
    """Get the result of an exchange trade search from PoE Trade API.

    This function queries PoE Trade API and returns the result of an exchange
    trade search with the given parameters.

    Parameters
    ----------
    have : List[str]
        List of item names to have.
    want : List[str]
        List of item names to want.
    status : Dict[str, str]
        Dictionary with the status option.
    sort : Dict[str, str]
        Dictionary with the sort option.
    engine : str
        Name of the search engine to use.

    Returns
    -------
    dict
        JSON response from PoE Trade API.

    """
    data = json_payload_template.copy()
    data["query"]["have"] = have
    data["query"]["want"] = want
    data["query"]["status"] = status
    data["sort"] = sort
    data["engine"] = engine

    response = requests.post(
        BASE_URL,
        params={},
        json=data,
        headers=HEADERS,
        cookies=COOKIES,
    )
    return response.json()


def create_url_payload_exchange(
    have: List[str],  
    want: List[str],):
    data = json_payload_template.copy()
    data["query"]["have"] = have
    data["query"]["want"] = want
    return data