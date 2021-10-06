import pandas as pd
import numpy as np

df = pd.read_csv("astronauts.csv")

# First two row´s
# print(df.head(2))

# Last two row's
# print(df.tail(2))

# X numbers of rand rows. With a chance to see the same row twice.
# print(df.sample(5, replace=True))


# Get dataframe info
# print(df.info())

# Descritive Statictic Info
# print(df.describe())

# Show basic info.
# In this case 316 rows and 19 columns
# print(df.shape)

# Show the correlation between  colunms
# Seens to be a linear correlation.
# print(df.corr())

# Show's all counts of a column.
# print(df["Year"].value_counts())

# To get the Max value of all columns.
print(df.max())



























