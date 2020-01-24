import numpy as np
import pandas as pd
import os

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)

data_path = "C:/Datasets/AirbnbMunich/"
df = pd.read_csv(data_path + "calendar.csv")
data_description = df.describe(include='all')
print(df.head(3))
print(df.tail(3))
print(data_description)
