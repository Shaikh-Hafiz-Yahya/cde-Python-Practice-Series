# Overriding for method
class Animal():

    def eat(self):
        print('ALL ANIMALS ARE EATING FOOD')

    def eat(self): #Override
        print('DEAR IS A ANIMAL') 

A:Animal = Animal()
A.eat()   

# Overriding for method & CONSTRUCTOR
class Animal():
    def __init__(self , eat , mammals):

        self.eat = eat
        self.mammals = mammals

    def drink(self):
        print('ALL_LIVING_THINGS_BASIC_NEED')
        print(f"ALL ANIMALS ARE EATING {self.eat}|{self.mammals} is a Mammals")

class Lion(Animal):
    def __init__(self , eat , mammals): #overriding for constructor
        super().__init__(eat , mammals)     

    def drink(self): #overriding for method
           print(f"ALL BIRDS & ANIMALS ARE EATING {self.eat}|{self.mammals} is a Animal")
           super().drink()

L:Lion = Lion('Food' , 'Dear') 
L.drink()    

# DIFFERENCE BETWEEN....

class Animal():
    def __init__(self , eat , mammals):

        self.eat = eat
        self.mammals = mammals

    def drink(self):
        print('ALL_LIVING_THINGS_BASIC_NEED')
        print(f"ALL ANIMALS ARE EATING {self.eat}|{self.mammals} is a Mammals")

class Lion(Animal):
    def __init__(self , eat , mammals): #overriding for constructor
        super().__init__(eat , mammals)     

    def drink(self): #overriding for method
           print(f"ALL BIRDS & ANIMALS ARE EATING {self.eat}|{self.mammals} is a Animal")
        #    super().drink()

L:Lion = Lion('Food' , 'Dear') 
L.drink()  

# DIFFERENCE BETWEEN....

class Animal():
    def __init__(self , eat , mammals):

        self.eat = eat
        self.mammals = mammals

    def drink(self):
        print('ALL_LIVING_THINGS_BASIC_NEED')
        print(f"ALL ANIMALS ARE EATING {self.eat}|{self.mammals} is a Mammals")

class Lion(Animal):
    def __init__(self , eat , mammals , color): #overriding for constructor
   
        self.color = color 

    def drink(self): #overriding for method
        print(f"ALL BIRDS & ANIMALS ARE EATING {self.eat}|{self.mammals} is a Animal | ALL ANIMALS ARE NOT {self.color} | PANTHER IS A ANIMAL")
 
L:Lion = Lion('Food' , 'Dear' , 'Black') 
L.drink()   #AttributeError: 'Lion' object has no attribute 'eat' , 'mammals'  
            #Reason: (super() method call nahi kiya but child class main 'Attributes' call kr diya this is wronge)


#   File "c:\Users\dell\Documents\Python\polymorphism practice.py", line 121, in drink
#     print(f"ALL BIRDS & ANIMALS ARE EATING {self.eat}|{self.mammals} is a Animal | ALL ANIMALS ARE NOT {self.color} | PANTHER IS A ANIMAL")
#                                             ^^^^^^^^
# AttributeError: 'Lion' object has no attribute 'eat'

















