

#1.-

def doble(x):
    return x * 2

print(doble(5))  
print(doble(3.5)) 


#2.-

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(sumar(1, 2, 3))        
print(sumar(10, 20, 30, 40))
print(sumar(5))               


#3.-

def factorial(n):
    if n == 0 or n == 1:   
        return 1
    return n * factorial(n - 1)  

print(factorial(5))  
print(factorial(0))  
print(factorial(7))  
