import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 18. Check if a value exists in data frame or not
value_exists = (data == 5.1).any().any()
print("\nCheck if Value 5.1 Exists in Data Frame:")
print(value_exists)