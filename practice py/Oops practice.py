# Task: Student Calss and Attributes and behavior 
# 1. create blueprint
# 2. build constructor
# 3. Attributes/properties ko store kiya constructor main as a parameter
# 4. self.variables 
# 5. create method / behavior
# 6. create obj 
class Student:
    def __init__(self , name , age , marks): #Constructor main attributes/properties as a parameter pss kiyay jate hain

        self.name = name  #properties/Attributes
        self.age = age    #properties/Attributes
        self.marks = marks #properties/Attributes

    def behavior(self): #Method

        """
        behavior method/obj belongs to Student class
        arg:No Arguments
        return:No Return
        """   
        print(f'{self.name} ka behavior study k hawaly sy boht Axha ha but {self.name} is a norty boy..')    

obj_uni:Student = Student('Andrew NG' , 20 , ['SUBJECT_MARKS_ARE' , {'Calculus':90 , 'ML':95 , 'ANN':88 , 'DSA':98 , 'Statistics':99}])

obj_uni.behavior()
print(f'{obj_uni.name}__YOUR__{obj_uni.marks}')
print('Your_Current_Age',obj_uni.age)
# ---------------------------------------------------------------------------------
class Birds():

    def parrot(self): #method

        self.color = input('enter parrot colors.') #properties/attributes
        self.tail_size = float(input('enter parrot tail size in centimeter..'))#properties/attributes

    def fly(self): #method
        print(f'Parrots Fly in the Sky..\nParrot color is {self.color}')

    def talking(self): #method
        print(f'My Parrot is talking to me..\nParrot_Tail_Size = {self.tail_size}')   

beauti_sky:Birds = Birds()

beauti_sky.parrot()  #paranthesis use
beauti_sky.fly()     #paranthesis use
beauti_sky.talking() #paranthesis use

# ----------------------------------------------------------------------------------
class Birds():

    def __init__(self): #constructor

        self.color = input('enter parrot colors.') #properties/attributes
        self.tail_size = float(input('enter parrot tail size in centimeter..'))#properties/attributes

    def fly(self):
        print(f'Parrots Fly in the Sky..\nParrot color is {self.color}')

    def talking(self):
        print(f'My Parrot is talking to me..\nParrot_Tail_Size = {self.tail_size}')   

beauti_sky:Birds = Birds()

beauti_sky.fly()     #paranthesis use
beauti_sky.talking() #paranthesis use

# ---------------------------------------------------------------------------------
class Birds():

    def __init__(self , color , tail_size): #Using constructor

        self.color = color #properties/attributes
        self.tail_size = tail_size #properties/attributes

    def fly(self):
        print(f'Parrots Fly in the Sky..\nParrot color is {self.color}')

    def talking(self):
        print(f'My Parrot is talking to me..\nParrot_Tail_Size = {self.tail_size}')   

beauti_sky:Birds = Birds(['Yellow','Green','Orange','Grey'] , 30.8)

beauti_sky.fly()     #paranthesis use
beauti_sky.talking() #paranthesis use
print('Parrot_color_is_',beauti_sky.color) #properties/attributes call krty time () not use


