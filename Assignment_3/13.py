import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 13. Add a column (say total_value) to the dataset which will display the sum of the integer values of each row
data['total_value'] = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].sum(axis=1)
print("\nData Frame with Total Value Column:")
print(data)