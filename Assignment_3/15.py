import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 15. Remove the column 'total_value'
data.drop(columns=['total_value'], inplace=True)
print("\nData Frame after Removing Total Value Column:")
print(data)

# Save the modified DataFrame back to the CSV file
data.to_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv', index=False)