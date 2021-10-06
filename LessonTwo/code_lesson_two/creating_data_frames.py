import numpy
import pandas as pd
import numpy as np

"""
    How to create a new dataframe using Pandas


"""
filename_two = "heart.csv"

df = pd.read_csv(filename_two)

# Using pandas.
df = pd.DataFrame(data={"A": [1, 2, 3], "B": ["Sam", "Alex", "John"]})

print(df.memory_usage())
