import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 5. Display the number of columns and names of the columns
print("\nNumber of Columns and Names:")
print(data.columns)
print(f"Number of Columns: {len(data.columns)}")