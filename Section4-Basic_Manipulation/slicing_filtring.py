import pandas as pb
import numpy as np

df = pb.read_csv('AB_NYC_2019.csv')

# print(df)

# TESTES NEW
# print(df.filter(item=['name']))
# print(df.filter(item=['name']))
#
# print(df.filter(['name', 'id']))

# ------------------------------------------------------------

# Filter
#  df + column name
# print(df["host_name"])
# print(df["host_name","id"])

# print(df.host_name)


# filtering on rows, mask filtering

print(
    df[df.host_name == "Taz"]
)
