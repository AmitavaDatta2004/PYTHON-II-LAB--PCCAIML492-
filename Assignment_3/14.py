import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 14. Rename the column name from variety to variety1 and reverse
data.rename(columns={'variety': 'variety1'}, inplace=True)
print("\nData Frame with Renamed Column (variety to variety1):")
print(data)

# Save the modified DataFrame back to the CSV file
data.to_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv', index=False)

# Rename the column back from variety1 to variety
data.rename(columns={'variety1': 'variety'}, inplace=True)
print("\nData Frame with Renamed Column (variety1 to variety):")
print(data)

# Save the modified DataFrame back to the CSV file again
data.to_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv', index=False)