# LOOPS
# syntax for Loop
# for temp_var in iterable():

for temp_var in ([1 , 23 , 45]):
    print(temp_var)

for temp_var in range(10):
    print(temp_var) 

for temp_var in range(5 , 21):
    print(temp_var)

for temp_var in ("HAPPY"):
    print(temp_var)

h = "HAPPY"
for temp_var in h:
    print(temp_var)    

wish = input("WISH YOU...") 
for temp_var in wish:
    print(temp_var)

wish = "HAPPY BIRTHDAY!"
for temp_var in range(5):
        print(temp_var , wish)    

# better way...
wish = "HAPPY BIRTHDAY!"
for temp_var in  range(5):
     print(wish)
# ===========================
for temp_var in range(10):
     print("DEEP LEARNING..")
# ===========================
list_fruits = ["APPLE" , "ORANGE" , "BANANA" , "KIWI"] 
for temp_var in range(6):
     print(temp_var , list_fruits) 

# best way..
list_fruits = ["APPLE" , "ORANGE" , "BANANA" , "KIWI"] 
for temp_var in range(6):
     print(list_fruits)
# ===========================
for temp_var in list_fruits:
     print(temp_var)  

# similarly

for temp_var in ["APPLE" , "ORANGE" , "BANANA" , "KIWI"] :
     print(temp_var)

red = yellow = green = "light.."
for temp_var in [red , yellow , green]:
     print(temp_var)


for temp_var in range(2):
     print(f"Green {green}")

for temp_var in range(2):  
     print("Reinforcement LearningL Depend  On --> (Punishment , Reward)")   

# ========================================================================

end_points = "Heart_Attack"
srrogate_end_points = "Blood_Pressure , Cholestrol"
for temp_var in range(2):
     for concept in ("Not _Surrogate _end _points:" , end_points , f"SURROGATE_END_POINTS_IS: {srrogate_end_points}--> Using_Clinical_Practice"):
          print(concept) 
# ==================================================================
# Without range() fn print objects
knowledge = ["Data_is_power"]*3
for temp_var in knowledge:
     print(temp_var)

for temp_var in knowledge*5:
     print(temp_var)

for temp_var in ["|Data_is_power|" , {"knowledge":"Data"}]*4:
     print(temp_var) 
#===================================================================
#Task: 
# write a program that takes a number n as an input from user and generates the first n terms 
# of the series formed by squaring the natural number.
person = 2
for i in range(5):
     for temp_var in [person]:
          
          person += 2

          print(temp_var)
# --------------------------------------------------------------------
person = 2
for i in range(5):
     for temp_var in [person**2]:
          
          person += 1

          print(temp_var)

# OR----------------------------------

person = int(input("Enter Number.."))
for i in range(6):
     for temp_var in [person**2]:
          
          person += 1

          print(temp_var) 


# Task: Write a program that prompts the user to input a number and prints its multipliction table

table = int(input("Enter number"))
for temp_var in range(10):  
        
     temp_var += 1

     print(f"{table} * {temp_var} = {table * temp_var}") 

# --------------------------------------------------------------
# critical concep
for temp_var in range(12):
     for table in [5 , 6 , 7 , 8 , 9 , 10]:
          temp_var += 1
          print(f"{table} * {temp_var} = {table * temp_var}\n")     
# --------------------------------------------------------------
# print table of 6 and 6 multiply by only even numbers.
table = 6
for temp_var in range(12):
     
     temp_var += 1
     if temp_var % 2 == 0:
          
          print('__________________')
          print(f"|{table}| * |{temp_var}| = |{table * temp_var}|")
          print('__________________')

print('----------------------------------')


# ----------OR-------------
table = 6
for temp_var in range(2 , 11 , 2):
     print(f"{table} * {temp_var} = {table * temp_var}")
print('___________________')     

#print table of 7 and 7 multiply by only odd numbers.
table_of = 7
for temp_var in range(9):
     temp_var += 1
     if temp_var % 2 == 1:
          print(f"{table_of} * {temp_var} = {table_of * temp_var}")  
        

