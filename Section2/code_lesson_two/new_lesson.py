from numpy import pi
import pandas as pd
import numbers as np
import pickle

filename = "example_1.csv"
filename_one = "astronauts.csv"
filename_two = "heart.csv"

df = pd.read_csv(filename_two)

# Apresenta a media das colunas "age" e "sex"
# print(df["age"].mean(), df["sex"].mean())

# Printa na tela as colunas 'age' e 'sex' da tabela heart.csv
#print(df["age"], df["sex"])

# print(df.info())
print(
    df.count().sum()
)
