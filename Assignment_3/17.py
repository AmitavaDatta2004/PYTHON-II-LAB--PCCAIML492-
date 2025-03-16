import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 17. Delete the last row of the data frame
data.drop(index=data.index[-1], inplace=True)
print("\nData Frame after Deleting Last Row:")
print(data)