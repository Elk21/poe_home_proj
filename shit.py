import os
import tft_git_scrapper, poe_ninja_api
import pandas as pd
import json
import datetime


def get_file_names_in_folder(folder_path):
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]


# print(get_file_names_in_folder("d:/code/tft-data-prices/lsc"))


### TESTING

# print(get_currency_name_by_id(21))
# with open('test.json', 'w+') as f:
#     a = get_currency_overview('Necropolis', 'Currency')
#     json.dump(a, f)
# print(poe_ninja_api.get_item_history('Necropolis', 'BaseType', '109670'))


# tft_git_scrapper.get_tft_history_files(n=3)


def read_currency_mappings(
    json_path="data/poe_ninja_currency_overview.json",
    csv_path="data/currency_mapping.csv",
    save=False,
):
    """
    This function reads the currency overview json file from the poe.ninja API.
    It normalizes the json into a pandas dataframe, and selects the columns
    of interest, which are id, name, tradeId, and icon.
    It returns the resulting dataframe,
    and saves it to a csv file at the given path.

    Parameters
    ----------
    json_path: str
        Path to the json file to read from.
    csv_path: str
        Path to the csv file to save to.
    save: bool
        Whether to save the dataframe to a csv file.

    Returns
    -------
    df: pandas.DataFrame
        The resulting dataframe.
    """
    with open(json_path) as file:
        dict_ = json.load(file)
        df = pd.json_normalize(dict_["currencyDetails"])
        df = df[["id", "name", "tradeId", "icon"]]
        if save:
            df.to_csv(csv_path, index=False)
    return df


# print(read_currency_mappings(save=True))

# print(poe_ninja_api.get_currency_history('Necropolis', 'Currency', '21'))


def save_df_to_csv(df, folder, name):
    if not os.path.exists(folder):
        os.makedirs(folder)
    df.to_csv(folder + name)


def save_currency_history(data, currency_id, save=False):
    dict_ = json.dumps(data)
    print(dict_)
    df1 = pd.json_normalize(dict_)
    # df2 = pd.json_normalize(dict_["payCurrencyGraphData"])
    if save:
        csv1_path = f"data/poe_ninja/currency_history/receive/id_{currency_id}.csv"
        csv2_path = f"data/poe_ninja/currency_history/pay/id_{currency_id}.csv"
        print("*" * 100)
        save_df_to_csv(df1, csv1_path)
        # save_df_to_csv(df2, csv2_path)


def dump_currency_history(currency_id: int) -> None:
    """
    Fetches currency history from PoeNinja API by id and saves it to a csv file.

    Parameters
    ----------
    currency_id: int
        The id of the currency to fetch history for.
    """
    data = poe_ninja_api.get_currency_history(
        "Necropolis", "Currency", str(currency_id)
    )
    arr = []
    for k, v in data.items():
    # Create a folder name from the first line of the response dictionary key
        folder = "".join([x if not x.isupper() else " " for x in k]).split(" ")[0]

        for i in v:
            unix_timestamp = datetime.date.today() - datetime.timedelta(i["daysAgo"])
            arr.append([i["count"], i["value"], unix_timestamp])
        df = pd.DataFrame(arr, columns=["count", "value", "daysAgo"])
        save_df_to_csv(
            df, f"data/poe_ninja/currency_history/{folder}/", f"id_{currency_id}.csv"
        )


def dump_all_currency_history() -> None:
    """
    Fetches and saves currency history for all ids from 2 to 244.
    """
    for i in range(2, 245):
        print(f"{i=}")
        try:
            dump_currency_history(i)
        except Exception as e:
            print(i, e)

print(123)
dump_all_currency_history()

# data = poe_ninja_api.get_currency_history('Necropolis', 'Currency', str(3))
# save_currency_history(data, 3, save=True)
