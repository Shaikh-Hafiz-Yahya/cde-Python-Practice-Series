# Arthematic Operators  In Python Pandas:

import pandas as pd

# Add New Columns:
df = pd.DataFrame({'A':[1 , 3 , 5 , 7] , 'B':[2 , 4 , 6 , 8]})
df['C'] = df['A'] + df['B']

print(df)
print(type(df))

# Add New Columns:
dataframe = pd.DataFrame({'A' : ['Apple' , 'Avocado'] , 'B' : ['Blue_Barry' , 'Barries']})
dataframe['C'] = dataframe['A']+dataframe['B']
print(dataframe)

# Add New Columns:
dataframe = pd.DataFrame({'int':[1 , 2 , 3] , 'float':[4.2 , 5.4 , 6.3]})
dataframe['int-float'] = dataframe['int'] - dataframe['float']
print(dataframe)

# Add New Columns:
dataframe = pd.DataFrame({'int':[1 , 2 , 3] , 'float':[4.1 , 5.5 , 6.1]})
dataframe['int*float'] = dataframe['int'] * dataframe['float']
print(dataframe)

# Add New Columns:
dataframe = pd.DataFrame({'int':[1 , 2 , 3] , 'float':[4.1 , 5.5 , 6.1]} , dtype=float)
dataframe['float*float'] = dataframe['int'] * dataframe['float']
print(dataframe)

# Add New Columns:
dataframe = pd.DataFrame({'int':[1 , 2 , 3] , 'float':[4.1 , 5.5 , 6.1]}, index=['n1' , 'n2' , 'n3'])
dataframe['int/float'] = dataframe['int'] / dataframe['float']
print(dataframe)
print(type(dataframe))

dataframe = pd.DataFrame({'Monitor' : ['Blood_Pressure:' , 'Colestrol:'] , 'Treatment' : ['Medicines_Experience' , 'Experiences_Medicines']})
dataframe['Surrogate_End_Points'] = dataframe['Monitor'] + dataframe['Treatment']
print(dataframe)

dataframe = pd.DataFrame({'A':[1 , 2 , 3 , 4 , 5] , 'B':[10 , 20 , 30 , 40 , 50]})
dataframe['Python'] = dataframe['A'] <= 20
dataframe['Python_1'] = dataframe['B'] >= 50
print(dataframe)

print(dataframe['B'][4])