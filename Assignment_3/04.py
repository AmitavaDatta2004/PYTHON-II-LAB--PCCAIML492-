import pandas as pd

data=pd.read_csv("iris.csv")
print("\n10 Random Sample Rows:")
print(data.sample(10))