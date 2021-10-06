import pandas as pd
import numpy as np


# Creating and saving dataset using pandas------------------------------------------
df = pd.DataFrame(np.random.random(size=(100000, 4)), columns=["A", "B", "C", "D"])

# print(df.head())

# That´s how to save a csv file work´s using pandas.
# df.to_csv("save.csv")

# Now a better way, with parameters.....
# %0.4f means four digits after comma using float
# df.to_csv("save.csv", index=False, float_format="%0.4f")

# Now using a pickle
# Is faster then csv
# df.to_pickle("save.pkl")

# Using json
# Good option for REST Lovers.
# df.to_json("save.json")
# ------------------------------------------------------------------------------------

df = pd.read_csv("astronauts.csv")

print(df.head())