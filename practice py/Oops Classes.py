# Create a class
class Ai:

    x = 5

print(Ai)   


# Create class and object
class Ai:

    x = 5

obj_information = Ai()
print(obj_information.x)    

# create class and object or using typehunting concept
class Ai:

    x = 5

obj_information:Ai = Ai()
print(obj_information.x)  

# create class , object , build contructor/magic method/initializer , store self parameter
# __init__() <--- initializer function
# . class ---> is a keyward
# . def ---> is a keyward
# . def __init__() <--- constructor/magic method/initializer 
# . self ---> unique parameter 
class Ai:
    def __init__(self):

        x = 5

obj_information:Ai = Ai()
print(obj_information)     

# create class , object , build contructor/magic method/initializer , store self parameter
# constructor main other parameter bhi store krwaein , pass argument , add properties ,using typehunting concept
class Ai:
    #constructor        parameter
    def __init__(self , knowledge): 
  
        self.knowledge = knowledge    # properties

obj_information:Ai = Ai('Set Of Information') #arguments 
print(f'Knowledge --> {obj_information.knowledge}')    


# create class , object , build contructor/magic method/initializer , store self parameter
# Store more then one parameters , pass arguments , add properties  , using typehunting concept
class Ai:
    def __init__(self , knowledge , machine , brain): #using 3 parameters
       
        # three properties 
        self.knowledge = knowledge
        self.machine = machine
        self.intelligent = brain

obj_information:Ai = Ai('set of information' , 'intelligent' , 'billions of parameters')
print(f"Data --> {obj_information.knowledge}")   #Obect properties 
print(f"Problem Solver --> {obj_information.machine}")   #Obect properties 
print(f"{obj_information.intelligent} pr train kiya AI Ko.")  #Obect properties 

# create class , object , build contructor/magic method/initializer , store self parameter
# Store more then one parameters , pass arguments , add properties  , add method and documentation, using typehunting concept
class Ai:
    def __init__(self, knowledge , machine , brain):

        # three properties 
        self.knowledge = knowledge
        self.machine = machine
        self.intelligent = brain
  
    def use_intelligence(self): #Method

        '''use_intelligence method belongs to Ai class
           args: no argument
           return: no return'''

        print(f"Machine-->{self.knowledge}-->Behavior-->Like Human")

obj_information:Ai = Ai('Set of information/Knowledge' , 'Intelligent' , 'Billions of parameters')  

obj_information.use_intelligence() #Object method
print(obj_information.machine)   #Obect properties 

# Modifying Obj properties
class car:
    def __init__(self , color , model , year_of_manufacture):

        self.color = color
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    def start(self):
        print('car is started..')

obj:car = car('blue' , 'Honda' , 2024)
obj.start()
obj.color = 'grey' #Modify
print(obj.color)            

    









       
