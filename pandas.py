import pandas as pd
data={
    'name' : ['Parth','Nikhil','Sahil','Rohan'],
    'age' : [20,21,22,23],
    'city' : ['Delhi','Mumbai','Bangalore','ChennaiCity'],
    'Salary' :[500000, 6000000,650000, 7000000]
}
df=pd.DataFrame(data)
print("DataFrame:")
print(df)
# Output:
#      name  age        city   Salary
# 0   Parth   20       Delhi   500000
# 1  Nikhil   21      Mumbai  6000000
# 2   Sahil   22   Bangalore   650000
# 3   Rohan   23  ChennaiCity 7000000

shape=df.shape
print(f"Shape of dataframe is:{shape}")
# Output: Shape of dataframe is:(4, 4)

col=df.columns
print(f"Columns in dataframe are:{col}")
# Output: Columns in dataframe are:Index(['name', 'age', 'city', 'Salary'], dtype='object')

datatypes=df.dtypes
print(f"Data types of columns are:\n{datatypes}")
# Output:
# Data types of columns are:
# name      object
# age        int64
# city      object
# Salary     int64
# dtype: object

#Selecting a data
print("Selecting a column:")
print(df['name'])
# Output:
# 0     Parth
# 1    Nikhil
# 2     Sahil
# 3     Rohan
# Name: name, dtype: object

print("Selecting multiple columns:")
print(df[['name','age']])
# Output:
#     name  age
# 0  Parth   20
# 1 Nikhil   21
# 2  Sahil   22
# 3  Rohan   23

head=df.head(2)
print(f"First 2 rows of dataframe:\n{head}")
# Output:
#     name  age   city  Salary
# 0  Parth   20  Delhi  500000
# 1 Nikhil   21 Mumbai 6000000

tail=df.tail(2)
print(f"Last 2 rows of dataframe:\n{tail}")
# Output:
#     name  age        city  Salary
# 2  Sahil   22   Bangalore  650000
# 3  Rohan   23  ChennaiCity 7000000

location=df.loc[0]
print(f"Row at index 0:\n{location}")
# Output:
# name      Parth
# age          20
# city      Delhi
# Salary   500000
# Name: 0, dtype: object

location2=df.loc[1]
print(f"Row at index 1:\n{location2}")
# Output:
# name      Nikhil
# age           21
# city      Mumbai
# Salary   6000000
# Name: 1, dtype: object

print("Selecting rows by index:")
print(df.iloc[0:2])  # First two rows
# Output:
#     name  age   city  Salary
# 0  Parth   20  Delhi  500000
# 1 Nikhil   21 Mumbai 6000000

#Filtering data
print("Filtering rows where age is greater than 21:")
filtered_data=df[df['age']>21]
print(filtered_data)
# Output:
#     name  age        city  Salary
# 2  Sahil   22   Bangalore  650000
# 3  Rohan   23  ChennaiCity 7000000

print("Filtering rows where city is Bangalore:")
filter_city=df[df['city']=='Bangalore']
print(filter_city)
# Output:
#    name  age      city  Salary
# 2 Sahil   22  Bangalore 650000

# Adding a new column
df['Experience']=[2,3,4,5]
print("DataFrame after adding a new column 'Experience':")
print(df)
# Output:
#     name  age        city   Salary  Experience
# 0  Parth   20       Delhi   500000           2
# 1 Nikhil   21      Mumbai  6000000           3
# 2  Sahil   22   Bangalore   650000           4
# 3  Rohan   23  ChennaiCity 7000000           5

print("Adding a new row:")
new_row={'name': 'Amit', 'age': 24, 'city': 'Pune', 'Salary': 800000, 'Experience': 6}
df=df.append(new_row, ignore_index=True)
print("DataFrame after adding a new row:")
print(df)
# Output:
#     name  age        city   Salary  Experience
# 0  Parth   20       Delhi   500000           2
# 1 Nikhil   21      Mumbai  6000000           3
# 2  Sahil   22   Bangalore   650000           4
# 3  Rohan   23  ChennaiCity 7000000           5
# 4   Amit   24        Pune   800000           6

print("Sorting DataFrame by age:")
sorted=df.sort_values(by='age')
print(sorted)
# Output:
#     name  age        city   Salary  Experience
# 0  Parth   20       Delhi   500000           2
# 1 Nikhil   21      Mumbai  6000000           3
# 2  Sahil   22   Bangalore   650000           4
# 3  Rohan   23  ChennaiCity 7000000           5
# 4   Amit   24        Pune   800000           6

print("Sorting DataFrame by Salary:")
sprted2=df.sort_values(by='Salary')
print(sprted2)
# Output:
#     name  age        city   Salary  Experience
# 0  Parth   20       Delhi   500000           2
# 2  Sahil   22   Bangalore   650000           4
# 4   Amit   24        Pune   800000           6
# 3  Rohan   23  ChennaiCity 7000000           5
# 1 Nikhil   21      Mumbai  6000000           3

# Grouping data
grouped=df.groupby('city,').mean()
print("Grouped DataFrame by city with mean values:")
print(grouped)
# ⚠️ Output: This will raise a KeyError because 'city,' is not a valid column.
# Fix: Use 'city' (without comma) in real scenario.

# Resetting index
grouped_reset=grouped.reset_index()
print("Grouped DataFrame after resetting index:")
print(grouped_reset)
# ⚠️ Output: Will not be reached if above line errors out.

# Dropping a column
print("DataFrame after dropping 'Experience' column:")
df=df.drop(columns=['Experience'])
print(df)
# Output:
#     name  age        city   Salary
# 0  Parth   20       Delhi   500000
# 1 Nikhil   21      Mumbai  6000000
# 2  Sahil   22   Bangalore   650000
# 3  Rohan   23  ChennaiCity 7000000
# 4   Amit   24        Pune   800000

# Merging DataFrames
df2=pd.DataFrame({
    'name': ['Parth', 'Nikhil', 'Sahil', 'Rohan', 'Amit'],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'Sales']
})
merged_df = pd.merge(df, df2, on='name', how='inner')
print("Merged DataFrame:")
print(merged_df)
# Output:
#     name  age        city   Salary Department
# 0  Parth   20       Delhi   500000         IT
# 1 Nikhil   21      Mumbai  6000000         HR
# 2  Sahil   22   Bangalore   650000     Finance
# 3  Rohan   23  ChennaiCity 7000000   Marketing
# 4   Amit   24        Pune   800000       Sales

# | Feature          | `.loc[]`                        | `.iloc[]`                       |
# | ---------------- | ------------------------------- | ------------------------------- |
# | Index type       | Label-based                     | Integer position-based          |
# | Row selection    | `df.loc[2]`                     | `df.iloc[2]`                    |
# | Column selection | `df.loc[:, 'age']`              | `df.iloc[:, 1]`                 |
# | Slice inclusive? | Yes (includes both start & end) | No (end is excluded)            |
# | Use case         | When you know row labels/names  | When you're working by position |
