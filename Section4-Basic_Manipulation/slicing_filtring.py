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
# print(df[df.host_name == "Taz"])

# Will return all showing True or False for each line.
# print((df.host_name == 'Taz'))

# Show the sum of named Taz.
# print((df.host_name == 'Taz').sum())

# Filtering cheap and Quick
# cheap = (df.price < 100) & (df.minimum_nights < 3)
# print(cheap.sum())
# print(cheap.head(4))


# Filtering row and column together
# mask = np.logical_or((df.reviews_per_month > 3), (df.number_of_reviews > 50))
# print(df[~mask].head(2))
# print(df.loc[mask, ["name", 'host_name']])
# print(df.loc[:, ["name", 'host_name']])
# print(df.loc[mask, :])


# Filtering based on index
# print(df.iloc[0, :])
# print(df.iloc[0, 1])
# df2 = df.set_index("id")
# using standard pyton lists methods
# df2 = df2.iloc[1:4, 6:]
# print(df2.iloc[0, :])


# Provided mask helpers
# print(df.loc[df.price.between(100, 300), "price"].head(3))
# to match only 100 and 200.
# print(df.loc[df.price.isin([100, 200]), "price"].head(3))


# Views vs Copy
df2 = df.copy()
# df2['name'][0] = "TESTING"

# print(df2.head(1))

# df2 = df2.loc[df2.index == 0, "name"] = 'TESTING 2'

print((df2[df2.host_name == "John"]))
