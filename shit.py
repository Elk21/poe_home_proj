import os
import tft_git_scrapper


def get_file_names_in_folder(folder_path):
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]


### TESTING

# print(get_currency_name_by_id(21))
# with open('test.json', 'w+') as f:
#     a= get_currency_overview('Necropolis', 'Currency')
#     json.dump(a, f)

# print(get_item_history('Necropolis', 'BaseType', '109670'))

print(get_file_names_in_folder("d:/code/tft-data-prices/lsc"))


tft_git_scrapper.get_tft_history_files(n=3)
