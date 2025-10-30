# Topic:1   Series()
import pandas as pd

l = [1 ,2 ,3 ,4 ,5 ,6 ,7]

l_series = pd.Series(l)

print(l_series)
print(type(l_series))


l = [1 ,2 ,3 ,4 ,5 ,6 ,7]

l_series = pd.Series(l , index=['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g'])

print(l_series)
print(type(l_series))

l = [1 ,2 ,3 ,4 ,5 ,6 ,7]
l_series = pd.Series(l , index=['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g'] , name='Python_Pandas')

print(l_series)
print(type(l_series))


l = [1 ,2 ,3 ,4 ,5 ,6 ,7]
l_series = pd.Series(l , index=['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g'] , name='Python_Pandas' , dtype=float)

print(l_series)
print(type(l_series))


l_series1 = pd.Series(11 , index=[0 ,1 ,2 ,3 ,4 ,5 ,6 ])
l_series2 = pd.Series(11 , index=[0 ,1 ,2 ,3])

print(l_series1 + l_series2)

# Create data in dictionary
programming_dict = {

    'Name':['Python' , 'c' , 'c++' , 'java'],
    'Por':[12 , 13 , 14 , 15],
    'rank':[1 , 4 , 3 , 2]
}

prog_series = pd.Series(programming_dict , name='Python')
print(prog_series)

programming_dict = {

    'Name':['Python' , 'c' , 'c++' , 'java'],
    'Por':[12 , 13 , 14 , 15],
    'rank':[1 , 4 , 3 , 2]
}

prog_series = pd.Series(programming_dict , name='Python')
print(prog_series)

programming_dict = {

    'Name':['Python' , 'c' , 'c++' , 'java'],
    'Por':[12 , 13 , 14 , 15],
    'rank':[1 , 4 , 3 , 2]
}

prog_series = pd.Series(programming_dict , index=['index_0' , 'index_1' , 'index_2'] , name= 'Python_Pandas')

print(prog_series)
print(type(prog_series))

# AGAIN PRACTICE IN COVER TOPICS:    

# 1.Series()
# create Series from list

lst_types_of_fever = ['MALARIA_FEVER' , 'DANGUE_FEVER' , 'LIVER_FEVER/JOINDIST' , 'NORMAL_FEVER']

s = pd.Series(lst_types_of_fever)

print(s)
print(type(s))

# change indexing
lst_types_of_fever = ['MALARIA_FEVER' , 'DANGUE_FEVER' , 'LIVER_FEVER/JOINDIST' , 'NORMAL_FEVER']

s = pd.Series(lst_types_of_fever , index=['case1' , 'case2' , 'case3' , 'case4'])

print(s)
print(type(s))

# name parameter use
lst_types_of_fever = ['MALARIA_FEVER' , 'DANGUE_FEVER' , 'LIVER_FEVER/JOINDIST' , 'NORMAL_FEVER']

s = pd.Series(lst_types_of_fever , index=['SYMPTOMS' , 'SYMPTOMS' , 'SYMPTOMS' , 'SYMPTOMS'] , name='python')

print(s)
print(type(s))

# change datatype using dtype parameter
lst_types_of_fever = ['MALARIA_FEVER' , 'DANGUE_FEVER' , 'LIVER_FEVER/JOINDIST' , 'NORMAL_FEVER']

s = pd.Series(lst_types_of_fever , index=['SYMPTOMS' , 'SYMPTOMS' , 'SYMPTOMS' , 'SYMPTOMS'] , name='python')

print(s)
print(type(s))

# create series from dictionary
dic = {
    'A':0,
    'B':1,
    'C':2,
    'D':3
}

S = pd.Series(dic , name='pYTHON_PANDAS' , dtype=float)

print(S)
print(type(S))

dic = {
    'A':0,
    'B':1,
    'C':2,
    'D':3
}

S = pd.Series(dic , name='pYTHON_PANDAS' , dtype=str) #dtype: object

print(S)
print(type(S))

dic = {
    'A':0,
    'B':1,
    'C':2,
    'D':3
}

S = pd.Series(dic , name='pYTHON_PANDAS')

print(S)
print(type(S))

# Create DataFarme from list
l = [1 , 2 , 3 , 5]

df = pd.DataFrame(l)
print(df)
print(type(df))

l = [1 , 2 , 3 , 5]

df = pd.DataFrame(l ,  index=['a' , 'b' , 'c' , 'd'])
print(df)
print(type(df))

l = [1 , 2 , 3 , 5]

df = pd.DataFrame(l , index=['A' , 'B' , 'C' , 'D'])
print(df)
print(type(df))

l = [1 , 2 , 3 , 5]

df = pd.DataFrame(l , index=['O' , 'T' , 'T' , 'F']) #DataFrame() main 'name' parameter pss nahi hota , sirf Series()fn main pass hota ha
print(df)

l = [1 , 2 , 3 , 5]

df = pd.DataFrame(l , index=['O' , 'T' , 'T' , 'F'] , dtype=float)
print(df)
print(type(df))

dic = {
    'Numbers':[1 , 2 , 3 , 5]
}
    
df = pd.DataFrame(dic , dtype=float , index=['O' , 'T' , 'T' , 'F'])
print(df)

# call  particular column
dic = {
    'A':[0 , 10  , 100],
    'B':[1 , 11 , 101],
    'C':[2 , 12 , 102],
    'D':[3 , 13 , 103]
}

df = pd.DataFrame(dic , columns=['B'])
print(df)
print(type(df))

# change index
dic = {
    'A':[0 , 10  , 100],
    'B':[1 , 11 , 101],
    'C':[2 , 12 , 102],
    'D':[3 , 13 , 103]
}
df = pd.DataFrame(dic , index=['a' , 'b' , 'c'])
print(df)
print(type(df))


dic = {
    'A':[0 , 10  , 100],
    'B':[1 , 11 , 101],
    'C':[2 , 12 , 102],
    'D':[3 , 13 , 103]
}

df = pd.DataFrame(dic , dtype=float , columns=['A' , 'C'])

print(df)
print(type(df))
print(id(df))

# create 2 Series
s1 = pd.Series(100 , index=[1 , 2 , 3 , 4])
s2 = pd.Series(100 , index=[1 , 2])
print(s1+s2)

s1 = pd.Series('100' , index=[1 , 2 , 3 , 4])
s2 = pd.Series('100' , index=[1 , 2])
print(s1+s2)

s1 = pd.Series('100' , index=[1 , 2 , 3 , 4 , 5])
s2 = pd.Series('10' , index=[1 , 2 , 3 ,4 , 5])
print(s1+s2)

s1 = pd.Series('100' , index=[1 , 2 , 3 , 4 , 5])
s2 = pd.Series('10' , index=[1 , 2 , 3 ,4 , 5 , 6])

s3 = s1 + s2
print(s3)
print(type(s3))

ser1 = pd.Series(12 , dtype=float)
ser2 = pd.Series(12 ,dtype=float)

ser3 = ser1 + ser2
print(ser3)
print(type(ser3))

ser1 = pd.Series(12 , dtype=str , index=['string1' , 'string2' , 'string3' , 'string4' , 'string5' , 'string6'])
ser2 = pd.Series(12 , dtype=str , index=['string1' , 'string2' , 'string3' , 'string4'])

add_two_series = ser1 + ser2
print(add_two_series)

# two Series sy DataFarme create krein
sr1 = pd.Series(12 , dtype=str , index=['string1' , 'string2' , 'string3' , 'string4' , 'string5' , 'string6'])
sr2 = pd.Series(12 , dtype=str , index=['string1' , 'string2' , 'string3' , 'string4' , 'string5' , 'string6'])

add_two_series = sr1 + sr2
df = pd.DataFrame(add_two_series)

print(df)
print(type(df))

series1 = pd.Series(12 , index=['index_0' , 'index_2' , 'index_3' , 'index_4' , 'index_5'])
series2 = pd.Series(12 , index=['index_0' , 'index_2' , 'index_3' , 'index_4'])


add_two_series = series1 + series2
df = pd.DataFrame(add_two_series)

print(df)
print(type(df))

series1 = pd.Series(12 , index=['index_0' , 'index_2' , 'index_3' , 'index_4'])
series2 = pd.Series(12 , index=['index_0' , 'index_2' , 'index_3' , 'index_4'])


add_two_series = series1 + series2
df = pd.DataFrame(add_two_series)

print(df)
print(type(df))

# points:
# . Series() main column parameter nahi pss krty (Reason --> Series 1D hoti ha. 'Column hota hi nahi ha only Row')
# . DataFrame() main column parameter pss hota ha. (Reason --> DataFrame 2D hota ha)


dic = {'n' : [1 , 2 , 3 , 4] , 'f':[1.1 , 2.2 , 3.3 , 4.4]}

df = pd.DataFrame(dic , columns=['f'])
print(df)
print(type(df))

#------------------------------------------------------------------------------| 
# . int datatype ko str or float main convert kr skty hain                     |  
#                                                                              | 
# . flot datatype ko str main convert kr skty hain.                            | 
#                                                                              |
# . But float datatype ko int main nahi convert kr skty Q K data ka loss hoga. |
# -----------------------------------------------------------------------------|

dic = {'n' : [1 , 2 , 3 , 4] , 'f':[1.1 , 2.2 , 3.3 , 4.4]}

df = pd.DataFrame(dic , columns=['n'] , dtype=float)
print(df)
print(type(df))

dic = {'n' : [1 , 2 , 3 , 4] , 'f':[1.1 , 2.2 , 3.3 , 4.4]}

df = pd.DataFrame(dic , columns=['f'] , dtype=str , index=['str1','str2','str3','str4'])
print('\nDATA_TYPE_IS_STRING',df)
print(type(s))

#get value means particular element call from column sy 
dic = {'n' : [1 , 2 , 3 , 4] , 'f':[1.1 , 2.2 , 3.3 , 4.4]}

df = pd.DataFrame(dic , dtype=float)

print(df['n'][3])

# -------------------------------------------------------------------------------
world_dic = {

    'Countries' : ['China' , 'India' , 'Albania'],
    'Population' : [30.50 , 2.88 , 39.11]

}
print(world_dic)

# Difference b/w
 
df = pd.DataFrame(world_dic) #2D
print(df)

# call particular column in pandas 
# Method:1  ALMOST USE HOTA HA
print(df['Countries'])

# call particular column in pandas 
# Method:2    
df.Countries


print(type(df) , type(df.Countries))
# <class 'pandas.core.frame.DataFrame'> <class 'pandas.core.series.Series'>


world_dic = {

    'Countries Name': ['China' , 'India' , 'Albania'],
    'Country Population' : [30.50 , 2.88 , 39.11]

}

df = pd.DataFrame(world_dic)

# Method:2
# print(df.Countries Name) ---> (yahan SyntaxError milay ga  QK Column name main space ha is liyay method:1 use hoga is case main)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print(df['Countries Name']) #Method:1

# Dataframe methods:

print(df.head(2))

print(df.tail(2))

# sample()
print(df.sample())  #randomly koe aik Row milay gi

# index
print(df.index)

print(df.columns)

# shape() Rows and Attributes/Features/Columns/variable k bare main btata ha
print(df.shape)

# info() Dataframe ki information dyta ha
print(df.info)


data = [9.9,0.9,0.99,0.899]
s = pd.Series(data , name='py_pandas') #1D
print(s)

data = [2,3,4,5,6]
s = pd.Series(data , dtype=float , name='pandas')
print(s)
print(type(s))

# points:-
# str ko int main nahi convert kr skty
# str ko float main bhi nahi convert krskty
# int ko str main convert kr skty hain 
# float ko str main convert kr skty hain
# float ko int main convert nahi krskty

data = [9.9,0.9,0.99,0.899]
s = pd.Series(data , dtype=str , name='py')
print(s)
print(type(s))

# - columns=[]  coulumns parameter DataFrame main pss hota ha,Series() main nahi 
# REASON: ----> DataFrame 2D ha means is main column bhi hoty ahin rows k saath 

data = ['APPLE','BANANA','ORANGE']
df = pd.DataFrame(data , columns=['Categorical'])#2D
print(df)
print(type(df))

dic_data = {'Name':'john_Andrew' , 'Age':22 , 'Gender':1}

df = pd.Series(dic_data , dtype=str , name='py_pandas')
print(df)

# -------------------------------------------------------------------------------------------
dic_data = {'Name':'john_Andrew' , 'Age':22 , 'Gender':1}
df = pd.DataFrame(dic_data , index=[0,1,2])
print(df)
# difference b/w:
dic_data = {'Name':['john_Andrew' , 'Andrew_NG' , 'Eigen'] , 'Age':[22,30,32] , 'Gender':1}
df = pd.DataFrame(dic_data , index=[0 , 1 , 2])
print(df)
# -------------------------------------------------------------------------------------------

dic_data = {

    'Name':['john_Andrew' , 'Andrew_NG' , 'Eigen'],
    'Age':[22,30,32],
    'Gender':1      
}
df = pd.DataFrame(dic_data , index=['j' , 'A' , 'E'])
print(df)
print(type(df))

dic_data = {
    
    'Name':['john_Andrew' , 'Andrew_NG' , 'Eigen'],
    'Age':[22,30,32],
    'Gender':1      
}

df = pd.DataFrame(dic_data)
print(df)

create_to_csv = df.to_csv('stu_data.csv' , index=False)

read_csv_file = pd.read_csv(r'C:\Users\dell\Documents\Python\stu_data.csv' , dtype=str)
print(read_csv_file)
print(type(read_csv_file) , type(read_csv_file['Age']))
# difference b/w 
print(type(read_csv_file) , type(read_csv_file[['Age' , 'Gender']]))

# ----------------------pandas practice for one hrs series-----------------
# points:-
# .dataset ko read krty time
#  UnicodeError milay tou humain encode='utf-8' ya encode='latin1' pass krein read_csv main

# create dataset and create Series ,create DataFrame , build csv file , read_csv(file) 
data = {
    'Name':['Mike_Hertz' , 'Andrew' , 'John' , 'Altman' , 'adrIENNE'],
    'Age':[30 , 40 , 44 , 29 , 43],
    'Gender':[1 , 1 , 1 , 1 , 0],
    'Discharge Date':['2024-02-02' , '2019-08-26' , '2022-10-07' , '2020-12-18' , '2022-10-09'],
    'Medication':['Paracetamol' , 'Ibuprofen' , 'Aspirin' , 'Ibuprofen' , 'Penicillin'],
    'Test Results':['Normal' , 'Inconclusive' , 'Normal' , 'Abnormal' , ' Abnormal']
}

df = pd.DataFrame(data)
build_csv_file = df.to_csv('My_Health_Data.csv' , index=False)

df = pd.read_csv(r'C:\Users\dell\Documents\Python\My_Health_Data.csv')
print(df)
print(type(df) , type(df['Medication']))

# call particular column using 'Method:1'
name = df['Name']
print(name)

# call particular column using 'Method:2'
print(df['Name'])
print('Call Name_Column:')

#call particular column using 'Method:3'
print(df.Name)

data = {
    'Stu Name':['Mike_Hertz' , 'Andrew' , 'John' , 'Altman' , 'adrIENNE'],
    'Age':[30 , 40 , 44 , 29 , 43],
    'Gender':[1 , 1 , 1 , 1 , 0],
    'Discharge Date':['2024-02-02' , '2019-08-26' , '2022-10-07' , '2020-12-18' , '2022-10-09'],
    'Medication':['Paracetamol' , 'Ibuprofen' , 'Aspirin' , 'Ibuprofen' , 'Penicillin'],
    'Test Results':['Normal' , 'Inconclusive' , 'Normal' , 'Abnormal' , ' Abnormal']
}

df = pd.DataFrame(data)
print(df)

# -stu Name ko call krny k liyay 'Method:3' nahi use ho skta
# Method:1
student_name = df['Stu Name']
print(student_name)

# Method:2
print(df['Stu Name'])


































 


















