# print table 2 to 5 but print (2 by 10,3 by 9, 4 by 8, 5 by 7)

times = 10
for tab in  range(2 , 6):

    for temp in range(times):
        temp += 1
        print(f"{tab}*{temp} = {tab * temp}") 

    times -= 1

# -----------------------------------------
# 10 by 18 , 11 by 16 , 12 by 14 , 13 by 12
times = 18
for table in range(10 , 14):
    for rep in range(times):
        rep += 1
        print(f"{table} * {rep} = {table * rep}")   
    times -= 2 
print('-------------------------------------------')    

#----------------------------------------------------
# print tables only even numbers & Range = (2 by 10 , 4 by 9 , 6 by 8 , 8 by 7 , 10 by 8)
times = 10
for table in range(2 , 11):
    if table % 2 == 0:
        for temp_var in range(times):
            temp_var += 1
            print(f"|{table}| * |{temp_var}| = {table * temp_var}")
            print('________________')
        times -= 1    

#---------------------------------------------------
# print tables --> (1 to 10) & everyone table print --> by 11
for table in range(10):
    table += 1
    if table % 2 == 0:
        for temp_var in range(11):
            temp_var += 1
            print('------------------')
            print(f"|{table}| * |{temp_var}| = |{table * temp_var}|")
            print('------------------')
            
# ---------------------OR-----------------------
start_table = int(input('Start Table'))
end_table = int(input('Stop Table'))
times = int(input('Repetations..'))

for tab in range(start_table , end_table):

    tab += 1
    if tab % 2 != 1:

        for temp_var in range(times):
            temp_var += 1

            print('-|------------------|')
            print(f'|{tab} * {temp_var} = {tab * temp_var}|')
            print('-|------------------|')

        times -= 1    
