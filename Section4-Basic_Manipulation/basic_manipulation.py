
#%%
import pandas as pd
import numpy as np
#%%

df = pd.read_csv("AB_NYC_2019.csv")


# This is how we set "id" as a new index
df = df.set_index("id")

# print(df.head(3))


# print(df.name[2539])

df3 = df.groupby("room_type").mean()


# Going back to standard index mode
# df3 = df3.reset_index()
print(df.head(5))