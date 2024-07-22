def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"
    
def modulo(a,b):
    return a%b

def floor(a,b):
    return a//b

def pow(a,b):
    return a**b