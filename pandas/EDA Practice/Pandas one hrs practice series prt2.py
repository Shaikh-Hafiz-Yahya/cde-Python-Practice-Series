import pandas as pd
data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}
df = pd.DataFrame(data , index=['i1','i2','i3','i4','i5','i6','i7','i8'])
print(df)

# add new column in dataset
df['Bonus'] = df['Salary']*0.01
print(df)

df['HalfYearBonus'] = df['Bonus']*0.1
print(df)

# Modify Age
df['Age'] = df['Age']+2
print(df)

# Modify Salary
df['Salary'] = df['Salary']+1e2
print(df)

# Modify Bonus
df['Bonus'] = df['Bonus']*1e1
print(df)

df['HalfYearBonus'] = df['HalfYearBonus']*0.001
print(df)
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print('\n----Salary-Series-1D----')
print(df.Salary)
print(type(df.Salary) , type(df))
print(id(df.Salary))

print('--DataFrame--2D--')
print(df[['Salary' , 'Bonus']])
print(type(df[['Salary' , 'Age']]) , type(df['Salary']))

# using insert()
# syntax:
# df.insert(loc , 'Column_Name' , 'some_data')
data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}
df = pd.DataFrame(data , index=['i1','i2','i3','i4','i5','i6','i7','i8'])
print(df)

df.insert(0 , 'Employee_Id' , [10010 , 10011 , 10012 , 10013 , 10014 , 10015 , 10016 , 10017])
print(df)
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.Employee_Id)
print(df['Employee_Id'])
print(type(df['Employee_Id']))
print(df[['Employee_Id' , 'Salary' , 'Name']])
print(type(df[['Employee_Id' , 'Salary' , 'Name']]))

print('-----------')
emp_id = df.Employee_Id
print(emp_id.describe())
print('-----------')
print(emp_id.info())

# Remove particular column
# using drop()
# syntax:
# df.drop(columns=['column_name'] , inplace=True) 
df.drop(columns=['Employee_Id'] , inplace=True)
print(df)

df.drop(columns=['Age' , 'Performance Source'] , inplace=True)
print(df)

print(df.info())
print(df.describe())

li = {
    'SALARY' : [100e00 , 200e02 , 300e2]
}
df = pd.DataFrame(li , index=['s1' , 's2' , 's3'])
print(df)

print(df.describe())
print(df.shape)
print(df.columns)
print(type(df))

# ADD New Column
df['Employee_Bonus'] = df['SALARY']*0.02
print(df)

# Modify 'Employee_Bonus' Column
df['Employee_Bonus'] = df['Employee_Bonus']*0.1
print(df)

# change Salary 
df['SALARY'] = df['SALARY']*0.2
print(df)

df['Employee_Bonus'] = df['Employee_Bonus']*0.1
print(df)
print(type(df))

li = {
    'SALARY' : [100e00 , 200e02 , 300e2]
}

df = pd.DataFrame(li , index=['e1' , 'e2' , 'e3'])
print(df)
df.drop(columns=['SALARY'] , inplace=True)  #Empty DataFrame
print(df)
print(type(df))
print(df.shape) #(3 , 0)
print(df.columns)
print('--Empty--')
print(df.info())
print(df.describe)
print('------------')

data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

# df.loc[] 
# syntax:
# df.loc(index_no , 'column name')
df.loc[1 , 'Age'] = 40
print(df)

df.loc[1 , 'Age'] = False
print(df)

df.iloc[1:2] = ['Imran' , 23 , 30000 , 89]
print(df)

# modify 2nd last row
df.iloc[-2:-1] = ['Imran_Ali' , 29 , 100000 , 92]
print(df)

# modify last row
df.iloc[-1:] = ['Aliyan' , 31 , 120000 , 90]
print(df)

df.insert(2 , 'Gender' , 1)
print(df)
df.loc[0: , 'Gender'] = True
print(df) 

# isnull() Method  ---> bool main dikhata ha data ko 
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
# kon sy column main kitni values missing ha
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
# Row , Column Remove ya fill

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

df.fillna(0.001 , inplace=True)
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
print(df.Age)
df.loc[1 , 'Age'] = df['Age'].mean()
print(df)
# syntax: df.loc[index_no , 'column_name] = data 
df.loc[1 , 'Name'] = 'Areeb' 
print(df)

df.loc[1 , 'Salary'] *= 099e2
print(df)

df.loc[1 , 'Performance Source'] *= 001E1
print(df)

df.iloc[1] = ['Usaid' , 25 , 1900000 , 89.9]
print(df) 
print(f'{type(df)} --Difference_B/W-- {type(df.iloc[1])}')

# SORT VALUES 
# syntax:-
# df.sort_values(by='column_name' , ascending=True ya False , inplace=True)
df.sort_values(by='Age' , ascending=True , inplace=True)
print(df)

df.sort_values(by=['Age' , 'Salary'] , ascending=False , inplace=True)
print(df)










