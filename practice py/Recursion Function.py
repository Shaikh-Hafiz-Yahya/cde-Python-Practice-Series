# Recursion Function 
def factorial(n):
    
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
            #  4 * factorial(3)
            #  4 * 3 * factorial(2*1)  
            #  4 * 3 * 2 * 1 
print(factorial(4))    

def factorial(num):

    if num == 0 or num == 1:
        return 1 
    else:
       return num * factorial(num - 1)
    #          5 * factorial(4)
    #          5 * 4 * factorial(3*2)   
    #          5 * 4 * 3 * factorial(2*1)   
    #          5 * 4 * 3 * 2 * factorial(1)  
print(factorial(5))      


def factorial(n):

    if (n == 0 or n == 1):
        return 1
    
    else:
        return 2 * factorial(n-1)
    
print(factorial(3))    
