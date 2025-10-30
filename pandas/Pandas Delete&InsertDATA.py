# Topic:  Delete and Insert DATA: 

import pandas as pd
var = pd.DataFrame({'A':[1 , 3 , 4 , 6] , 'B':[2 , 7 , 12 , 17]})
print(var)

# insert() fn
var.insert(1 , 'Python' , var['A'])
print(var)

# OR 

var.insert(2 , 'Python_1' , [50 , 100 , 200 , 300])
print(var)

# CREATE NEW COLUMN AND STORE FROM COLUMN A --->  FIRTST THREE ROWS
var['Python_12'] = var['A'][:3]
print(var)

# DELETE COLUMN  
# USING POP()
df_dic = pd.DataFrame({'A':[20 , 25 , 30 , 35] , 'B':[40 , 45 , 50 , 55] , 'C':[60 , 65, 70 , 75]})
print(df_dic)

df_dic1 = df_dic.pop('B') #DELETE COLUMN 'B'
print(df_dic1)
print(df_dic)

# DELETE COLUMN  
# USING del keyward
del df_dic['A']
print(df_dic) #DELETE COLUMN 'A' BUT Remaining column is 'C'

