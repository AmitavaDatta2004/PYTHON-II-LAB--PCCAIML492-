import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 16. Delete the first row of the data frame
data.drop(index=data.index[0], inplace=True)
print("\nData Frame after Deleting First Row:")
print(data)