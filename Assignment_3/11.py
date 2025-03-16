import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 11. Calculate the sum, mean and mode of a particular column (say petal.length)
print("\nSum, Mean, and Mode of Petal Length:")
print(f"Sum: {data['petal.length'].sum()}")
print(f"Mean: {data['petal.length'].mean()}")
print(f"Mode: {data['petal.length'].mode()[0]}")