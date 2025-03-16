import pandas as pd

# Load the dataset
data = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 19. Check if a value exists in a particular column or not
value_exists_in_column = (data['sepal.length'] == 5.1).any()
print("\nCheck if Value 5.1 Exists in Sepal Length Column:")
print(value_exists_in_column)