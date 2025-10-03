# syntax of function 
# def functionname(parameters):
# def is a keyward
# def keyward function header k start ko show krata ha
# calling function --> functionaname()

# creating a function
def my_function():
    print("hello from a function") 

# calling a fn 
my_function() #parenthesis use hota ha fun/method call krty time

# Argument/parameter
# information ko as a argument/parameter store kiya jata ha
def my_function(fname):

    print(fname + "NG's") #concatenation for str

my_function("ANDREW")  

#  --------OR--------

def my_function(fname):

    print(fname + "NG's") #concatenation for str

my_function("ANDREW")
my_function("JOHN")
my_function("ELON")  

# -----OR-------
def my_function(fname):

    print(fname+' '+'NG\'s')

my_function('ANDREW')
my_function("JOHN")
my_function("ELON")  

# -------OR--------
def my_function(fname):

    print(f"{fname} NG's")

my_function("ANDREW")
my_function("JOHN")
my_function("ELON")  

# NUMBER OF ARGUMENTS MORE THEN 1
def my_function(first , last):
    print(f"{first}{last}")

my_function('DEEP' , 'LEARNING')    

def my_function(name , tech):

    print(f'{name} {tech}')

my_function("ANDREW NG" , "FOUNDER_OF_DEEP_LEARNING.")

def my_fn(name , technology):

    print(name+' '+technology)

my_function("ANDREW NG" , "DEEP LEARNING.")   

# Default Parameter Value:
def display(country = "Norway"): #default parameter set 

    print(f"I am from --> {country}.")

display('Pakistan')   
display()
display('Japan')

def display(name , country = 'Norway'):

    print(name +' '+ country)

display('john')   
display('john','Japan') 
display('john','USA')

# Arbitrary Argument: using this sumbol *
# def functionname(*args):
# syntax: 
# def functionname(*parameter):
def my_fn(*kids):
    
    print('The youngest child is' + kids[2])

my_fn('John','Emily','Andrew')

def display(*kids):

    print(kids[3]+' '+'is Intelligent')

display('John','Emily','Andrew','AI','Youtube') 

def walk(*args):

    print('Daily' +' '+ args[2])

walk('running','cycling','physical activity') 

# keyward Arguments
def my_fn(country1 , country2 , country3):

    print('This Is My Country' +' '+ country2)

my_fn(country1='USA',country2='LONDON',country3='AUSTRALIA')  

def my_fn(country1 , country2 , country3):

    print("MY Country id" +' '+ country2)

my_fn(country2='USA' , country3='LONDON' , country1='AFRICA')

# ARBITRARY KEYWARD ARGUMENTS
# syntax:
# def functionname(**kwargs):
# OR ---
# def functionname(**parameter):
def my_fn(**kwargs):

    print('my fname is' +' '+ kwargs['l_name'])

my_fn(f_name = 'Emily' , m_name = 'John' , l_name = 'Gauss')    

# -----------------------------------------------------
# passing a list as an Argument 
def my_fn(food):

    for food in fruits:
        print(f'juicy fruity'+' '+food)

fruits = ["Apple" , "Cherry" , "Orange" , "Mango" , "Watermelon"]        
my_fn(fruits)

# passing a list  as an Argument
def manufacturing(car , Cars):
    
    for material in year_model:
        # print('Name of parts is' +' '+ material)

        for multi in color:
            print('This Car Is' +' '+ multi)
            print('Manufacturing Model IS' +' '+ material)

year_model = ['2015' , '2020' , '2019' , '2013' , '2024' , '2014' , '2010']
color = ['Red' , 'Yellow' , 'Green' , 'Black' , 'Blue' , 'Silver' , 'Grey' , 'aqua']

manufacturing(year_model , color)
  
# Return Values
def num(x):

    return 5 * x 

print(num(2))
print(num(3))
print(num(4))
print(num(7))
print(num(8))

def fruits(apple):
    return 'Apple' + apple
print(fruits('Color Is Red..'))

def eat(mango):
    return 'juicy fruity' +' '+ mango
print(eat('Delicious fruit.'))
 
# minur difference b/w return & lambda 

# Lambda
# syntax:
# lambda argument: expression
x = lambda a : a + 10
print(x(6))

p = lambda x:x + 5
q = lambda y:y * y * y
r = lambda x , y , z : (x + y)/z
#        3 parameter use
print(p(10))
print(q(11))
print(r(12 , 3 , 7)) #3 arguments use

# one parameter/argument use
apple = lambda a : a + 'Red'
banana = lambda b : b + 'Yellow'
orange = lambda o : o + 'orange'

print(apple('3_Apple_is'))
print(banana('12_BANANA_is'))
print(orange('6_ORANGE_is'))

# 3 parameters/argument use
car = lambda a , b , c : (f"CAR IS --> {a+' '+b+' '+c}")
print(car('Red','Grey','Green'))

sigmoid_activation_fn = lambda one , e , z : one / (one + e**-z)
print(sigmoid_activation_fn(1 , 71.81 , 0.01))

dependent = y = lambda m , x , c : m*x+c
print(y(4 , 7 , 0.01))
print(dependent(6 , 10 , 0.01))
print(y(0 , 10 , 0.01))

l = lambda argument : argument + 22
print(l(100))

y    = lambda beta0 , beta1 , x1 , beta2 , x2 : beta0+beta1*x1+beta2*x2
print(y(0.01 , 2 , 4 , 6 , 12))

# lambda fn
def my_fun(n):

    return lambda x : n * x

my_doubler = my_fun(2)
print(my_doubler(11)) 

def flying(birds):

    return lambda sky : birds +' '+ sky

beauti = flying('Parrots')
print(beauti("Can Fly.."))

def Machine(knowledge):

    return lambda set : set + knowledge

intelligent = Machine('Information')
print(intelligent('MACHINE DEPENDENT ON-->'))

def num(number):
    return lambda  binary : binary + number

sum = num(10)
print(sum(1)) 
again_sum = num(2)
print(again_sum(1))

sum = num(10)
again_sum = num(2)
print(sum(1))
print(again_sum(0))

''' lambda ka use tb 
 hoga jb missing 
 function ki need ho'''
