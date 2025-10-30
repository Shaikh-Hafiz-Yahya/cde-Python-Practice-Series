# important point:-
# AIk Random data ko sequence vice grop main k sy convert kiya jata ha
# using groupby()

import pandas as  pd

df = pd.DataFrame({
    'Name':['a','b','c','a','b','c','d','a','a','c','d','b','a','d'],
    's_1':[12,14,16,10,17,19,11,22,11,22,20,12,16,18],
    's_2':[22,10,16,11,15,12,9,22,14,22,23,8,3,19]

})
print(df)

var_new = df.groupby('Name')
print(var_new)

for x , y in var_new:
    print(x)
    print(y)
    print()

print('print all a rows')
print(var_new.get_group('a'))
   
print('print all d rows')   
print(var_new.get_group('d'))

# apply aggregation:
# 1.summary statistics
# df['column name].mean()
# df['column name].min()
# df['column name'].max()
# df['column name'].sum()

all_name_mean = var_new.mean() 
print(all_name_mean)
print()

all_name_sum = var_new.sum()
print(all_name_sum)
print()

all_name_min = var_new.min()
print(all_name_min)
print()

all_name_max = var_new.max()
print(all_name_max)
print()

li = list(var_new)
print(li)





