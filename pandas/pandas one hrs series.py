import pandas as pd

df = pd.read_csv(r'C:\Users\dell\Documents\Python\sales_data_sample.csv' , encoding='latin1')  
print(df)
# important points:
# read_csv() main donoun parameter main sy koe aik bhi encoding chal skti ha.
# 1. encoding='latin1'
# 2. encoding='utf-8

df = pd.read_json(r'C:\Users\dell\Documents\Python\sample_Data.json')
print(df)

# create dataset and build csv file and read_csv(file)
identify_dic = {
    'Name':['Andrew' , 'JOhn' , 'Altman'],
    'age':[30 , 20 , 45],
    'Gender': 1

}

df = pd.DataFrame(identify_dic)
print(df)

build_csv = df.to_csv('Identity.csv' , index=False) #index=False parameter pss hoga 'to_csv()' main

ReadCsvFile = pd.read_csv(r'C:\Users\dell\Documents\Python\Identity.csv')
print(ReadCsvFile)

# create dataset and build_json file and read_json(file)
identify_dic = {
    'Name':['Andrew' , 'JOhn' , 'Altman'],
    'age':[30 , 20 , 45],
    'Gender': 1

}

df = pd.DataFrame(identify_dic)
print(df)

build_json_file = df.to_json('details.json' , index=False) #index parameter pss hoga 'to_csv()' main

ReadJsonFile = pd.read_json(r'C:\Users\dell\Documents\Python\details.json')
print(ReadJsonFile)

# 1. Understand the data set
# 2. Identify the Problems
# 3. Plain next steps

df_read_json = pd.read_json(r'C:\Users\dell\Documents\Python\sample_Data.json')
print(df_read_json)

# head()
print(df_read_json.head())

# tail()
print(df_read_json.tail())

# -----------------------------
# 1- columns , rows?
# 2- what type of?
# 3- missing data

# info() is a method not fn

# 1- number of rows and columns
# 2- column name 
# 3- int64 float64 obj
# non null counts
# 4- non null counts
# 5- memory usage 

df = pd.read_json(r'C:\Users\dell\Documents\Python\sample_Data.json')
print(df.info()) #info() aik trha sy data set ki summary dyta ha


identify_dic = {
    'Name':['Andrew' , 'JOhn' , 'Altman'],
    'age':[30 , 20 , 45],
    'Gender': 1

}

df = pd.DataFrame(identify_dic)
print(df.info()) #info() aik trha sy data set ki summary dyta ha

# Describe()
data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}
df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print('Descriptive Statistics')
print(df.describe())

""" 
1- how big is your dataset
2- what are the names of columns

shape and columns 
 """
data = pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column Name: {df.columns}')

# 1- select sepecific column
# 2- filter rows
# 3- combine multiple conditions

# particular column select in pandas --> using square bracket & access column

# 1- square bracket
# 2- boolean conditions

# selecting columns
# 1- a series
# 2- dataframe multiple columns of data

data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}
df = pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print("Name (Single column return series)")
name = df['Name']
print(name)
# similarly:
print(df['Name'])

# selecting multiple columns
print(df[['Name' , 'Salary']])

data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,18000,199000,250000,39000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}
df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)

high_salary = df[df['Salary'] > 50000]
print("\nEmployee with salary > 50000")
print(high_salary)

# filtering rows salary > 50k & age > 30
filtered = df[(df['Age']>30) & (df['Salary'] > 50000)]  # & --> jb work kre ga k dounoun conditions true hongi
print("\nEmployee age > 30 +  salary > 50000")
print(filtered)

# Using OR condition
filtered_or = df[(df['Age'] > 35) | (df['Performance Source'] > 90)]
print("\nEmployee older than 35 OR performance is > 90")
print(filtered_or)