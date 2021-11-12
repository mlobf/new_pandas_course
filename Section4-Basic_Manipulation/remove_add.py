import pandas as pd
import numpy as np

df = pd.read_csv('astronauts.csv')
# Operational with datas.

# Removing
# Transmuting
# Add


# Modify data type of Columns
# Using the datatime with pandas
birthdate = pd.to_datetime(df['Birth Date'], format='%m/%d/%Y')

print(birthdate.dt.year)
