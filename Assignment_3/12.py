import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 12. Extract minimum and maximum value from a column (say petal.length)
print("\nMinimum and Maximum Value of Petal Length:")
print(f"Minimum: {data['petal.length'].min()}")
print(f"Maximum: {data['petal.length'].max()}")