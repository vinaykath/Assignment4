def add(a,b):   
    """Adding"""
    return a + b

def subtract(a,b):  
    """Subtracting"""
    return a - b

def multiply(a,b):
    """Multiplying"""
    return a * b

def divide (a,b):
    """Dividing"""
    if b == 0:
        raise ZeroDivisionError("Cannot divde by zero")
    return a /b
