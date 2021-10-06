import pandas as pd
import numpy as np
import seaborn as sb

df = pd.read_csv('heart.csv')


chest_pain = df.groupby(by='cp').median()

# print(chest_pain)

#chest_pain.plot(x="cp", y="age")
print(chest_pain.plot())
