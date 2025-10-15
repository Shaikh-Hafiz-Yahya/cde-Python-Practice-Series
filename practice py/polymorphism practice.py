#Topic: Polymorphism
list = [12 , 20 , 30 , 40 , 50]
print(len(list))

str = "PYTHON_IS_HEART_OF_AI"
print(len(str))

""" 'Polymorphism means same function name (but diff signature) being uses for defferent types'
 liike above program main len() fn use kiya but aik main data type list pss ki or aik main 
 str donoun pr same method kaam kiya but diff answers milay. """


# Topic: polymorphism with Overloading:
# example 1
class ws():
    def display(self , programing = ''):
        print("Welcome to Wscube" + programing) #CONCATENATE

obj:ws = ws()

obj.display()      
# DIFF B/W SAME functions do alg kaam kr rahay hain is called Overloading
obj.display('PYTHON')

# example 2
class String():
    def __init__(self , string):
        
        self.string = string

    def __add__(self , other):
        return String(self.string + other.string) 

    def __str__(self):
        return self.string       

S1:String = String("HELLO")

S2:String = String("WORLD")

S3 = S1 + S2
print(S3)


