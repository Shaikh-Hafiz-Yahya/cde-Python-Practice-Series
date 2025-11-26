import pandas as pd

df = pd.read_csv(r'C:\Users\dell\Desktop\exploratory-data-analysis-eda\Day 3 (DataFrames & Aggregating Data)\dataset\titanic.csv')
print(df.head())

print('----------After dropna-----------')
df.dropna(axis=0 , inplace=True)
print(df.head())

df.dropna(axis=1 , inplace=True)
print(df)

df = pd.DataFrame({
    'Name':['a', None , 'c' , 'd' , None , 'f'],
    'Age':[20 , None , 30 , 35 , None , 39],
    'Salary':[200000 , None , 210000 , 300000 ,None , 390000] 
})
print(df)

# jitni bhi null values wali rows hain wo sb eliminate ho joe ga 
df.dropna(how="any" , inplace=True)
print(df)



df = pd.DataFrame({
    'Name':['a', None , 'c' , 'd' , None , 'f'],
    'Age':[20 , None , 30 , 35 , None , 39],
    'Salary':[200000 , None , 210000 , 300000 ,None , None] 
})
print(df)

# how='all' parameter ye krta ha k complete null values wali row ko hi eleiminate krta ha jahan complete row main null values nahi wahan null hi rehna dyga
df.dropna(how='all' , inplace=True)
print(df)



df = pd.DataFrame({
    'Name':['a', None , 'c' , 'd' , None , 'f'],
    'Age':[20 , 26 , 30 , 35 , None , 39],
    'Salary':[200000 , 290000 , 210000 , 300000 ,None , None] 
})
print(df)

# kici bhi row main koe aik bhi null value mila wo complete row hi eliminate ho jae gi 
df.dropna(how='any' , inplace=True)
print(df)

# kici aik particular column ki value remove krnay k liyay
# df.dropna(subset=['Column_name'])
# but jo parti ular column ki null value ko remove kre gy tou wo complete row remove hogi 
df = pd.DataFrame({
    'Name':['a', None , 'c' , 'd' , None , 'f'],
    'Age':[20 , 26 , 30 , 35 , None , 39],
    'Salary':[200000 , 290000 , 210000 , 300000 ,None , None] 
})
print(df)

df.dropna(subset=['Salary'] , inplace=True)
print(df)

# Summary ---> inplace parameter: 
# Common Pandas Methods That Support inplace:-
# Category	Method	Description:
#   Data Cleaning	drop(labels, axis, inplace)	Remove rows or columns
# 	dropna(inplace)	Remove missing values
# 	fillna(value, inplace)	Fill missing values
# 	replace(to_replace, value, inplace)	Replace specific values
# 	rename(mapper, inplace)	Rename columns or index
# 	set_index(keys, inplace)	Set a column as index
# 	reset_index(inplace)	Reset the index to default
# 	sort_values(by, inplace)	Sort by values in a column
# 	sort_index(inplace)	Sort by index
# 	clip(lower, upper, inplace)	Limit values between boundaries
# 	update(other, inplace)	Update values from another DataFrame
# 	astype(dtype, inplace)	Change data types (new in pandas 2.0+)



