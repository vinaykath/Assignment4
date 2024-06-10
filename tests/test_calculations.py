'''My Calculator Test'''
from calculator.actions import add, multiply, subtract, divide

def test_addition_action():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction_action():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication_action():
    '''Test that multiply works'''
    assert multiply(2,2) == 4

def test_division_action():
    '''Test division'''
    assert divide(2,2) == 1

def test_division_zero_action():
    '''Test division by zeor'''
    assert divide(2,0) == None