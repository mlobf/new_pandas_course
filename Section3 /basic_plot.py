
# %%
from importlib.util import set_loader
import pandas as pd
import numpy as np
import seaborn as sb

df = pd.read_csv('heart.csv')

chest_pain = df.groupby(by='cp').median()

# print(chest_pain)

# %%
#chest_pain.plot(x="cp", y="age")
# %%
chest_pain.plot()

# %%
#print(chest_pain.head(5))

# %%
