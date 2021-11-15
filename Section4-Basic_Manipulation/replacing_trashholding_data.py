import pandas as pd
import numpy as np

# df = pd.read_csv('PRODUCTS.csv', sep="|")
# print(df.info())
df = pd.read_csv('AB_NYC_2019.csv')
# print(df.info())

"""
    So are at least two main elements

        1 DataFrame
        2 Series


    How to  deal with Nan.
          or
    Replace then for something else.
"""

print((df))

#df = df.dropna()

# Means only drop a row if it has at least 3 NaN.
#df = df.dropna(thresh=3).info()


print(df.info())

# To add a row in conjuntion with a column, use the axis parameter
# with 1 value
# df = df.dropna(subset=["last_review"], axis=0).info()

print(df.columns)

# to use a subset


# to fill a nan with a 0.
# df = df.fillna(0)

print(df)


# Generic Replace
print(df.host_name.replace('John', 'Garibaldo').head(1))

# Thresholding
