'''My Calculator Test'''

from calculator import Calculator


def test_addition():
    '''Test that addition function works '''    
    assert Calculator.addition(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtraction(2,2) == 0

def test_multiply():
    '''Test that addition function works '''    
    assert Calculator.multiplication(2,2) == 4

def test_divide():
    '''Test that addition function works '''    
    assert Calculator.divison(2,2) == 1

def test_zero_divison():
    '''Test that 0 division function works '''    
    assert Calculator.divison(2,0) == None  
