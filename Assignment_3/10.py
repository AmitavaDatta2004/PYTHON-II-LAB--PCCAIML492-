import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 10. Display only those rows whose variety is Setosa
print("\nRows where Variety is Setosa:")
print(data[data['variety'] == 'Setosa'])