import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 9. Counting the number of counts of each variety
print("\nCount of Each Variety:")
print(data['variety'].value_counts())