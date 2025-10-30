# Series: it is defined as a 1D Array that is capable of storing various data types.
# .Series() --> S is capital

#Topic:1 Series()

import pandas as pd

# create data in list
x = [3 , 4 , 5 , 6]

var = pd.Series(x)

print(var)

print(type(var))

print('index num_2 is', var[2])

# Functionality uses:-

# index change:  
var = pd.Series(x , index=['a' , 's' , 'd' , 'f'])
print(var)

# change dtype:  dtype is parameter
var = pd.Series(x , index=['a' , 's' , 'd' , 'f'] , dtype=float)
print(var)

# change class name pandas to python ---> use name parameter
var = pd.Series(x , index=['a' , 's' , 'd' , 'f'] , dtype=float , name='Python')
print(var)

# Create data in dictionary
programming_dict = {

    'Name':['Python' , 'c' , 'c++' , 'java'],
    'Por':[12 , 13 , 14 , 15],
    'rank':[1 , 4 , 3 , 2]
}

var_series = pd.Series(programming_dict)
print(var_series)  
#----------------- 
# Name    [Python, c, c++, java]
# Por           [12, 13, 14, 15]
# rank              [1, 4, 3, 2]
# dtype: object

# - dtype: 'object' aany ka reason mix_data_type ha
# -----------------

# create Series ---> single data 
single_data = pd.Series(20)
print(single_data)
print(type(single_data))

single_data = pd.Series(3.12)
print(single_data)
print(type(single_data))

single_data = pd.Series('Pandas' , index=[1 , 2 , 3 , 4 , 5 , 6])
print(single_data)
print(type(single_data))

# add 2 Series:
s1 = pd.Series(12 , index=[1 ,2 ,3 ,4 ,5 ,6])
s2 = pd.Series(12 , index=[1 ,2 ,3 ,4])

print(s1 + s2)  #dtype: float64

# Difference B/W..

s1 = pd.Series(12)
s2 = pd.Series(12)

print(s1 + s2)   #dtype: int64

#Topic:    DataFrame
programming_dict = {

    'a':[100 , 200 , 300 , 400],
    'b':[12 , 13 , 14 , 15],
    'c':[1 , 4 , 3 , 2]
}

df = pd.DataFrame(programming_dict)
print(df)
print(type(df))

programming_dict = {

    'a':[100 , 200 , 300 , 400],
    'b':[12 , 13 , 14 , 15],
    'c':[1 , 4 , 3 , 2]
}

# call particular column
df = pd.DataFrame(programming_dict , columns=['a'])
print(df)

df = pd.DataFrame(programming_dict , columns=['a' , 'c'])
print(df)

# change index
df = pd.DataFrame(programming_dict , index=['index_0' , 'index_1' , 'index_2' , 'index_3'])
print(df)
print(type(df))

#Topic: get value
programming_dict = {

    'a':[100 , 200 , 300 , 400],
    'b':[12 , 13 , 14 , 15],
    'c':[1 , 4 , 3 , 2]
}

df = pd.DataFrame(programming_dict)
print(df['b'][3])

# change index 
programming_dict = {

    'a':[100 , 200 , 300 , 400],
    'b':[12 , 13 , 14 , 15],
    'c':[1 , 4 , 3 , 2]
}

df = pd.DataFrame(programming_dict , index=['a' , 'b' , 'c' , 'd'])
print(df)
print(type(df))

# create DataFrame list of list
list_of_list = [[1 , 2 , 3 , 4 , 5 ] , [10 , 20 , 30 , 40 , 50]]
df = pd.DataFrame(list_of_list)

print(df)
print(type(df))

# create Series from list of list
list_of_list = [[10 , 20 , 30 , 40] , [100 , 200 , 300 , 400]]
df = pd.Series(list_of_list)

print(df)
print(type(df))

# Two Series sy 1 DataFarme create krain
series_dict_of_list =  {'A':pd.Series([100 , 200 , 300 , 400 , 500]) , 'B':pd.Series([600 , 700 , 800 , 900 , 1000])}
df = pd.DataFrame(series_dict_of_list)

print(df)
print(type(df))
