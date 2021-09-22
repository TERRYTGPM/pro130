import csv
import pandas as pd

df = pd.read_csv("finalcopy.csv")

del df["Luminosity"]

print(df.shape)

print(list(df))

df.to_csv("e.csv")