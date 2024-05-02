import streamlit as st
import numpy as np
import pandas as pd
import json
import datetime
import os

# data = json.load(open('data/poe_ninja/currency_mapping.csv', 'r'))
df = pd.read_csv("data/poe_ninja/currency_mapping.csv", index_col="id")
df.columns = ["Name", "ID", "Image"]
df = df[["Image", "Name", "ID"]]


def get_currency_history_from_file(currency_id, pay=True):
    folder = "pay" if pay else "receive"

    if not os.path.exists(
        f"data/poe_ninja/currency_history/{folder}/id_{currency_id}.csv"
    ):
        return [], []

    try:
        with open(
            f"data/poe_ninja/currency_history/{folder}/id_{currency_id}.csv", "r"
        ) as f:
            data = pd.read_csv(f)
            data = data[data["value"] > 1]
            price_value = data["value"].to_list()
            price_data = data["daysAgo"].to_list()
            return price_value, price_data
    except Exception as e:
        print(e)
        return [], []


values_receive = []
values_pay = []
values_data_receive = []
values_data_pay = []

for i, row in df.iterrows():
    try:
        values_receive.append(get_currency_history_from_file(i, pay=False)[0])
        values_pay.append(get_currency_history_from_file(i, pay=True)[0])
        values_data_receive.append(get_currency_history_from_file(i, pay=False)[1])
        values_data_pay.append(get_currency_history_from_file(i, pay=True)[1])
    except Exception as e:
        print(i, e)

df["receive"] = values_receive
df["pay"] = values_pay



# line_chart_df_recieive = pd.DataFrame.from_dict(
#     {
#         "price": values_pay[5],
#         "date": values_data_pay[5],
#     }
# )
# line_chart_df_pay = pd.DataFrame.from_dict(
#     {
#         "price": values_pay[5],
#         "date": values_data_pay[5],
#     }
# )


# st.line_chart(
#     data=line_chart_df_pay,
#     x="date",
#     y="price",
#     color=None,
#     width=0,
#     height=0,
#     use_container_width=True,
# )


df_edited = st.data_editor(
    df,
    column_config={
        "Image": st.column_config.ImageColumn("Preview Image", help="shit happens"),
        "pay": st.column_config.AreaChartColumn(
            "Pay",
            width="medium",
            help="123",
        ),
        "receive": st.column_config.AreaChartColumn(
            "Recieve",
            width="medium",
            help="123",
        ),
    },
)















# Display image in cell
# Converting links to html tags
# def path_to_image_html(path):
#     return '<img src="' + path + '" width="60" >'


# def convert_df(input_df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html))


# html = convert_df(df)