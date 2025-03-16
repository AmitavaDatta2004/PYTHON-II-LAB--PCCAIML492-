import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 7. Fetch data from 5th row to 10th row
print("\nData from 5th to 10th Row:")
print(data.iloc[4:10])