class parents():

    def __init__(self , eyes_color , hair_color):

        self.eyes_color = eyes_color
        self.hair_color = hair_color

    def can_paint(self): #methods
        print(f"have ability to draw/paint arts") 

par_obj:parents = parents('brown' , 'brown') 

print(par_obj.eyes_color)
print(par_obj.hair_color)
par_obj.can_paint()

class child(parents):
    pass

child_obj:child = child('brown' , 'black')
print(child_obj.eyes_color)
print(child_obj.hair_color)
child_obj.can_paint()

# ----OR----
class parents():

    def __init__(self , eyes_color , hair_color):

        self.eyes_color = eyes_color
        self.hair_color = hair_color
    def can_paint(self):
        print(f"have ability to draw/paint arts")   

class child(parents):
    pass  
child_obj:child = child('brown' , 'black')
print(child_obj.eyes_color)
print(child_obj.hair_color)
child_obj.can_paint()   
# --------------------------------------------------
# Topic: super() function in instance method/local method
# eg:1
class ParentClass:

    def parents_method(self):
        print('This is the parent method1')

class ChildClass(ParentClass):

    def parents_method(self):

        print("Harry2")        
        super().parents_method()

    def Child_method(self):

        print('This is the child method.2')
        super().parents_method()

child_obj:ChildClass = ChildClass()
child_obj.Child_method()
child_obj.parents_method()

# diff b/w... above and below
# eg:2 without super() function k inherit nahi kiya parent sy
class ParentClass:
    
    def parents_method(self):
        print('This is the parent method.1')

class ChildClass(ParentClass):

    def parents_method(self):  #override in method/instance method
        print('Harry.2')

    def Child_method(self):
        print('This is the parent method.2') 

obj_ChildClass:ChildClass = ChildClass()
obj_ChildClass.parents_method()
obj_ChildClass.Child_method()

# Topic: super() function in constructor..

# without super() fun 
class ParentClass:
    def __init__(self , name , age , salary):

        self.name = anme
        self.age = age 
        self .salary = salary

class ChildClass(ParentClass):
    def __init__(self , name , age , salary , address):
        
    #    without super() fun  k inherit krna this is bad way 
        self.name = name
        self.age = age 
        self.salary = salary
        self.address = address

obj_ChildClass:ChildClass = ChildClass('john' , 23 , 2000000.00 , 'WXJO28990/USA')  
print(obj_ChildClass.name)
print(obj_ChildClass.address)     

# diff b/w..
# without super() fun 
# class ParentClass:
#     def __init__(self , name , age , salary):

#         self.name = anme
#         self.age = age 
#         self .salary = salary

# class ChildClass(ParentClass):
#     def __init__(self , name , age , salary , address):
        
#         self.address = address

# obj_ChildClass:ChildClass = ChildClass('john' , 23 , 2000000.00 , 'WXJO28990/USA')  

# print(obj_ChildClass.name) #AttributeError: 'ChildClass' object has no attribute 'name'
# print(obj_ChildClass.address) 

# Diff b/w
# Using super() fun 
class ParentClass:
    def __init__(self , name , age , salary):

        self.name = name
        self.age = age 
        self .salary = salary

class ChildClass(ParentClass):
    def __init__(self , name , age , salary , address):
        super().__init__(name , age , salary)  
        self.address = address
   

obj_ChildClass:ChildClass = ChildClass('john' , 23 , 2000000.00 , 'WXJO28990/USA')  

print(obj_ChildClass.name)  # yahan AttributeError nahi mila..
print(obj_ChildClass.address)

class ParentClass():

    def __init__(self , name , age , salary):

        self.name = name
        self.age = age 
        self.salary = salary

    def behavior1(self):
        print(f"{self.name} is Talking to me")

class ChildClass(ParentClass):

    def __init__(self , name , age , salary , address):

        super().__init__(name , age , salary)
        self.address = address

    def behavior2(self):
        print(f"{self.name}_walk_and_talk.")

obj_ChildClass:ChildClass = ChildClass('john' , 23 , 2000000.00 , 'WXJO28990/USA')

obj_ChildClass.behavior2()
obj_ChildClass.behavior1()
print(obj_ChildClass.address)

class ParentClass():

    def __init__(self , name , age , salary):

        self.name = name
        self.age = age 
        self.salary = salary

    def behavior1(self):
        print(f"{self.name} is Talking to me")

class ChildClass(ParentClass):

    def __init__(self , name , age , salary , address):

        super().__init__(name , age , salary)
        self.address = address

    def behavior1(self):  #Override in method
        print(f"{self.name}_walk_and_talk.")

obj_ChildClass:ChildClass = ChildClass('john' , 23 , 2000000.00 , 'WXJO28990/USA')

obj_ChildClass.behavior1()
print(obj_ChildClass.address)
print(obj_ChildClass.salary)

class ParentClass():

    def __init__(self , name , age , salary):

        self.name = name
        self.age = age 
        self.salary = salary

    def behavior1(self):
        print(f"{self.name} is Talking to me")

class ChildClass(ParentClass):

    def __init__(self , name , age , salary , address):

        super().__init__(name , age , salary)
        self.address = address

    def behavior1(self):
        print(f"{self.name}_walk_and_talk.")
        super().behavior1()

obj_ChildClass:ChildClass = ChildClass('john' , 23 , 2000000.00 , 'WXJO28990/USA')

obj_ChildClass.behavior1()
print(obj_ChildClass.address)

class Birds():
    def __init__(self , parrots , doves , eagle):

        self.parrots = parrots
        self.doves = doves 
        self.eagle = eagle

    def fly(self):
        print('beuaty of sky')

    @staticmethod
    def beauty_sky():
        print('birds can fly in the sky..')

class Sky(Birds):
    def __init__(self , parrots , doves , eagle , finches):

        super().__init__(parrots , doves , eagle)

        self.finches = finches

    @staticmethod
    def beauty_sky():
        print('ALL BIRDS CAN FLY IN THE SKY...')

Obj_Sky:Sky = Sky('HERBIVORSE' , 'SMALL' , 'OMNIVORSE' , 'BEAUTI')

Obj_Sky.fly()
Sky.beauty_sky()

class Birds():
    def __init__(self , parrots , doves , eagle):

        self.parrots = parrots
        self.doves = doves 
        self.eagle = eagle

    def fly(self):
        print('beuaty of sky')

    @staticmethod
    def beauty_sky():
        print('birds can fly in the sky..')

class Sky(Birds):
    def __init__(self , parrots , doves , eagle , finches):

        super().__init__(parrots , doves , eagle)

        self.finches = finches

    def beauty_sky(self):
        print('ALL BIRDS CAN FLY IN THE SKY...')
        super().beauty_sky()

Obj_Sky:Sky = Sky('HERBIVORSE' , 'SMALL' , 'OMNIVORSE' , 'BEAUTI')

Obj_Sky.fly()
Obj_Sky.beauty_sky()

class Birds():
    def __init__(self , parrots , doves , eagle):

        self.parrots = parrots
        self.doves = doves 
        self.eagle = eagle

    def fly(self):
        print('beuaty of sky')

    @staticmethod
    def beauty_sky():
        print('birds can fly in the sky..')

class Sky(Birds):
    def __init__(self , parrots , doves , eagle , finches):

        super().__init__(parrots , doves , eagle)

        self.finches = finches

    def beauty_sky(self):
        print('ALL BIRDS CAN FLY IN THE SKY...')
        super().beauty_sky()

Obj_Sky:Sky = Sky('HERBIVORSE' , 'SMALL' , 'OMNIVORSE' , 'BEAUTI')

Obj_Sky.fly()
Obj_Sky.beauty_sky()


class Diagnoses():
    def __init__(self , HeartAttack):

        self.HeartAttack = HeartAttack

    def SurrogateEndPoint(self , Cholestrol , BloodPressure):
    
        self.BloodPressure = BloodPressure
        self.Cholestrol = Cholestrol

    def MedicineUse1(self):
        print(f"CRITICAL CONDITION -->{self.HeartAttack}-->UNDER OBSERVATION -->MONITOR -->{self.Cholestrol} AND MONITOR -->{self.BloodPressure}")

class Treatment(Diagnoses):
    def __init__(self , HeartAttack , Medicine):
        super().__init__(HeartAttack)

        self.Medicine = Medicine

    def MedicineUse2(self):
        print(f"{self.Medicine}--->AFTER MEDICATION COURSE COMPLETED --->COME CLINICAL CHECK-UP..") 
        super().MedicineUse1()   

    @staticmethod 
    def MedicineEffected():
        print('|\|\|\|\|\|\|\|\|/|/|\|\|\|AFTER UNDEROBSERVATION HAERTBEAT IS NORMAL|\|\|\|\|\|\|\|')  

ObjectTreatment:Treatment = Treatment('CARDIO_VASCULAR_DISEASE' , 'STRICTLY_FOLLOW_MEDICATION_COURSE') 

ObjectTreatment.SurrogateEndPoint('Maintain_Cholestrol_LEVEL_Through_Medicine' , 'Maintain_BLOODPRESSURE_LEVEL_Through_Medicine')
ObjectTreatment.MedicineUse2()
Treatment.MedicineEffected()
















