import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 8. Display data for two columns: petal.length and petal.width
print("\nData for Petal Length and Petal Width:")
print(data[['petal.length', 'petal.width']])