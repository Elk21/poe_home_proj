import os, json
from api_scrappers.poe_trade_api import get_exchange_trade_search_result


def save_to_file_poetrade_search_result() -> None:
    """
    Download data from pathofexile.com/api/trade and save it to data/poe_trade

    Returns:
        None
    """
    x = get_exchange_trade_search_result(
        have=["divine"],
        want=["mirror"],
        status={"option": "online"},
        sort={"have": "asc"},
        engine="new",
    )

    if not os.path.exists("data/poe_trade/"):
        os.makedirs("data/poe_trade/")
        print("Created data/poe_trade/")
    with open("data/poe_trade/api_result.json", "w+") as f:
        json.dump(x, f, indent=4)
        print("Saved JSON to data/poe_trade/api_result.json")


if __name__ == "__main__":
    save_to_file_poetrade_search_result()
    pass
