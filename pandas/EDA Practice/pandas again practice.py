import pandas as pd 

data = [1 , 2 , 3 , 4 , 5]
s = pd.Series(data , index=['A' , 'B' , 'C' , 'D' , 'E'] , dtype=float , name='PYTHON_PANDAS')
print(s)

data = {'numeric':[1 , 2 , 3 , 4 , 5]}
df = pd.DataFrame(data)
print(df)
print(type(df))

data = [1 , 2 , 3 , 4 , 5]
df = pd.DataFrame(data , columns=['Numeric'])
print(df)

df = pd.read_csv(r'C:\Users\dell\Documents\Python\stu_data.csv')
print(df)
print(type(df))

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data , index=['index1' , 'index2' , 'index3' , 'index4' , 'index5' , 'index6' , 'index7' , 'index8'])
print(df)
print(df.shape)
print(df.columns)
print(df.Name)
print(type(df.Name) , type(df))
print(df['Name'])
print(df[['Name' , 'Age']])
print(type(df[['Name' , 'Age']]))
print(df.info())
print(df.describe())
print(df['Age'].mean())
print(df.Age.mean())
print(df[['Age' , 'Salary']].mean())
print(type(df[['Age' , 'Salary']]) , type(df[['Age' , 'Salary']].mean()))

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
df.loc[3 , 'Name'] = 'Rauf'
print(df)

df.loc[3 , 'Age'] = 29
print(df)

df.loc[4 , ['Name' , 'Age' , 'Salary' , 'Performance Source']] = ['M.Usman' , 24 , 5900000 , 93]
print(df)

df.loc[0 , ['Name' , 'Age']] = ['M.Ali' , 23]
print(df)

# insert()  ------> column
# syntax:  df.insert(index , 'column name' , data)
df.insert(2 , 'Gender' , 1)
print(df) 

df.loc[0: , 'Gender'] = True
print(df)

df.loc[0: , 'Name'] = ('Imtiaz','Afnan','Farooq','M.Usman','Rauf','Arif','Umar','M.Ali')
print(df)

df.loc[0: , 'Age'] = (28 , 35 , 39 , 24 , 29 , 24 , 30 ,23)
print(df)
print('------------------------------------------')

print('using loc:')
df.loc[6 , ['Name' , 'Age' , 'Gender' , 'Salary' , 'Performance Source']] = ['Anaya' , 26 , False , 4500000 , 99] #yahan double effort lagi
print(df)

# difference b/w loc and iloc

print('using iloc:')                              #Complete row change krny k liyay iloc better way ha
df.iloc[5] = ['Hania' , 27 , False , 400000 , 90] #complete row ko change krta ha
print(df)


data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)
print(type(df))

print(df.shape)
print(df.columns)
print(df['Salary'])
print(df[['Performance Source' , 'Salary']])
print(type(df[['Salary' , 'Performance Source']]))
print(df['Name'])

df.loc[1 , 'Name'] = 'M.Umar'
print(df)

df.loc[3 , ['Name' , 'Age']] = ['Hassan' , 24] 
print(df)

df.iloc[6] = ['Furqan' , 36 , 500000 , 98]
print(df)

print(df.info())
print(df.describe())
print(df.Age.mean()) #method 1
print(df['Age'].mean()) #method 2

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Employee Age':[20 , 30 , 24 , 21 , 22 , 39 , None , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,200000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data)
print(df)

#method#1 yahan fail ho jae ga
print(df['Employee Age'].mean()) #method:2

df.insert(2 , 'Gender' , 1)
print(df)

df.dropna(how='any' , inplace=True)
print(df)


data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq',None,'Imtiaz'],
    'Employee Age':[20 , 30 , 24 , 21 , 22 , 39 , None , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,None,390000],
    'Performance Source':[85,90,78,92,88,80,None,91]

}

df = pd.DataFrame(data)
print(df)

df.dropna(how='all' , inplace=True)
print(df)

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq',None,'Imtiaz'],
    'Employee Age':[20 , 30 , 24 , None , 22 , 39 , 21 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,200000,390000],
    'Performance Source':[85,90,78,92,None,80,77,91]

}

df = pd.DataFrame(data)
print(df)

# how='any' ---> wo rows ko eliminate kre ga jis rows main aik bhi null values ho gi
df.dropna(how='any' , inplace=True)
print(df)
print(df.info())

print(df.sum())
print(df['Employee Age'].sum())
print(df.Salary.sum())
print(df[['Performance Source' , 'Employee Age']].sum())


data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq',None,'Imtiaz'],
    'Employee Age':[20 , 30 , 24 , None , 22 , 39 , 21 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,200000,390000],
    'Performance Source':[85,90,78,92,None,80,77,91]

}
df = pd.DataFrame(data)
df.dropna(axis=0 , inplace=True)
print(df)

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq',None,'Imtiaz'],
    'Employee Age':[20 , 30 , 24 , None , 22 , 39 , 21 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,200000,390000],
    'Performance Source':[85,90,78,92,None,80,77,91]

}
df = pd.DataFrame(data)

df.dropna(axis=1 , inplace=True)
print(df)
print(df.info())

df.insert(0 , 'Name' , 'xyz')
print(df)
print(type(df))
print(df.info())

data = {'numeric':[1 , None , 3 , None , 5]}
df = pd.DataFrame(data , index=['a' , 'b' , 'c' , 'd' , 'e'])
print(df)

df.fillna(0 , inplace=True)
print(df)

data = {'numeric':[1 , None , 3 , None , 5]}
df = pd.DataFrame(data , index=['a' , 'b' , 'c' , 'd' , 'e'])
print(df)

df.fillna(df['numeric'].sum() , inplace=True)
print(df)

data = {'numeric':[1 , None , 3 , None , 5]}
df = pd.DataFrame(data , index=['a' , 'b' , 'c' , 'd' , 'e'])
print(df)

df.fillna(df['numeric'].mean() , inplace=True)
print(df)

data = {'numeric':[1 , None , 3 , None , 5]}
df = pd.DataFrame(data , index=['a' , 'b' , 'c' , 'd' , 'e'])
print(df)

df.dropna(axis=0 , inplace=True)
print(df)

data = {'numeric':[1 , None , 3 , None , 5],'str':['p' , 'q' , 'r'  , 's' , None]}
df = pd.DataFrame(data , index=['a' , 'b' , 'c' , 'd' , 'e'])
print(df)

df.dropna(how='any' , inplace=True)
print(df)

data = {'numeric':[1 , None , 3 , None , 5],'str':['p' , 'q' , 'r'  , 's' , None]}
df = pd.DataFrame(data , index=['a' , 'b' , 'c' , 'd' , 'e'])
print(df)

df.dropna(how='all' , inplace=True) 
print(df)

li = ['a' , 'b' , {'c' : 'cakes' , 'd' : 'delicious'}]
df = pd.DataFrame(li , columns=['Alphabates'])
print(df)

df.loc[0] = 'a cake'
print(df)

df.loc[2] = [{'Cakes' : 'DELICOUS' , 'MORE_CREAMY' : True}]
print(df)

print('using iloc')
df.iloc[2] = [{'Cakes' : 'DELICOUS' , 'MORE_CREAMY' : True}]
print(df)

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq',None,'Imtiaz'],
    'Employee Age':[20 , 30 , 24 , None , 22 , 39 , 21 , 28],
    'Salary':[50000,None,100000,500000,180000,199000,200000,390000],
    'Performance Source':[85,90,78,92,None,80,77,91]

}
df = pd.DataFrame(data)
print(df)

df.dropna(how='any' , inplace=True)
print(df)

df.iloc[1] = ['Furqan' , 21 , 200000 , 77]
print(df)

df.iloc[2] = ['M.Farooq' , 40 , 190000 , 82]
print(df)

df.loc[3 , 'Name'] = 'M.Yahya'
print(df)

df.iloc[4]  = ['M.YAHYA' , 24 , 1500000 , 91]
print(df)

df.iloc[4] = ['Saad' , 24 , 120000 , 79]
print(df)

df.insert(2 , 'Gender' , True)
print(df)

df['Gender'] = 1
print(df)

print(df['Salary'])
print(df.Salary)

print(df.Salary.sum())
print(df[['Salary' , 'Employee Age']].mean())

print('STANDARD DEVIATION ---> Salary ---> Column')
print(df['Salary'].std())

data = {   
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq',None,'Imtiaz'],
    'Employee Age':[20 , 30 , 24 , 21 , 22 , 39 , None , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,None,390000],
    'Performance Source':[85,90,78,92,88,80,None,91]

}

df = pd.DataFrame(data)
print(df)

