import pandas as pd
data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

# add new column in dataset
df['Bonus'] = df['Salary']*0.1  #ten percent increment in salary
print(df)

# using insert method 
# df.insert(loc , 'column_name' , some_data)
df.insert(0 , 'Employee_Id' , [1001 , 1002 , 1003 , 1004 , 1005 , 1006 , 1007 , 1008])
print(df)

# salary update
# increasing salary in 5%   
df['Salary'] = df['Salary'] * 1.05
print(df)


data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

# Remove perticular column 
# using drop()
# df.drop(columns=["Column NAME"] , inplace=True)
print('Modify_Data')
df.drop(columns=['Performance Source'] , inplace=True)
print(df)

# .loc[]
# -Specific location pr jakr kici bhi value ko update kr skty hain
# df.loc[index_row , 'Column Name'] = New Value
df.loc[1 , 'Salary'] = 180000
print(df)

# isnull() Method
# - Data jahan jahan missing ha means None ha wahan 'True' milay ga
data = {
    'Name':['Ali',None,'Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , None , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,None,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

print(df.isnull())

# isnull().sum() method
# kon sy column main kitni values missing ha wahan
data = {
    'Name':['Ali',None,'Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , None , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,None,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())

# - Missing values ko pta krnay k baad do raasty hain 
# value Remove ya fill

# 1. dropna(axis=0 , inplace=True)
# axis=0 means missing values wali rows remove hogi
# axis=1 means missing values wala column remove hoga

df.dropna(axis=0 , inplace=True)
print(df)

# fillna() method
data = {
    'Name':['Ali',None,'Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , None , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,None,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)
df.fillna(0 , inplace=True)  #fill default value
print(df)


# fillna() method
data = {
    'Name':['Ali',None,'Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , None , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,None,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

df.fillna(df['Age'].mean() , inplace=True)
print(df)

# pandas main interpolation aik estimate nikalta ha aik numerical column ki
# yaad rahy sirf numerical column ny
data = {
    'Name':['Ali',None,'Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , None , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,None,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)
# linear , polynomial , time
df.interpolate(method='linear' , axis=0 , inplace=True) #numerical column main missing values ko fill krta ha sequence k hisaab sy
print(df)


datas = {
    'Time':[1,2,3,4,5],
    'Values':[1,None,3,None,5]
}

df = pd.DataFrame(datas)
print(df)

df['Values'] = df['Values'].interpolate(method='linear')
print(df)
"""
USES: interpolate()
1. Time series data
2.numeric data with trends 
3.Avoid droping raws
"""

# single column sort values
# sort_values() 
# syntax:- 
# df.sort_values(by='column name' , ascending=True ya False , inpalce=True)

datas = {
    'Name':['JOHN' , 'ANDREW' , 'EIGEN ROSUM'],
    'Age':[29 , 20 , 23],
    'Gender':1

}

df = pd.DataFrame(datas)
print(df)

df.sort_values(by='Age' , ascending=False , inplace=True) #age decending main chaly gi
print(df)

# sort multiple columns 
datas = {
    'Name':['JOHN' , 'ANDREW' , 'EIGEN ROSUM'],
    'Age':[29 , 20 , 23],
    'Salary':[20000.0 , 100000.0 , 450000.0],
    'Gender':1

}

df = pd.DataFrame(datas)
print(df)
df.sort_values(by=['Age' , 'Salary'] , ascending=[True , False] , inplace=True)
print(df)

# aggregation:
# 1. summary statistics 
# df['column name].mean()
# df['column name].min()
# df['column name'].max()
# df['column name'].sum()

datas = {
    'Name':['JOHN' , 'ANDREW' , 'EIGEN ROSUM'],
    'Age':[29 , 20 , 23],
    'Salary':[20000.0 , 100000.0 , 450000.0],
    'Gender':1

}

df = pd.DataFrame(datas)
print(df)

avg_salary = df['Salary'].mean()
print(avg_salary)

avg_age = df['Age'].mean()
print(avg_age)

min_salary = df['Salary'].min()
print(min_salary)

min_age = df['Age'].min()
print(min_age)

max_salary = df['Salary'].max()
print(max_salary)

max_age = df['Age'].max()
print(max_age)

sum_salary = df['Salary'].sum()
print(sum_salary)

sum_age = df['Age'].sum()
print(sum_age)

sum_age_salary = df[['Age' , 'Salary']].sum()
print(sum_age_salary)
# Age           72.0     
# Salary    570000.0
# dtype: float64       #impotant point: dtype float diya q k python data ka loss nahi krta

# GROUPING:


