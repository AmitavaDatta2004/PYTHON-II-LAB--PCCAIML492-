import pandas as pd

# Load the dataset
df = pd.read_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris.csv')

# 1. Print the data frame
print("Data Frame:")
print(df)

# 2. Display top 5 rows
print("\nTop 5 Rows:")
print(df.head())

# 3. Compute statistical analysis on the data frame
print("\nStatistical Analysis:")
print(df.describe())

# 4. Display 10 random sample rows
print("\n10 Random Sample Rows:")
print(df.sample(10))

# 5. Display the number of columns and names of the columns
print("\nNumber of Columns and Names:")
print(df.columns)
print(f"Number of Columns: {len(df.columns)}")

# 6. Print the shape of the dataset
print("\nShape of the Dataset:")
print(df.shape)

# 7. Fetch data from 5th row to 10th row
print("\nData from 5th to 10th Row:")
print(df.iloc[4:10])

# 8. Display data for two columns: petal.length and petal.width
print("\nData for Petal Length and Petal Width:")
print(df[['petal.length', 'petal.width']])

# 9. Counting the number of counts of each variety
print("\nCount of Each Variety:")
print(df['variety'].value_counts())

# 10. Display only those rows whose variety is Setosa
print("\nRows where Variety is Setosa:")
print(df[df['variety'] == 'Setosa'])

# 11. Calculate the sum, mean and mode of a particular column (say petal.length)
print("\nSum, Mean, and Mode of Petal Length:")
print(f"Sum: {df['petal.length'].sum()}")
print(f"Mean: {df['petal.length'].mean()}")
print(f"Mode: {df['petal.length'].mode()[0]}")

# 12. Extract minimum and maximum value from a column (say petal.length)
print("\nMinimum and Maximum Value of Petal Length:")
print(f"Minimum: {df['petal.length'].min()}")
print(f"Maximum: {df['petal.length'].max()}")

# 13. Add a column (say total_value) to the dataset which will display the sum of the integer values of each row
df['total_value'] = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].sum(axis=1)
print("\nData Frame with Total Value Column:")
print(df)

# 14. Rename the column name from variety to variety1 and reverse
df.rename(columns={'variety': 'variety1'}, inplace=True)
print("\nData Frame with Renamed Column (variety to variety1):")
print(df)
df.rename(columns={'variety1': 'variety'}, inplace=True)
print("\nData Frame with Renamed Column (variety1 to variety):")
print(df)

# 15. Remove the column 'total_value'
df.drop(columns=['total_value'], inplace=True)
print("\nData Frame after Removing Total Value Column:")
print(df)

# 16. Delete the first row of the data frame
df.drop(index=df.index[0], inplace=True)
print("\nData Frame after Deleting First Row:")
print(df)

# 17. Delete the last row of the data frame
df.drop(index=df.index[-1], inplace=True)
print("\nData Frame after Deleting Last Row:")
print(df)

# 18. Check if a value exists in data frame or not
value_exists = (df == 5.1).any().any()
print("\nCheck if Value 5.1 Exists in Data Frame:")
print(value_exists)

# 19. Check if a value exists in a particular column or not
value_exists_in_column = (df['sepal.length'] == 5.1).any()
print("\nCheck if Value 5.1 Exists in Sepal Length Column:")
print(value_exists_in_column)

# 20. Write the data frame to another csv file
df.to_csv('d:\\PYTHON\\PYTHON-II-LAB--PCCAIML492-\\Assignment_3\\iris_modified.csv', index=False)
print("\nData Frame Written to iris_modified.csv")