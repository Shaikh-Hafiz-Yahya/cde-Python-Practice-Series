import pandas as pd

data = [1 , 2 , 3 , 4 , 5]
s = pd.Series(data)
print(s)

# Modify indexing in rows :
s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'])
print(s)
print(type(s))

#using name='' parameter
s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'] , name='py _pandas') 
print(s)
print(type(s))

# Modify dtype
# using  parameter --> dtype= 
# syntax:-   dtype='datatype'
s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'] , dtype=float , name='py_pandas')
print(s)
print(type(s))

s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'] , dtype=str , name='py_pandas')
print(s)
print(type(s))

data = [1.1 , 2.2 , 3.3 , 4.4 , 5.5]
s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'] , name='py')
print(s)

data = [1.1 , 2.2 , 3.3 , 4.4 , 5.5]
s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'] , name='py' , dtype=str)
print(s)

data = [1.0 , 2.0 , 3.0 , 4.0 , 5.0]
s = pd.Series(data , index=['n1' , 'n2' ,'n3' , 'n4' , 'n5'] , dtype=str , name='py')
print(s)
print(type(s))

dic_data = {
    'Name' : ['Umar' , 'Atif' , 'Umar'],
    'Age' : [22 , 26 , 20 , 30],
    'Gender' : 1

}

s = pd.Series(dic_data , dtype=str , name='py')
print(s)
print(type(s))

dic_data = {
    'Name' : ['Umar' , 'Atif' , 'Umar'],
    'Age' : [22 , 26 , 20],
    'Gender' : 1

}

df = pd.DataFrame(dic_data)
print(df)
print(type(df))

df = pd.DataFrame(dic_data , index=[1 , 2 , 3] , dtype=str)
print(df)
print(type(df))

df = pd.DataFrame(dic_data)
print(df)


li = [1 , 3 , 5 , 7]
df = pd.DataFrame(li , dtype=float)
print(df)
print(type(df))

# set Rows index and Column  index 
li = [1 , 3 , 5 , 7]
df = pd.DataFrame(li , dtype=float , index=['a' , 'b' , 'c' , 'd'] , columns=['float_numbers'])
print(df)
print(type(df))

fruits_list = ['apple' , 'banana' , 'cherry' , 'ornage' , ['Red' , 'Yellow' , 'Red' , 'Orange']]
df = pd.DataFrame(fruits_list , index=['A' , 'B' , 'C' , 'O' , 'Fruits colors'] , columns=['Juicy_Fruity'])
print(df)
print(type(df))

fruits_list = ['apple' , 'banana' , 'cherry' , 'ornage' , ['Red' , 'Yellow' , 'Red' , 'Orange']]
s = pd.Series(fruits_list , index=['A' , 'B' , 'C' , 'O' , 'Fruits colors'])
print(s)
print(type(s))

# Two Series sy DataFrame create krein
s1 = pd.Series(12 , index=['1' , '2' , '3'])
s2 = pd.Series(14 , index=['1' , '2' , '3' , '4'])
print(s1+s2)
  
sr1 = pd.Series(12 , index=['1' , '2' , '3'])
sr2 = pd.Series(12 , index=['1' , '2' , '3'])
print(sr1+sr2)

sr1 = pd.Series('12' , index=['1' , '2' , '3'] , name='pandas_py')
sr2 = pd.Series('12' , index=['1' , '2' , '3'])
print(sr1+sr2)

s1 = pd.Series('12' , index=[1 , 2 , 3 ,4] , name='pandas')
s2 = pd.Series('12' , index=[1 , 2 , 3 ,4])
print(s1+s2)

s1 = pd.Series([12 , 13 , 14])
s2 = pd.Series([12 , 13 , 14])
print(s1+s2)

sr1 = pd.Series(12 , index=[1 , 2 ,3])
sr2 = pd.Series(12 , index=[1 , 2 , 3 , 4])
s1_s2 = pd.Series(sr1+sr2)
print(s1_s2)
print(type(s1_s2))

df = pd.DataFrame(s1_s2 , columns=['Float'])
print(df)
print(type(df))

df = pd.DataFrame({'name':['a' , 'b' , 'c'] , 'salary':[100000 , 200000 , 290000]} , index=['R1' , 'R2' , 'R3'] , dtype=str)
print(df)
print(type(df))

df = pd.DataFrame([1 , 2 , 3 , 4 , 5] , index=['a' , 'b' , 'c' , 'd' , 'e'] , columns=['numeric'] , dtype=str)
print(df)
print(type(df))

df = pd.DataFrame('Scipy_TensorFlow_ScikitLearn' , index=[1 , 2 , 3] , columns=['String'])
print(df)

df = pd.DataFrame(1221 , index=[1 , 2 , 3 , 4 , 5] , columns=['numeric'] , dtype=float)
print(df+df)

world_dic = {

    'Countries Name': ['China' , 'India' , 'Albania'],
    'Country Population' : [30.50 , 2.88 , 39.11]

}

df = pd.DataFrame(world_dic)
print(df['Countries Name'])  #method:2
# print(df.Country Population) method:1 --> ye method yahan kaam nahi kre ga 

world_dic = {

    'CountriesName': ['China' , 'India' , 'Albania'],
    'CountryPopulation' : [30.50 , 2.88 , 39.11]

}

df = pd.DataFrame(world_dic , index=['C' , 'I' , 'A'] , dtype=str)
print(df.CountriesName) #method:1 ---> yahan method1 kaam kre ga

print(df['CountriesName'])#method:2
print(type(df['CountriesName']) , type(df)) 

print(df.head(1))

print(df.tail(1))

print(df.sample()) #randomly koe aik row milay gi

print(df.columns)

print(df.index)  #Index(['C', 'I', 'A'], dtype='object')


world_dic = {

    'CountriesName': ['China' , 'India' , 'Albania'],
    'CountryPopulation' : [30.50 , 2.88 , 39.11]

}

df = pd.DataFrame(world_dic)
print(df.index)   #RangeIndex(start=0, stop=3, step=1)

print(df.index)
print(df.columns)
print(df.sample())

print(type(df['CountriesName']))
print(type(df[['CountriesName','CountryPopulation']]))


world_dic = {

    'CountriesName': ['China' , 'India' , 'Albania'],
    'CountryPopulation' : [30.50 , 2.88 , 39.11],
    'AvgHeight' : ['6ft' , '6ft4inch' , '6ft2inch']

}
df = pd.DataFrame(world_dic)

print(df[['CountriesName' , 'AvgHeight']])
print(df)
print('--------------------------')

world_dic = {

    'CountriesName': ['China' , 'India' , 'Albania'],
    'CountryPopulation' : [30.50 , 2.88 , 39.11],
    'AvgHeight' : ['6ft' , '6ft4inch' , '6ft2inch']

}
df = pd.DataFrame(world_dic)
print(df.info())  #info() method dataset ki summary dikhata ha aik trha sy

print(df.describe())

print(df.shape)

print(df.columns)


world_dic = {

    'CountryCode': [10e21 , 200e2 , 400e01],
    'CountryPopulation' : [30.50 , 2.88 , 39.11],
    'AvgHeight' : [6.21 , 5 , 6]

}

df = pd.DataFrame(world_dic)
print(df)
print(df.columns)



world_dic = {

    'CountryCode': 10e21,
    'CountryPopulation' : 30.50,
    'AvgHeight' : 6.21

}
S = pd.Series(world_dic)
print(S)
print(type(df))
print('-----------')

df = pd.DataFrame(S , columns=['Records'])
print(df)
print(type(df))


dic = {
    'A' : 'APPLE',
    'B' : 'BANANA',
    'C' : 'CHerry'
}

s = pd.Series(dic)
print(s)
print(type(s))

df = pd.DataFrame(s , columns=['FRUITS'])
print(df)
print(type(df))

diction = {
    'A' : 0E2,
    'B' : 1E3,
    'C' : 2E6, 
    'D' : 3E4
}

s = pd.Series(diction)
print(s)
print(type(S))


data = {
    'Name':['Ali','Umar','Arif','Hasan','Usman','Farooq','Afnan','Imtiaz'],
    'Age':[20 , 30 , 24 , 21 , 22 , 39 , 35 , 28],
    'Salary':[50000,200000,100000,500000,180000,199000,2500000,390000],
    'Performance Source':[85,90,78,92,88,80,89,91]

}

df = pd.DataFrame(data , index=['idx1' , 'idx2' , 'idx3' , 'idx4' , 'idx5' , 'idx6' , 'idx7' , 'idx8']) 
print(df)

print(df['Name'])
print(type(df) , type(df['Name']))

print(df[['Name' , 'Salary']])
print(type(df) , type(df[['Name' , 'Salary']]))

print(df.Name)
print(df.Salary)
print(type(df.Salary))

print(df['Salary'] > 50000)
print(df['Salary'] < 50000)
print(df['Salary'] >= 50000)
print(df['Salary'] <= 50000)
print(type(df['Salary'] <= 50000))
print('--------------------------------------------')
filterd = df[(df['Salary'] > 50000) & (df['Age'] < 30)] # & --> jb kaam kre ga jb donoun true hon 
print(filterd)
print('--------------------------------------------')
print(df[(df['Salary'] > 1000000) & (df['Age'] > 25)])

print('-------------Empty DataFrame-----------')
print(df[(df['Salary'] > 10000000) & df['Age'] > 25])  
print(type(df[(df['Salary'] > 10000000) & df['Age'] > 25]))

# using OR condition 
print(df[(df['Salary'] > 500000) | (df['Age'] > 40)])
print(type(df[(df['Salary'] > 500000) | (df['Age'] > 40)]))




